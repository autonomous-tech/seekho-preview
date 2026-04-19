#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0"]
# ///
"""Batch driver: call generate_image.py, then resize/crop to target JPG."""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from PIL import Image

GENERATOR = "/home/rizki/work/autonomous/repos/products/openclaw/skills/nano-banana-pro/scripts/generate_image.py"
OUT_DIR = Path("/home/rizki/work/autonomous/scratch/seekho/images")
TMP_DIR = Path("/home/rizki/work/autonomous/scratch/seekho/image-gen-batch/raw")
TMP_DIR.mkdir(parents=True, exist_ok=True)


def pick_resolution(w: int, h: int) -> str:
    m = max(w, h)
    if m <= 1024:
        return "1K"
    if m <= 2048:
        return "2K"
    return "2K"  # 2K is enough for our largest target (1600)


def center_crop_resize(src: Path, dst: Path, target_w: int, target_h: int, quality: int = 85) -> int:
    img = Image.open(src)
    if img.mode != "RGB":
        img = img.convert("RGB")
    sw, sh = img.size
    target_ratio = target_w / target_h
    src_ratio = sw / sh
    if src_ratio > target_ratio:
        new_w = int(sh * target_ratio)
        left = (sw - new_w) // 2
        img = img.crop((left, 0, left + new_w, sh))
    else:
        new_h = int(sw / target_ratio)
        top = (sh - new_h) // 2
        img = img.crop((0, top, sw, top + new_h))
    img = img.resize((target_w, target_h), Image.LANCZOS)
    img.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    return dst.stat().st_size


def generate_one(name: str, prompt: str, width: int, height: int, api_key: str, fmt: str = "jpg", quality: int = 85) -> tuple[bool, str]:
    resolution = pick_resolution(width, height)
    raw_png = TMP_DIR / f"{name}.png"
    if raw_png.exists():
        raw_png.unlink()

    cmd = [
        "uv", "run", GENERATOR,
        "--prompt", prompt,
        "--filename", str(raw_png),
        "--resolution", resolution,
        "--api-key", api_key,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        return False, f"timeout after 300s"
    if result.returncode != 0:
        err = (result.stderr or result.stdout).strip().splitlines()[-1] if (result.stderr or result.stdout) else "unknown"
        return False, f"generator failed: {err[:200]}"
    if not raw_png.exists():
        return False, "generator produced no file"

    if fmt == "png":
        dst = OUT_DIR / f"{name}.png"
        img = Image.open(raw_png)
        if img.mode != "RGB" and img.mode != "RGBA":
            img = img.convert("RGBA")
        sw, sh = img.size
        target_ratio = width / height
        src_ratio = sw / sh
        if src_ratio > target_ratio:
            new_w = int(sh * target_ratio)
            left = (sw - new_w) // 2
            img = img.crop((left, 0, left + new_w, sh))
        else:
            new_h = int(sw / target_ratio)
            top = (sh - new_h) // 2
            img = img.crop((0, top, sw, top + new_h))
        img = img.resize((width, height), Image.LANCZOS)
        img.save(dst, "PNG", optimize=True)
        size = dst.stat().st_size
    else:
        dst = OUT_DIR / f"{name}.jpg"
        size = center_crop_resize(raw_png, dst, width, height, quality=quality)

    return True, f"{size // 1024}KB"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--config", required=True, help="JSON file with list of {name, prompt, w, h, fmt?, quality?}")
    parser.add_argument("--only", help="Only run images whose name contains this substring")
    parser.add_argument("--skip-existing", action="store_true", help="Skip images whose output already exists at target size")
    parser.add_argument("--parallel", type=int, default=1, help="Number of parallel generations")
    parser.add_argument("--names", help="Comma-separated exact names to include")
    args = parser.parse_args()

    with open(args.config) as f:
        images = json.load(f)

    if args.only:
        images = [img for img in images if args.only in img["name"]]
    if args.names:
        wanted = set(n.strip() for n in args.names.split(","))
        images = [img for img in images if img["name"] in wanted]

    total_generated = 0
    total_size = 0
    failures = []

    def worker(img):
        name = img["name"]
        fmt = img.get("fmt", "jpg")
        ext = "png" if fmt == "png" else "jpg"
        out_path = OUT_DIR / f"{name}.{ext}"
        ok, detail = generate_one(
            name=name,
            prompt=img["prompt"],
            width=img["w"],
            height=img["h"],
            api_key=args.api_key,
            fmt=fmt,
            quality=img.get("quality", 85),
        )
        return name, ext, out_path, ok, detail

    if args.parallel <= 1:
        results = [worker(img) for img in images]
    else:
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            futures = [ex.submit(worker, img) for img in images]
            results = []
            for fut in as_completed(futures):
                results.append(fut.result())

    for name, ext, out_path, ok, detail in results:
        if ok:
            print(f"[OK] {name}.{ext} ({detail})", flush=True)
            total_generated += 1
            try:
                total_size += out_path.stat().st_size
            except OSError:
                pass
        else:
            print(f"[FAIL] {name}: {detail}", flush=True)
            failures.append((name, detail))

    print()
    print(f"=== SUMMARY ===")
    print(f"Generated: {total_generated}/{len(images)}")
    print(f"Total size: {total_size // 1024}KB ({total_size / 1024 / 1024:.1f}MB)")
    if failures:
        print(f"Failures ({len(failures)}):")
        for n, d in failures:
            print(f"  - {n}: {d}")


if __name__ == "__main__":
    main()
