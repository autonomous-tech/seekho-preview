# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0"]
# ///
"""Generate on-brand Seekho placeholder images (JPG + PNG favicons + SVG).

Brand palette:
  - deep green #0D4A2F (brand)
  - lime       #6EE086 (accent)
  - cream      #F9F8F4 (bg)
"""

from __future__ import annotations
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/home/rizki/work/autonomous/scratch/seekho/images")
OUT.mkdir(parents=True, exist_ok=True)

GREEN = (13, 74, 47)      # #0D4A2F
LIME  = (110, 224, 134)   # #6EE086
CREAM = (249, 248, 244)   # #F9F8F4
INK   = (20, 30, 25)

def pick_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bb = draw.textbbox((0, 0), test, font=font)
        if (bb[2] - bb[0]) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_placeholder(path: Path, w: int, h: int, label: str, kind: str):
    """Draw a placeholder tile. kind in: 'hero','og','portrait','contextual','book','icon'."""
    # Background: cream with green border; accent bar on one side
    img = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(img)

    # Border
    border = max(4, min(w, h) // 200)
    d.rectangle([0, 0, w - 1, h - 1], outline=GREEN, width=border)

    # Top brand bar (green) with lime underline
    bar_h = max(24, h // 14)
    d.rectangle([0, 0, w, bar_h], fill=GREEN)
    d.rectangle([0, bar_h, w, bar_h + max(4, bar_h // 6)], fill=LIME)

    # Brand wordmark
    brand_font = pick_font(max(14, bar_h // 2))
    d.text((max(12, w // 60), bar_h // 6), "SEEKHO", font=brand_font, fill=CREAM)

    # Type badge top-right
    type_font = pick_font(max(10, bar_h // 3))
    type_txt = f"PLACEHOLDER · {w}×{h} · {kind.upper()}"
    bb = d.textbbox((0, 0), type_txt, font=type_font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((w - tw - max(12, w // 60), bar_h // 4), type_txt, font=type_font, fill=LIME)

    # Central label area (what real image should show)
    inner_pad = max(24, min(w, h) // 20)
    inner_top = bar_h + inner_pad
    inner_bottom = h - inner_pad
    inner_left = inner_pad
    inner_right = w - inner_pad
    max_text_w = inner_right - inner_left

    # Title "REAL IMAGE GOES HERE"
    title_font = pick_font(max(16, min(w, h) // 22))
    title = "REAL PHOTOGRAPHY"
    bb = d.textbbox((0, 0), title, font=title_font)
    tw = bb[2] - bb[0]
    d.text(((w - tw) // 2, inner_top), title, font=title_font, fill=GREEN)
    title_h = bb[3] - bb[1]

    # Label body (wrapped)
    label_font = pick_font(max(13, min(w, h) // 32))
    lines = wrap_text(d, label, label_font, max_text_w)
    line_h = d.textbbox((0, 0), "Ay", font=label_font)[3] + 6
    total_h = line_h * len(lines)
    y = inner_top + title_h + 20
    # If overflow, shrink
    if y + total_h > inner_bottom - 40:
        label_font = pick_font(max(10, min(w, h) // 42))
        lines = wrap_text(d, label, label_font, max_text_w)
        line_h = d.textbbox((0, 0), "Ay", font=label_font)[3] + 4
        total_h = line_h * len(lines)

    for i, ln in enumerate(lines):
        bb = d.textbbox((0, 0), ln, font=label_font)
        lw = bb[2] - bb[0]
        d.text(((w - lw) // 2, y + i * line_h), ln, font=label_font, fill=INK)

    # Footer note
    note_font = pick_font(max(10, min(w, h) // 48))
    note = "Replace with real photo · brief: scratch/seekho/copy/image-gen-brief.md"
    bb = d.textbbox((0, 0), note, font=note_font)
    lw = bb[2] - bb[0]
    d.text(((w - lw) // 2, h - inner_pad - (bb[3] - bb[1]) - 4), note, font=note_font, fill=(100, 105, 102))

    # Save
    if path.suffix.lower() in (".jpg", ".jpeg"):
        img.save(path, "JPEG", quality=82, optimize=True)
    else:
        img.save(path, "PNG", optimize=True)

def draw_icon(path: Path, size: int, bg=GREEN, fg=LIME):
    """Square S-mark icon — solid bg, big bold S centered."""
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    # scale font to ~60% of canvas
    font = pick_font(int(size * 0.62))
    txt = "S"
    bb = d.textbbox((0, 0), txt, font=font)
    tw = bb[2] - bb[0]
    th = bb[3] - bb[1]
    # visual-center adjustment (fonts sit low)
    x = (size - tw) // 2 - bb[0]
    y = (size - th) // 2 - bb[1] - int(size * 0.02)
    d.text((x, y), txt, font=font, fill=fg)
    if path.suffix.lower() in (".jpg", ".jpeg"):
        img.save(path, "JPEG", quality=90)
    else:
        img.save(path, "PNG", optimize=True)

# ---------- Specification ----------
# (filename, width, height, kind, label)
SPEC = [
    # Heroes
    ("hero-homepage.jpg", 800, 1000, "hero", "Hero: Female Pakistani instructor + young woman student in Toyota Corolla on quiet DHA Karachi commercial street, golden hour, warm documentary style."),
    ("hero-dha.jpg", 800, 1000, "hero", "Hero: Silver Honda City on tree-lined DHA Phase 6 street with L learner sticker, student at wheel + female instructor, overcast soft light."),
    ("hero-clifton.jpg", 800, 1000, "hero", "Hero: White Suzuki Swift on Clifton Block 5 street, woman driver making a left turn, female instructor coaching, sea-breeze late afternoon."),
    ("hero-ladies.jpg", 800, 1000, "hero", "Hero: Young Pakistani woman in Toyota Yaris adjusting rearview mirror; female instructor in cream hijab smiling, dual-brake visible, golden light."),
    ("hero-automatic.jpg", 800, 1000, "hero", "Hero: Close-up student's hand on automatic gear shifter (P-R-N-D), instructor gesturing at dashboard, shallow DOF, warm windscreen light."),
    ("hero-programme.jpg", 1600, 900, "hero", "Hero wide: Small Seekho classroom — 5 Pakistani students at light-wood tables, female instructor at whiteboard with road-sign diagrams. Natural window light."),
    ("hero-traffic-club.jpg", 1600, 900, "hero", "Hero wide: Pakistani schoolchildren ages 8–12 around miniature traffic cones in school playground, female Seekho instructor demonstrating crosswalk."),
    ("hero-book.jpg", 800, 600, "book", "Book-page hero: Smiling female driving instructor on phone, professional Seekho academy interior background."),
    ("book-sidebar-team.jpg", 600, 800, "book", "Book sidebar: 5 female Seekho instructors standing beside white sedan on DHA commercial side street, golden hour, warm & approachable."),

    # Instructor portraits — brief specifies 600x600; team-lead override says 400x400.
    # We'll produce BOTH the 400x400 sized ones listed by team-lead AND keep naming per brief.
    ("instructor-omaima.jpg", 400, 400, "portrait", "Portrait: Omaima — Pakistani woman early 30s, shoulder-length dark hair, sage-green long-sleeve shirt, warm genuine smile, natural daylight, cream bokeh bg."),
    ("instructor-farkhanda.jpg", 400, 400, "portrait", "Portrait: Farkhanda — Pakistani woman late 30s, soft taupe hijab, charcoal shawl, confident approachable smile with laugh lines, natural afternoon window light."),
    ("instructor-zainab.jpg", 400, 400, "portrait", "Portrait: Zainab — Pakistani woman late 20s, no hijab, low ponytail, cream button-down sleeves rolled, relaxed slight smile, outdoor palm-frond bokeh."),
    ("instructor-tehreem.jpg", 400, 400, "portrait", "Portrait: Tehreem — Pakistani woman early 30s, plum chiffon dupatta on shoulders, olive kurta, warm smile outdoors in late-afternoon light."),
    ("instructor-muzaffar.jpg", 400, 400, "portrait", "Portrait: Muzaffar — Pakistani male instructor early 40s, short dark hair, trimmed beard, sage-green collared shirt, warm trustworthy smile, natural daylight."),
    # Brief placeholder additions (if about.html uses them, keep parity)
    ("instructor-placeholder-a.jpg", 600, 600, "portrait", "Portrait placeholder A: Pakistani woman mid-40s, soft beige hijab, deep teal top, kind motherly presence, natural daylight."),
    ("instructor-placeholder-b.jpg", 600, 600, "portrait", "Portrait placeholder B: Pakistani woman late 20s, shoulder-length hair no hijab, rust-coloured shirt, relaxed professional smile, warm beige interior bokeh."),
    ("instructor-placeholder-c.jpg", 600, 600, "portrait", "Portrait placeholder C: Pakistani male instructor early 40s, sage-green collared shirt, warm smile — reassurance for male learners."),
    ("instructor-placeholder-d.jpg", 600, 600, "portrait", "Portrait placeholder D: Pakistani woman mid-30s, navy-blue dupatta on shoulders, cream blouse, calm confident smile, natural window light."),

    # Founder
    ("faryal-portrait.jpg", 800, 1000, "portrait", "About-page founder: Faryal Farooqui (Pakistani woman late 30s/early 40s), shoulder-length dark hair, deep green blazer, confident warm smile, modern office bokeh."),
    ("founder-faryal.jpg", 600, 600, "portrait", "Founder square: Faryal Farooqui — founder & CEO of Seekho Pakistan, confident warm portrait, soft window light."),

    # Team group (brief-aligned + team-lead's requested name)
    ("team-group.jpg", 1200, 800, "hero", "Team group: 6-8 Pakistani driving instructors (majority female) outside modern sedan, professional but approachable, warm DHA street."),

    # Contextual
    ("contextual-student-smile.jpg", 1200, 800, "contextual", "Context: Young Pakistani woman in Toyota Yaris driver's seat beaming after first lesson, hands on wheel, DHA bokeh through window."),
    ("contextual-instruction-moment.jpg", 1200, 800, "contextual", "Context: Over-the-shoulder view of instructor (cream hijab, clipboard) animatedly explaining to student driving on tree-lined DHA street."),
    ("contextual-parallel-parking.jpg", 1200, 800, "contextual", "Context: White sedan mid-manoeuvre parallel-parking between two cars on narrow DHA Bukhari Commercial side street, warm afternoon light."),
    ("contextual-night-drive.jpg", 1200, 800, "contextual", "Context: Over-the-shoulder student driving on Karachi main road at dusk/blue hour, warm orange streetlights, dashboard glow, slight motion blur."),
    ("contextual-street-pov.jpg", 1200, 800, "contextual", "Context: Driver's POV through windshield — quiet tree-lined DHA commercial street with palm trees, low-rise shops, afternoon light."),
    ("contextual-certificate.jpg", 1200, 800, "contextual", "Context: Close-up of hands holding a simple cream-and-gold completion certificate, warm wood-toned office background, shallow DOF."),

    # Team-lead optional extras using alt filenames
    ("student-smiling-driver-seat.jpg", 800, 600, "contextual", "Context: Pakistani woman student grinning in driver's seat after lesson, warm natural light, clean car interior."),
    ("instructor-guiding-wheel.jpg", 800, 600, "contextual", "Context: Instructor gently guiding a student's grip on the steering wheel, close-up hands and wheel, warm afternoon light."),
    ("parallel-parking-practice.jpg", 800, 600, "contextual", "Context: Student practising parallel parking between two cars on a quiet DHA commercial street."),
    ("completion-certificate-closeup.jpg", 800, 600, "contextual", "Context: Close-up of Seekho driver's education completion certificate held by graduating student."),

    # OG images (1200x630)
    ("og-homepage.jpg", 1200, 630, "og", "OG: Seekho homepage — female instructor + student in white Corolla, warm golden-hour DHA street, left-third empty for headline overlay."),
    ("og-packages.jpg", 1200, 630, "og", "OG: Packages — modern car dashboard with keys + folded (illegible) price sheet + pen; 'confident decision' mood, left half for headline."),
    ("og-book.jpg", 1200, 630, "og", "OG: Book — Pakistani woman's hand holding smartphone with WhatsApp green interface (text illegible), warm cream wooden table left."),
    ("og-about.jpg", 1200, 630, "og", "OG: About — 4-5 Pakistani women instructors beside white sedan, DHA golden hour, subjects right 60%."),
    ("og-faq.jpg", 1200, 630, "og", "OG: FAQ — smiling Pakistani woman in driver's seat turning toward camera as if asking a question, warm natural light."),
    ("og-program.jpg", 1200, 630, "og", "OG: Programme — split composition: right = whiteboard with abstract road-sign sketches + marker hand; left = car seen through window."),
    ("og-ladies.jpg", 1200, 630, "og", "OG: Ladies — two Pakistani women in car (instructor cream hijab, student at wheel), left-third empty, warm empathetic documentary style."),
    ("og-dha.jpg", 1200, 630, "og", "OG: DHA — white sedan with L sticker on tree-lined DHA Phase 6 street, palm trees, cream buildings, left-third empty."),
    ("og-clifton.jpg", 1200, 630, "og", "OG: Clifton — white Suzuki Swift on Clifton Block 5 street, sea-breeze feel, late-afternoon warm light, left-third for overlay."),
    ("og-automatic.jpg", 1200, 630, "og", "OG: Automatic — close-up of automatic gear shifter with woman's hand and bracelet, warm sunlight through windscreen."),
    ("og-traffic-club.jpg", 1200, 630, "og", "OG: Traffic Club — Pakistani schoolchildren around miniature traffic cones and signs in playground, female instructor gesturing."),
    ("og-careers.jpg", 1200, 630, "og", "OG: Careers — female instructor 30s in soft hijab + sage shirt leaning on Seekho training car holding keys, DHA street."),
    ("og-press.jpg", 1200, 630, "og", "OG: Press — Faryal-style founder portrait beside Seekho training car, DHA street, warm natural afternoon light, editorial feel."),
]

def main():
    created = []
    skipped = []
    for fname, w, h, kind, label in SPEC:
        path = OUT / fname
        try:
            draw_placeholder(path, w, h, label, kind)
            created.append((fname, w, h, path.stat().st_size))
        except Exception as e:
            skipped.append((fname, str(e)))

    # Favicons / icons
    # Source 512 (brief + team-lead both want a mark)
    draw_icon(OUT / "icon-source-512.png", 512)
    draw_icon(OUT / "icon-512.png", 512)
    draw_icon(OUT / "icon-192.png", 192)
    draw_icon(OUT / "apple-touch-icon.png", 180)
    draw_icon(OUT / "favicon-32.png", 32)
    draw_icon(OUT / "favicon-16.png", 16)

    # favicon.ico (multi-size)
    ico_img = Image.new("RGB", (64, 64), GREEN)
    d = ImageDraw.Draw(ico_img)
    f = pick_font(40)
    bb = d.textbbox((0, 0), "S", font=f)
    d.text(((64 - (bb[2]-bb[0])) // 2 - bb[0], (64 - (bb[3]-bb[1])) // 2 - bb[1] - 2), "S", font=f, fill=LIME)
    ico_img.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # favicon.svg — crisp vector S-mark
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="10" fill="#0D4A2F"/>
  <text x="32" y="46" font-family="'Helvetica Neue', Arial, sans-serif"
        font-weight="800" font-size="44" fill="#6EE086" text-anchor="middle">S</text>
</svg>
'''
    (OUT / "favicon.svg").write_text(svg, encoding="utf-8")

    # Summary
    print(f"\n=== Created {len(created)} placeholder JPGs ===")
    total_bytes = 0
    for n, w, h, b in created:
        total_bytes += b
        print(f"  {n}  {w}x{h}  {b//1024}KB")

    # Icons summary
    icons = [
        "icon-source-512.png", "icon-512.png", "icon-192.png",
        "apple-touch-icon.png", "favicon-32.png", "favicon-16.png",
        "favicon.ico", "favicon.svg",
    ]
    print(f"\n=== Icons ({len(icons)}) ===")
    for n in icons:
        p = OUT / n
        if p.exists():
            print(f"  {n}  {p.stat().st_size//1024 if p.stat().st_size>=1024 else p.stat().st_size}{'KB' if p.stat().st_size>=1024 else 'B'}")

    if skipped:
        print(f"\n=== Skipped ({len(skipped)}) ===")
        for n, e in skipped:
            print(f"  {n}: {e}")

    print(f"\nTotal placeholder bytes: {total_bytes/1024:.1f} KB")
    print(f"Output: {OUT}")

if __name__ == "__main__":
    main()
