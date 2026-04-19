# Seekho — Real Brand Identity (from live site + assets)

**Source of truth:** `https://seekhopakistan.com.pk/assets/css/style.css` + `index.html` + logo asset `Group 33.png`, fetched 2026-04-19.

> **Correction vs. audit-report.md §12:** the previous audit guessed the palette was "red/white/black". That is **wrong**. The real live site is **purple-dominant** (`#4E0CB9`). No red appears in the custom CSS except a single Bootstrap danger `#dc3545`. Treat that audit bullet as an error.

---

## 1. Primary palette (HEX codes + evidence)

All hex codes below are copied directly from `/assets/css/style.css`. Confidence is based on count + semantic weight of the selector.

| Role | Color | HEX | Evidence | Confidence |
|------|-------|-----|----------|------------|
| **Brand primary** (dominant) | Deep violet | `#4E0CB9` | `body { background: #4E0CB9 }` (line 9), `.menu_overlay { background: #4E0CB9 }` (line 203), full-bleed modal sections `.about-us, .press, .contact-us, .faqs, .our-partner` (lines 647, 653), mobile menu overlay (line 862). **This is THE Seekho color — the page sits on it.** | Very High |
| **Brand secondary** (interactive) | Muted purple | `#52367C` | `.button_container` CTAs (line 136), slider arrow hover (line 1280), modal close-button containers (lines 499, 727), `.show-btn` hover state (line 727) | Very High |
| Text on dark | Pure white | `#FFFFFF` | Body text when on purple bg (e.g. line 648 `color: white` on `.about-us` etc.) | Very High |
| Surface / modal inner | Off-white | `#FFF` + `#f1f1f1` | Modal card interiors | High |
| Bright accent 1 | Sun yellow | `#FFE51F` | Price highlights in packages (lines 548, 814, 837), used to call out numbers | High (decorative) |
| Bright accent 2 | Electric pink | `#FF2994` / `#EC5580` | Price/label accents (lines 132, 1500) | Medium |
| Bright accent 3 | Clear blue | `#2983EF` | Package labels (lines 1492, 1513, 2514) | Medium |
| Bright accent 4 | Emerald green | `#198D49` | Package labels, success-ish (lines 572, 1488, 1521) | Medium |
| Bright accent 5 | Amber | `#E89707` | Package labels (lines 1496, 1505) | Low-Medium |
| Mint highlight | Mint | `#7CFFB2` | Hover/success micro-accents (lines 620, 624) | Low |
| Functional grey | Line | `#707070` / `#C1C1C1` | Borders between nav items, 16 uses of `#707070` | Very High (structural) |
| Text muted | Mid grey | `#727272` / `#434343` / `#504F52` | Lines 1213, 1217, 1392 | Medium |
| Functional red | Bootstrap danger | `#dc3545` | Used once or twice for a label swatch (lines 1484, 1517). **Not a brand color.** | Low |

**Load-bearing summary (for the redesign):** `#4E0CB9` (hero/nav/overlay), `#52367C` (CTAs, hovers), white, and the set of bright accents (yellow/pink/blue/green/amber) that Seekho uses as **per-package colour coding** on their price cards. That per-package coding is a genuine brand habit worth preserving — each program card gets its own accent.

## 2. Recommended Seekho CSS palette (my synthesis)

Keep the violet identity, sharpen the secondary into a more confident purple-wine, tighten the accents to two primary companions (yellow + green) so the site doesn't feel like a Skittles packet, and add a proper WhatsApp green + dark ink for type.

```css
:root {
  /* ---------- Brand primary (violet) ---------- */
  --violet:         #4E0CB9;   /* EXACT brand — hero, nav, overlays, big CTA backgrounds */
  --violet-dark:    #3A0890;   /* Hover state, active nav, pressed buttons */
  --violet-light:   #7A4DD6;   /* Tints, badge backgrounds, subtle surfaces on white */
  --violet-wine:    #52367C;   /* Exact existing secondary — muted purple for card headers */

  /* ---------- Ink & surface ---------- */
  --ink:            #1B0E3A;   /* Violet-biased near-black — headings on light backgrounds */
  --ink-soft:       #3A2F5C;   /* Body copy on light bg */
  --cream:          #FBF8F3;   /* Warm off-white — primary surface, warmer than #FFF */
  --white:          #FFFFFF;   /* Pure — modal interiors, card bodies */
  --muted:          #6B6385;   /* Violet-tinted grey for meta / muted text */
  --line:           #E5E0EE;   /* Violet-tinted divider — replaces generic #C1C1C1 */

  /* ---------- Accent (two only — preserve per-program coding habit) ---------- */
  --gold:           #FFC93C;   /* Warmed-up version of #FFE51F — headline numbers, price tags */
  --gold-dark:      #D9A517;   /* Hover for gold CTAs / text on yellow */

  /* ---------- Functional ---------- */
  --success:        #1E8A4A;   /* From existing #198D49 — completion ticks, verified badges */
  --wa:             #25D366;   /* WhatsApp official green — for WA CTA only */
  --wa-dark:        #128C7E;   /* WA hover */
  --danger:         #DC3545;   /* Form errors only — never brand */

  /* ---------- Program colour-coding (optional accents for package cards) ---------- */
  --pkg-learn:      #FFC93C;   /* "Teach Me Everything" (headline product) */
  --pkg-refresh:    #2983EF;   /* "Enhance My Skills" */
  --pkg-student:    #1E8A4A;   /* "Student Bundle" */
  --pkg-ladies:     #EC5580;   /* "Ladies" page accent only */
}
```

**Why these choices:**
- `#4E0CB9` stays because it's the only genuinely recognisable part of Seekho's current brand and the body background of the entire legacy site.
- `--violet-dark` and `--violet-light` are derived tones to give us hover and tint states — the legacy CSS has no such system.
- `--cream` (warm off-white) lifts the violet instead of fighting it; pure #FFF on deep violet can feel clinical.
- `--ink` is violet-biased rather than neutral black — subtle hint of brand in every paragraph.
- The five legacy accents (yellow/pink/blue/green/amber) are reduced to **gold + success + WA + danger**, with the legacy per-package colour habit preserved as optional `--pkg-*` tokens. This gives the designer a defensible, disciplined system while respecting Seekho's actual visual quirk of colour-coding each program.

## 3. Typography

**Current site:**
- Only custom family is **Roboto 300** — pulled from Google Fonts via `<link>` in `index.html:19` and in `style.css` line 1. Weight 300 is applied to `body h2, h3, h4, h5, h6, p`.
- Font Awesome 5 Free for icons.
- Bootstrap default stack as fallback.

**Diagnosis:** Roboto 300 across everything — including headings — is why the site reads generic and weightless. There is no display face and no numerical hierarchy. Roboto was fine in 2017; in 2026 it signals "Bootstrap template".

**Recommended pairing** (sans + sans — keep it modern, Pakistani market reads better on geometric sans than serif):

- **Display:** **Space Grotesk** (600/700) — confident, geometric, slightly quirky, pairs beautifully with violet. Free on Google Fonts.
- **Body:** **Inter** (400/500) — clearest possible reading type for long-form pages (prices, testimonials, FAQ). Free on Google Fonts.
- **Optional numerical / tabular accent:** **JetBrains Mono** — only for price tables / "PKR 15,000" callouts. Gives the gold price a "receipt" feel.

Fallback stack:
```css
--font-display: "Space Grotesk", "Helvetica Neue", Arial, sans-serif;
--font-body:    "Inter", "Helvetica Neue", Arial, sans-serif;
--font-mono:    "JetBrains Mono", ui-monospace, Menlo, monospace;
```

No brand font licence is implied by the logo — the wordmark is a custom-drawn bold sans; we do **not** need to licence a specific face.

## 4. Logo

**File:** `assets/images/header-images/Group 33.png` — 268×57 PNG, pure-white-on-transparent.

**Composition:** horizontal lockup — **wordmark only**, with the final "O" redrawn as a stylised steering-wheel mark (circle with three internal spokes forming a rotated "Y" or steering-wheel grip). Letterforms are a heavy, tight-tracked geometric sans close to Montserrat Black or Gotham Bold. Proportions roughly 5:1 wide-to-tall.

**Mark vs wordmark:** technically a **combination mark** — the "O" is the brand icon, but it's inseparable from the wordmark. There is no standalone "Seekho O" icon provided in the fetched assets.

**How it's used on the current site:** reused 8+ times across modal headers/footers (see audit note line 432). Always rendered in **white on purple** — the asset is mono-white, meaning the colour comes from the background, not the logo.

**Preserve in redesign:**
- Keep the steering-wheel-O as the brand icon. Commission a **standalone favicon/app-icon version** (we may already have `favicon.svg` / `apple-touch-icon.png` locally — check).
- Deliver three logo variants: white (existing), deep violet `#4E0CB9` (for light backgrounds), and near-black `#1B0E3A` (for neutral press/one-pagers).
- Don't rebuild the wordmark from scratch; re-trace it cleanly as SVG to replace the 268×57 raster.

**Confirm with Faryal:** is "Group 33.png" the current official logo? The filename suggests a Figma export layer name, not a deliberate brand-asset name — possible the logo has been revised and the website was never updated.

## 5. Photography mood (for image-gen agent reference)

Could not fetch Instagram/Facebook or vehicle photos (WebFetch returned no decoded images for `instagram.com/seekho.pk` or `facebook.com/Seekho.org`; no browser available locally for screenshots; Google image search not attempted as it would be guess-work without visual confirmation).

**What I know from existing local assets** (`/scratch/seekho/images/`): the current redesign already has placeholder imagery aligned with the positioning — `hero-ladies.jpg`, `contextual-street-pov.jpg`, `contextual-parallel-parking.jpg`, `instructor-*.jpg`, `founder-faryal.jpg`, vehicle-interior shots.

**Recommended direction** (based on audit-report.md observations and Seekho's positioning around fear→confidence, female-instructor-led, Karachi roads):

- **Subjects:** Karachi women drivers, Pakistani instructors, white/silver Suzuki Swift and Alto interiors (matches "our fleet" copy). No stock imagery of European highways.
- **Lighting:** warm late-afternoon / golden hour — Karachi has incredible end-of-day light and it visually matches the warm-cream/violet palette better than harsh midday sun.
- **Framing:** tight on hands-on-wheel, over-shoulder from passenger seat (instructor POV), eye-level student portraits with visible **confident smile** (the emotional arc is fear → confidence — photography must end on confidence).
- **Environment:** recognisable Karachi — Clifton, Sea View, DHA phase streets, school gates in Gulshan/Nazimabad — avoid generic anonymous asphalt.
- **Colour treatment:** slight warm-up, retain Pakistani skin tones accurately, no heavy Instagram filter. The violet brand tone is applied via UI chrome and overlays — photos stay naturally coloured.
- **Avoid:** cartoon mascots, stock "woman with car key dangling from fingertip", thumbs-up clip art, traffic-cone illustrations.

**Follow-up:** ask Faryal to share (a) their Instagram Drive folder if one exists, (b) any vehicle-wrap photos for decal-colour reference, and (c) the Aurora 2019 spread photos which were professionally shot.

## 6. Visual tone

Professional, confident, slightly premium — **not** a discount driving school, **not** a government safety poster. The current site leans institutional (big purple slabs, uppercase nav) which is good for trust but sabotages itself with template-grade Roboto 300 and no hierarchy. The redesign should keep the institutional confidence of the deep violet while adding **warmth** (cream surface, Pakistani faces, gold numerical accents) and **clarity** (real headings, tabular prices, badges). Think: "licensed practice, not a friend teaching you in their uncle's car".

## 7. Designer's brief (one paragraph)

Keep the safaikaro-derived CSS architecture intact — radii, borders, card shapes, component scaffolding all stay. Swap the palette wholesale to the `--violet / --violet-wine / --cream / --ink / --gold / --wa` token set above, applying `#4E0CB9` as the hero / nav / footer / section-break anchor (this is the one colour Karachi actually associates with Seekho). Replace Roboto 300 globally with Space Grotesk 600/700 for display and Inter 400/500 for body, introducing a real type-scale — display numbers (prices, stats) get JetBrains Mono for tabular clarity. Retain Seekho's legacy habit of **colour-coding each program card** using the `--pkg-*` tokens, but cap it at four colours (gold / blue / green / pink) instead of five so the page reads intentional rather than chaotic. Every photo should be a warm, real Pakistani-face-in-Karachi moment — no stock — with the violet applied only through UI chrome and subtle overlays. The logo stays as-is (white wordmark with steering-wheel O) on the violet hero, but we ship a violet-on-cream variant for the press kit and about section.

---

## Appendix — Limitations

1. **Instagram + Facebook images not retrievable** via WebFetch (auth + JS-rendered). Chromium not installed locally; recommend running Playwright screenshots from a machine with Chrome available to verify social-media palette matches the site.
2. **Vehicle decal colours not confirmed** — no scraped vehicle photos; suggest Faryal provides.
3. **Logo file provenance** — `Group 33.png` is an anonymous Figma layer-name export; needs official confirmation it is the current mark.
4. **Google Fonts are the only web fonts declared** — no brand-font licence in evidence, so the Space Grotesk/Inter pairing is safe (both free, both SIL/OFL-licensed).
