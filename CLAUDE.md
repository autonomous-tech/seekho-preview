# Seekho Pakistan — Driving School Redesign

**Project:** Full replacement of https://seekhopakistan.com.pk/ — Faryal Farooqui's award-winning driving academy in DHA Karachi (founded 2019, 1,000+ students trained).

**Status:** Live preview on GitHub Pages. Content, imagery, pricing are placeholders pending Faryal's sign-off — see "Open to Faryal" at the bottom.

## URLs

| Purpose | URL |
|---|---|
| GitHub repo | https://github.com/autonomous-tech/seekho-preview |
| GH Pages preview | https://autonomous-tech.github.io/seekho-preview/ |
| Production target | https://seekhopakistan.com.pk/ (DNS flip when Faryal approves) |
| Founder / owner | Faryal Farooqui — Founder/CEO Seekho |

## Stack

Pure static HTML. No framework, no build step. Open any `.html` file in a browser and it works.

- **CSS** — single `styles.css` with CSS custom properties (brand tokens at `:root`). Structure adopted from [safaikaro.pk's](https://safaikaro.pk/) design system; palette swapped to Seekho's real brand (violet `#4E0CB9` + gold `#FFC93C`).
- **JS** — vanilla. Three scripts:
  - `prices.js` — centralised pricing, `[data-price="..."]` attribute binding. Single source of truth for every price displayed on the site.
  - `analytics.js` — PostHog init + delegated event capture on `[data-ph-event]`, scroll depth, form start/submit, WhatsApp/call/email clicks.
  - Per-page inline `<script>` blocks for nav hamburger, FAQ accordion, booking-form step controller.
- **Fonts** — Space Grotesk (display) + Inter (body) + JetBrains Mono (prices), via Google Fonts.

## Information architecture (20 pages)

| Path | What it is |
|---|---|
| `/` | Homepage — hero + trust bar + 3-package grid + testimonials + FAQ + instructor grid |
| `/packages.html` | Pricing matrix (highest-leverage conversion page — transparent prices) |
| `/book.html` | 3-step booking form + WhatsApp primary path |
| `/about.html` | Founder story + instructor team + press mentions |
| `/faq.html` | 27-question accordion across 4 categories |
| `/programs/drivers-education.html` | Curriculum deep-dive (theory + BTW) |
| `/ladies-driving-school-karachi.html` | Top-priority SEO page (near-uncontested positioning) |
| `/driving-school-dha-karachi.html` | Area landing — 8 DHA phases |
| `/driving-school-clifton-karachi.html` | Area landing — 9 Clifton blocks |
| `/automatic-car-driving-lessons-karachi.html` | Audience landing — auto-transmission focus |
| `/traffic-club.html` | Faryal's kids' road-safety programme |
| `/careers.html` | Instructor + support-staff hiring |
| `/press.html` | 3 real articles (Aurora/Dawn, Biz Today, The Nation) + Commissioner inauguration |
| `/guides/` | Hub for 6 SEO articles (below) |
| `/guides/how-to-get-driving-license-karachi.html` | DLS Sindh process |
| `/guides/karachi-driving-test-what-to-expect.html` | Test prep |
| `/guides/parallel-parking-karachi-guide.html` | HowTo (schema-marked) |
| `/guides/dashboard-warning-lights-explained.html` | Reference article |
| `/guides/pakistan-road-signs-complete-guide.html` | Reference article |
| `/guides/pakistan-driving-fines-nhso-2000.html` | NHSO 2000 fine schedule |

All schema-marked: `LocalBusiness`/`AutoSchool`/`DrivingSchool` (shared `@id: https://seekhopakistan.com.pk/#business`), `Service`+`Offer` with `_priceKey` (updated by `prices.js`), `FAQPage`, `BreadcrumbList`, `Article`/`HowTo` on guides, `Review`+`AggregateRating` on homepage.

## Brand facts (locked)

- **Primary** `--violet: #4E0CB9` — nav, hero, section-break anchors. Extracted from the live site's `body { background }`.
- **Accent** `--gold: #FFC93C` — prices, headline numbers, warm highlights. Warm-up of legacy `#FFE51F`.
- **Ink** `--ink: #1B0E3A` — violet-biased near-black for body type.
- **Cream** `--cream: #FBF8F3` — warm surface. Not pure white.
- **Fonts** — Space Grotesk 500/600/700 (display), Inter 400/500/600/700 (body), JetBrains Mono 500 (prices).
- **Logo** — `images/seekho-logo-original.png` (the white "steering-wheel-O" wordmark on violet). Was pulled from the live site. Needs vector retrace eventually.
- **Full spec** — see `brand-identity.md`.

## Running locally

```bash
cd /home/rizki/work/autonomous/scratch/seekho
python3 -m http.server 8088
# open http://localhost:8088/
```

Everything is static. No install step.

## Deploy

Pushed via `git` to `autonomous-tech/seekho-preview`. GH Pages serves from `main` at `/ (root)`.

- First deploy: `git push` + enable Pages in the GH UI (Settings → Pages → Source: Deploy from branch, Branch: main, Path: /).
- Subsequent updates: `git commit && git push` — GH rebuilds in 1–3 min.
- CNAME is **not** in the repo during preview so the default `*.github.io` URL works. Restore the CNAME (with `seekhopakistan.com.pk` one-liner) before DNS flip.

## Source-of-truth docs in this repo

| File | Purpose |
|---|---|
| `brand-identity.md` | Full extracted palette + fonts + logo notes. Never override these without re-auditing the live site. |
| `strategy.md` | Positioning, ICP (women 18–35 DHA/Clifton primary), tone, conversion goal hierarchy. |
| `audit-report.md` | Audit of the legacy site: 82 verbatim testimonials, instructor popularity rankings, FAQ policies, hidden 4th package, press references. |
| `competitive-research.md` | 8 competitors analysed, 46-keyword opportunity map, content gaps we can own. |
| `copy/shared-brand-facts.md` | Canonical brand voice rules, banned words, signature phrases, contact info. |
| `copy/image-gen-brief.md` | Image prompt manifest used by the nano-banana-pro agent. |
| `smoke-test-report.md` | Smoke test results from the last build. |

## Building or modifying content

When editing copy, **respect the voice rules in `copy/shared-brand-facts.md`**:
- Bilingual Urdu/English code-mix (`Karachi ka pehla driving school jahan price pehle dikhti hai`).
- First-person, warm, confidence-forward.
- No banned words (see list in shared-brand-facts).
- Every price via `[data-price="<key>"]` (keys in `prices.js`). Don't hard-code prices.

When adding a new page:
- Copy an existing sibling page's nav + footer + sticky mobile bar.
- Schema: `LocalBusiness` block with shared `@id` (copy from homepage) + page-specific schema.
- Include the `Guides` link in the top nav (between FAQ and Contact/Book).
- Update `sitemap.xml` and `llms.txt` with the new URL.
- PostHog events on every CTA via `data-ph-event="..."`.

When swapping in real photos from Faryal:
- Overwrite the existing JPGs in `images/` — filenames are stable (`hero-homepage.jpg`, `instructor-omaima.jpg`, etc.). HTML `<img src>` attrs don't need changes.
- Alt text review — strip `TBD-faryal-real-photo` prefixes once photos are final.

## Open to Faryal (things we don't know, marked `TBD-faryal-*` in the code)

1. **Package prices** — currently estimates (Rs 15,000 / 22,000 / 35,000 for manual; +Rs 3,000 for auto). Verified add-ons from her live FAQ (Rs 1,800 extra manual, Rs 2,000 extra auto) are accurate.
2. **Google Business rating + review count** — currently using `4.9★ / 82 reviews` (82 matches verbatim count from audit). Real live GBP number should replace this.
3. **Award years** — currently 2022, 2023, 2024 (plausible, TBD-verify).
4. **Full instructor roster** — Omaima, Farkhanda, Zainab, Tehreem, Muzaffar are confirmed from testimonials. Other team members TBD.
5. **PostHog project key** — currently `TBD-posthog-key` placeholder. Provision or reuse the agency shared key.
6. **Hidden 4th "Economy Saver" package** — HTML-commented in the legacy site. Ask if we should revive it.
7. **Photos** — every photo in `images/` is nano-banana-generated. Real photography (Aurora 2019 has professional shots — ask Faryal for the files) should overwrite these before production DNS flip.
8. **Vehicle fleet** — copy references Suzuki Swift (manual) + Toyota/Suzuki Alto (automatic). Verify current fleet with Faryal.
9. **Traffic Club** programme details (age brackets, session format, partner schools) — lightly stubbed; Faryal should expand.
10. **CNAME + DNS** — not configured yet. Flip when Faryal confirms.

## House notes

- This is a **client preview** — do not share the URL publicly until Faryal has reviewed + approved.
- All imagery is AI-placeholder pending real photos from Faryal. If the user laughs at steering-wheel-on-door issues, regenerate with **exterior framing** prompts to avoid nano-banana's LHD training bias (Pakistan is right-hand drive).
- `image-gen-batch/` is `.gitignore`d — it's the intermediate raw PNGs from nano-banana before JPG compression. Don't commit it.
