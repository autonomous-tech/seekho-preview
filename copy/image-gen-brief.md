# Seekho — Image Generation Brief

**For:** image-gen agent (nano-banana-pro)
**Site:** seekhopakistan.com.pk
**Context:** Rebuild of Seekho driving school website, styled on safaikaro.pk design system.
**Deliverable:** All images listed below, generated at exact dimensions, saved under `/home/rizki/work/autonomous/scratch/seekho/images/` with the exact filenames given.

---

## Style North Star

**Reference:** match safaikaro.pk's photography style — realistic, professional, warm, natural-light, documentary-feel. NOT stock-photo glossy. NOT corporate sterile. NOT AI-obvious (avoid uncanny hands, plastic skin, symmetrical-staring-into-camera).

**Brand voice translation into imagery:**
- **Confident, empathetic, not condescending.** Nervous-driver-friendly. Show human moments — instructor laughing with student, student's hands on wheel mid-lesson, pickup/drop-off scene.
- **Women-forward but not exclusionary.** Majority of human images should feature women (students and instructors) reflecting Seekho's majority-female team, but include men so male learners still feel welcome.
- **Pakistani, specifically Karachi.** Subjects must look South Asian / Pakistani. Setting must read as Karachi — DHA/Clifton commercial streets, Karachi palm trees, sunlight quality, car brands common in Pakistan (Toyota Corolla, Suzuki Cultus, Honda City, Toyota Yaris). Not Dubai, not Delhi, not generic.
- **Modesty-respectful.** Dupatta / headscarf on some female subjects, not all. Mix of hijabi, non-hijabi, older/younger. Modest clothing (long sleeves, shalwar kameez for some, modern western wear for others). No cleavage, no crop tops.
- **Real cars.** Seekho trains on sedans and hatchbacks. Dual-brake-retrofit optional detail. Clean, well-maintained, not luxury, not beat-up.
- **Natural daylight preferred.** Golden hour for heroes. Overcast for instructional shots. Avoid harsh midday overhead sun and blown-out skies.
- **No text overlays in generated images.** Text is added in HTML/CSS. Image must have enough negative space on one side for headline overlay (typically left side for hero, where we'll place H1 over the photo in CSS).
- **Colour palette compatible with:** cream #F9F8F4 background, deep green #0D4A2F brand, lime #6EE086 accent. Photos should not clash — earthy tones, natural greens, warm skin tones, soft blue sky.

**Negative prompt baseline (apply to every prompt unless otherwise noted):**
> no text, no watermarks, no logos, no studio backdrop, no stock-photo composition, no over-smoothed skin, no AI artefacts on hands or teeth, no selfie pose, no cartoon style, no pastel backgrounds, no generic white woman, no Dubai skyline, no Western suburban street

---

## Dimension Reference

| Label | Dimensions | Use |
|-------|-----------|-----|
| Hero portrait | 800 × 1000 | Homepage and area-landing hero images (right side of hero block, portrait orientation) |
| Hero wide | 1600 × 900 | Wide hero variant (book page, programme page, traffic-club) |
| Page sidebar | 600 × 800 | Booking page sidebar, about page inset |
| Portrait headshot | 600 × 600 | Instructor profiles, founder portrait — square |
| OG image | 1200 × 630 | Social sharing / link previews — every route needs one |
| Contextual photo | 1200 × 800 | Blog-style / section photos — landscape |
| Icon concept | 512 × 512 | Favicon / apple-touch-icon source |

---

## Image Set 1 — Hero Images

### 1.1 Homepage hero
- **Filename:** `hero-homepage.jpg`
- **Dimensions:** 800 × 1000 (portrait)
- **Page(s):** `/index.html`
- **Alt text:** `Seekho female driving instructor guiding a young woman student behind the wheel on a quiet DHA Karachi commercial street, golden hour light`
- **Prompt:**
> Realistic documentary-style photograph, shot on 35mm lens, shallow depth of field. A young Pakistani woman in her mid-20s sits in the driver's seat of a white Toyota Corolla, hands on steering wheel, expression calm and focused with slight confident smile. In the passenger seat, a female Pakistani driving instructor in her 30s (dupatta draped loosely over shoulders, not head) is gesturing gently toward the windscreen, explaining something. Both subjects have warm natural Pakistani complexions. Setting: quiet DHA Karachi commercial side-street, palm trees in soft background bokeh, a couple of parked cars, golden hour late-afternoon light coming through windscreen. Car dashboard visible, modern but not luxury. Composition leaves negative space on the left third for headline overlay. Warm earthy colour grade. Natural skin, no glossy retouching.

### 1.2 DHA area page hero
- **Filename:** `hero-dha.jpg`
- **Dimensions:** 800 × 1000
- **Page(s):** `/driving-school-dha-karachi.html`
- **Alt text:** `Seekho driving lesson on a tree-lined DHA Phase 6 street, student driver and female instructor in the car`
- **Prompt:**
> Realistic photograph, natural afternoon light. View from front-right of a silver Honda City parked on a tree-lined DHA Phase 6 Karachi commercial street (Ittehad Commercial style — low-rise shops, palm trees, wide road). Through the windscreen we see a young Pakistani woman at the wheel with focused expression and a female instructor in the passenger seat smiling encouragingly. "L" learner sticker visible on back window. Empty street, no traffic, mid-day soft overcast light. DHA signage subtle in background. Composition: car occupies right 60%, left third empty sky/street for text overlay. Earthy, realistic, documentary, no over-saturation.

### 1.3 Clifton area page hero
- **Filename:** `hero-clifton.jpg`
- **Dimensions:** 800 × 1000
- **Page(s):** `/driving-school-clifton-karachi.html`
- **Alt text:** `Driving lesson on a Clifton Karachi street near Block 5, female student at the wheel, Seekho instructor coaching`
- **Prompt:**
> Realistic photograph, late-afternoon diffused light. A white Suzuki Swift hatchback on a quiet Clifton Block 5 Karachi street — low buildings, a few trees, sidewalk. Through the open driver-side window, we see a Pakistani woman in her late 20s in the driver's seat, both hands at 9-and-3 on the wheel, making a slight left turn with focused expression. A female instructor in the passenger seat gestures forward. Subtle sea-breeze atmosphere, soft blue-grey sky. Warm tones, natural contrast. Leave left third of frame clear for text overlay. Absolutely no text on signage or car.

### 1.4 Ladies landing page hero
- **Filename:** `hero-ladies.jpg`
- **Dimensions:** 800 × 1000
- **Page(s):** `/ladies-driving-school-karachi.html`
- **Alt text:** `Pakistani female driving instructor with hijab teaching a young woman student how to check mirrors before driving, both smiling, warm natural light`
- **Prompt:**
> Realistic warm documentary-style photograph. A young Pakistani woman in her early 20s sits in the driver's seat of a clean, modern automatic sedan (Toyota Yaris). She is adjusting the rearview mirror, looking attentive. Next to her in the passenger seat sits a female driving instructor in her 30s wearing a soft cream hijab and long-sleeve shirt, smiling gently and pointing at something on the dashboard. The instructor holds a small clipboard. Both women are at ease, laughing softly. Soft golden afternoon light through the windscreen. Interior of car spotless, dual-brake pedal subtly visible on passenger side. Background outside: quiet Karachi residential street. Warm skin tones, natural hair, no heavy makeup. Empty space on left side of frame for headline.

### 1.5 Automatic transmission page hero
- **Filename:** `hero-automatic.jpg`
- **Dimensions:** 800 × 1000
- **Page(s):** `/automatic-car-driving-lessons-karachi.html`
- **Alt text:** `Close-up of student's hand on automatic gear shifter, Seekho instructor pointing to the dashboard display`
- **Prompt:**
> Realistic close-up photograph, 50mm lens, shallow depth of field. From passenger-side angle, we see the interior of a modern automatic car. A young Pakistani woman's right hand rests on the automatic gear shifter (P-R-N-D visible), bracelet on wrist. Passenger-side hand (instructor) is gently pointing toward the dashboard display. Warm afternoon sunlight slants through the windscreen creating gentle lens flare. Clean modern interior, black leather seats. Everything in frame is in-focus enough to read "D" on the gear selector. No faces in frame — this is a tactile, detail-oriented image. Composition leaves some negative space top-left for text overlay.

### 1.6 Programme page hero
- **Filename:** `hero-programme.jpg`
- **Dimensions:** 1600 × 900 (wide)
- **Page(s):** `/programs/drivers-education.html`
- **Alt text:** `Seekho classroom theory session — small group of students reviewing a Karachi road-signs handbook with instructor at whiteboard`
- **Prompt:**
> Realistic photograph, slightly wide-angle. Small classroom setting — 5 Pakistani students (3 women, 2 men, ages 18–35, mix of hijabi and non-hijabi women, modest modern clothing) seated at light-wood tables looking forward. At the front of the room, a female Pakistani instructor in her 30s stands beside a whiteboard pointing at a road-sign diagram (stop sign, yield, speed limit — all Pakistani signage style, no text legible). Whiteboard has simple marker diagrams. Natural light coming through a window on the left. Warm cream walls, clean, professional but not sterile. Realistic, documentary style. Composition leaves space above and to right for overlay.

### 1.7 Traffic Club hero
- **Filename:** `hero-traffic-club.jpg`
- **Dimensions:** 1600 × 900 (wide)
- **Page(s):** `/traffic-club.html`
- **Alt text:** `Children learning road safety with traffic cones and miniature signs in a school playground, Seekho Traffic Club programme`
- **Prompt:**
> Realistic documentary photograph. A school playground in Karachi — mixed Pakistani children aged 8–12 in school uniforms (grey trousers/navy skirts, white shirts) standing around a miniature road layout made of traffic cones and chalk lines on the ground. A female Seekho instructor in casual khakis and brand-neutral green shirt (no logos visible) is demonstrating how to cross a crosswalk, pointing to a miniature stop sign. Two kids hold small red-and-white signs. Sunny morning light, palm trees visible in background, light blue sky. Joyful, active, educational atmosphere. Subjects natural, slightly candid. No text on signs.

### 1.8 Book page sidebar photo
- **Filename:** `book-sidebar-team.jpg`
- **Dimensions:** 600 × 800 (portrait)
- **Page(s):** `/book.html`
- **Alt text:** `Seekho instructor team — group of five female driving instructors standing beside a Seekho training car`
- **Prompt:**
> Realistic environmental group portrait. Five Pakistani female driving instructors, ages 28–45, standing in a relaxed line beside a clean white sedan parked at the curb. Mix of hijabi and non-hijabi, different heights and body types, all in neutral professional clothing — long-sleeve shirts, modest trousers or long kurta tops. Natural smiles, arms casually at sides or one with arm around shoulder. Warm late-afternoon light, slight golden tone. Setting: DHA Karachi commercial side street, palm trees in soft bokeh, cream-coloured building behind. Subjects are real-looking, not models, warm and approachable. Clothing has no logos. Realistic skin, no heavy retouching. Composition portrait orientation — subjects occupy bottom two-thirds, sky/building above.

---

## Image Set 2 — Instructor Portraits

All instructor portraits: 600 × 600 square, shot at eye level, soft natural light, plain warm-neutral background (cream wall or soft outdoor bokeh), shoulders-up framing, no logos on clothing, subject slightly smiling, looking at camera or slightly off-camera. Warm skin tones, no filter, documentary-style.

### 2.1 Omaima
- **Filename:** `instructor-omaima.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`, `/ladies-driving-school-karachi.html`, `/driving-school-dha-karachi.html`
- **Alt text:** `Omaima — senior Seekho driving instructor, warm smiling portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her early 30s. Shoulder-length dark brown hair loose or lightly tied back, warm olive-toned complexion, subtle natural makeup, small stud earrings. Wearing a soft sage-green long-sleeve shirt, modest. Warm natural daylight from camera-left, soft shadow on right cheek. Genuine warm smile, eyes to camera. Background: softly blurred cream wall with slight warm glow. No text, no logo on clothing. 50mm lens look, documentary portrait feel, not corporate headshot. No over-retouching — natural skin texture visible.

### 2.2 Farkhanda
- **Filename:** `instructor-farkhanda.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`, `/ladies-driving-school-karachi.html`
- **Alt text:** `Farkhanda — Seekho driving instructor, confident warm portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her late 30s wearing a soft taupe hijab wrapped modestly under chin, warm complexion, laugh lines around eyes. Wearing a simple charcoal shawl over long-sleeve top. Confident, approachable smile — eyes slightly crinkled. Natural afternoon daylight from window side. Background: softly out-of-focus interior, neutral warm tones. Documentary-style portrait, real and warm, not glamour-retouched. 50mm lens, shallow depth of field, subject eyes sharp.

### 2.3 Zainab
- **Filename:** `instructor-zainab.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`, `/ladies-driving-school-karachi.html`, `/driving-school-clifton-karachi.html`
- **Alt text:** `Zainab — Seekho driving instructor, youthful approachable portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her late 20s, dark hair pulled back in low ponytail, no hijab, warm golden-brown complexion, small gold hoop earrings. Wearing a cream-coloured button-down shirt, sleeves rolled to elbows (one elbow visible). Natural daylight from overhead slightly front-left. Relaxed, slight smile, looking at camera. Background: soft out-of-focus outdoor greenery (palm fronds). Candid documentary feel, not staged. 50mm portrait.

### 2.4 Tehreem
- **Filename:** `instructor-tehreem.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`, `/ladies-driving-school-karachi.html`
- **Alt text:** `Tehreem — Seekho driving instructor, smiling outdoor portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her early 30s wearing a soft plum-coloured chiffon dupatta draped loosely over shoulders (not covering head), dark hair loose around shoulders. Warm complexion. Light natural makeup. Wearing a muted olive kurta neckline visible. Genuine warm smile, teeth showing naturally. Standing outdoors in soft late-afternoon light, palm trees blurred behind. Looking slightly off-camera to the right. Documentary portrait feel.

### 2.5 Instructor portrait — placeholder A (TBD-faryal — swap with real instructor once confirmed)
- **Filename:** `instructor-placeholder-a.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`
- **Alt text:** `Seekho driving instructor — portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her mid-40s wearing a soft beige hijab. Warm complexion, slight smile lines, kind eyes. Wearing a deep teal long-sleeve top. Natural daylight. Background neutral cream. Warm, motherly presence, confident professional. Documentary portrait style. No logos.

### 2.6 Instructor portrait — placeholder B
- **Filename:** `instructor-placeholder-b.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`
- **Alt text:** `Seekho driving instructor — portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her late 20s, shoulder-length dark hair, no hijab, warm fair-medium complexion, wearing a simple rust-coloured shirt. Relaxed professional smile. Soft afternoon backlight. Background: out-of-focus warm beige interior. Documentary portrait feel, natural.

### 2.7 Instructor portrait — placeholder C (male instructor — for men-students' reassurance)
- **Filename:** `instructor-placeholder-c.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`
- **Alt text:** `Seekho male driving instructor — portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani man in his early 40s, short dark hair, warm complexion, neat trimmed short beard, wearing a soft sage-green collared shirt. Warm approachable smile, eyes to camera. Natural daylight. Background softly blurred neutral cream wall. Documentary portrait style, professional but warm.

### 2.8 Instructor portrait — placeholder D
- **Filename:** `instructor-placeholder-d.jpg`
- **Dimensions:** 600 × 600
- **Page(s):** `/about.html`
- **Alt text:** `Seekho driving instructor — portrait`
- **Prompt:**
> Realistic natural-light portrait of a Pakistani woman in her mid-30s wearing a soft navy-blue dupatta loosely on shoulders (not head), dark hair pulled back, warm complexion. Small silver earrings. Wearing a simple cream blouse. Calm, confident smile. Natural window light. Background out-of-focus interior. Real, not retouched.

---

## Image Set 3 — Founder Portrait

### 3.1 Faryal Farooqui founder portrait
- **Filename:** `founder-faryal.jpg`
- **Dimensions:** 600 × 600 (square)
- **Page(s):** `/about.html`, `/press.html`
- **Alt text:** `Faryal Farooqui — founder and CEO of Seekho Pakistan, portrait`
- **Prompt:**
> Realistic natural-light portrait of Faryal Farooqui-style figure — Pakistani woman in her late 30s to early 40s, shoulder-length dark hair with subtle natural waves, warm olive complexion, kind confident eyes, light natural makeup, small gold earrings. Wearing a well-tailored deep green (sage or forest) long-sleeve blazer or kurta over cream top. Subtle professional smile, eyes directly to camera. Natural soft light from large window on camera-left. Background: slightly blurred modern office setting — hints of books or a plant, warm wood tones. Confident, approachable, not corporate-stiff. Documentary style, 50mm, real skin texture, no heavy retouching. This is the founder of a female-led driving school — presence should read as competent, warm, trustworthy.

---

## Image Set 4 — Contextual / Section Photos

### 4.1 Student smiling in driver's seat
- **Filename:** `contextual-student-smile.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** Homepage testimonials section, `/ladies-driving-school-karachi.html`, `/about.html`
- **Alt text:** `Young Seekho student beaming in the driver's seat after completing her first lesson`
- **Prompt:**
> Realistic photograph, shot from passenger-side diagonal. A young Pakistani woman (early 20s) in the driver's seat of a clean Toyota Yaris, hands on the wheel, head turned slightly toward camera, grinning broadly with genuine excitement — "I just did it" energy. Car parked, key-light natural through windscreen. Seatbelt visible. Clean car interior. Background through side window: soft bokeh of DHA commercial street with palm trees. Natural warm tones. Documentary, no posed-model feel.

### 4.2 Instructor guiding student at wheel
- **Filename:** `contextual-instruction-moment.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** Homepage, `/programs/drivers-education.html`
- **Alt text:** `Seekho instructor explaining steering technique while student drives on a quiet Karachi street`
- **Prompt:**
> Realistic photograph from rear-passenger-seat angle looking forward between two front seats. Student (young Pakistani woman, hands on wheel) and instructor (female, cream hijab, clipboard) in front seats. Instructor is animated, gesturing forward with her left hand, explaining something. Student is focused forward. Through the windscreen: quiet tree-lined DHA street, soft overcast daylight. Interior of car well-lit. Real moment, candid, shows partnership between instructor and student. No faces to camera. Natural colour grade.

### 4.3 Parallel parking practice
- **Filename:** `contextual-parallel-parking.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** `/programs/drivers-education.html`, homepage, `/driving-school-dha-karachi.html`
- **Alt text:** `Parallel parking practice between two parked cars on a DHA Karachi commercial street, Seekho training car`
- **Prompt:**
> Realistic photograph shot from across-the-street angle. A white sedan (Seekho training car) is mid-manoeuvre parallel-parking between two other cars on a narrow DHA commercial side street (e.g. Bukhari Commercial style). Front wheels angled, car slightly into the spot. Warm afternoon light. Empty side of street, sidewalk with palm tree. Real Karachi context — shop shutters pulled down, cream-coloured building. Documentary feel, slightly candid, no posing. No text visible on shops. Car is clean but everyday, not luxury.

### 4.4 Highway / Shahrah-e-Faisal drive at night
- **Filename:** `contextual-night-drive.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** `/programs/drivers-education.html` (advanced skills section), blog placeholder
- **Alt text:** `Seekho training car on a Karachi main road at dusk, city lights and traffic beginning`
- **Prompt:**
> Realistic photograph from behind the driver (over the shoulder angle inside the car). Through the windscreen: a wide Karachi main road at early dusk / blue hour, warm orange streetlights beginning to turn on, a few cars ahead with red tail lights, light traffic. Dashboard glow visible, student's hands on wheel visible. Mood: calm, confident, learning advanced skills. Slight motion blur on passing headlights. Realistic, cinematic but not over-stylised. No text on signage.

### 4.5 Karachi street scene from driver's POV
- **Filename:** `contextual-street-pov.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** `/driving-school-dha-karachi.html`, homepage, blog
- **Alt text:** `Driver's point of view of a quiet DHA Karachi commercial street with palm trees and low buildings`
- **Prompt:**
> Realistic photograph from driver's first-person perspective — windshield frame visible at top and sides (dashboard at bottom of frame), road ahead. Setting: a quiet DHA Karachi commercial street (Jami or Ittehad style) — tree-lined, low-rise shops on both sides, palm trees, afternoon warm light, a couple of parked cars ahead, no heavy traffic. Peaceful, manageable traffic for a learner. Natural warm colour grade. No visible text on shops.

### 4.6 Completion certificate close-up
- **Filename:** `contextual-certificate.jpg`
- **Dimensions:** 1200 × 800
- **Page(s):** `/programs/drivers-education.html`, `/about.html`
- **Alt text:** `Close-up of a Seekho driver's education completion certificate being held by a graduating student`
- **Prompt:**
> Realistic close-up photograph, shallow depth of field. Hands of a young Pakistani woman holding a simple, elegant printed certificate (cream paper, gold trim, no readable text — leave text blurred/abstract). Her hands are in frame from wrists down, soft natural skin, simple bracelet on one wrist. Background softly blurred: a modern office/classroom with warm wood tones and a hint of a green plant. Warm natural light. The certificate is the focus. Symbolic, warm, aspirational. No legible text anywhere (will be added via CSS/HTML overlays if needed).

---

## Image Set 5 — OG (Open Graph) Images

**All OG images: 1200 × 630. Designed for social link previews (WhatsApp, Facebook, LinkedIn, X).**

**General OG style rules:**
- Photo-led, with a small Seekho wordmark in lime #6EE086 in a lower corner (simple sans-serif "Seekho" — will be added as CSS overlay in actual site, but include visual space for it in image composition).
- Warm natural photography, same as hero style.
- Landscape orientation, subject on right, negative space on left for title overlay.
- Cream #F9F8F4 or soft warm background if not photographic.
- No text baked into image (overlaid at render).

### 5.1 Homepage OG
- **Filename:** `og-homepage.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/` (Open Graph image for homepage social share)
- **Alt text:** `Seekho — Karachi driving school — female student and instructor in a training car`
- **Prompt:**
> Realistic photograph, 1200×630 landscape. Right two-thirds of frame: through the open passenger-side window we see a young Pakistani woman student at the wheel of a clean white Toyota Corolla, female instructor beside her (cream hijab) pointing at dashboard, both mid-conversation. Warm golden-hour DHA Karachi commercial street backdrop. Left third: softly blurred street/sky — empty for headline. Warm earthy palette compatible with cream + green brand.

### 5.2 Packages OG
- **Filename:** `og-packages.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/packages.html`
- **Alt text:** `Seekho packages and transparent driving school pricing Karachi`
- **Prompt:**
> Realistic photograph. Right half: a modern car dashboard with keys in the ignition, a folded simple price sheet (text not legible) resting on the dashboard, a pen beside it. Composition feels "making a confident decision." Soft warm daylight. Left half: softly blurred interior of car, empty for overlay text. No text visible on paper.

### 5.3 Book OG
- **Filename:** `og-book.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/book.html`
- **Alt text:** `Book your first Seekho driving lesson — mobile phone with WhatsApp chat visible`
- **Prompt:**
> Realistic photograph. Right half: a Pakistani woman's hand holding a smartphone, WhatsApp-like green chat interface visible but text illegible. Phone is tilted at natural angle. Warm daylight. Left half: soft cream-coloured wooden table surface, empty space for headline. Documentary style. No legible text on screen.

### 5.4 About OG
- **Filename:** `og-about.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/about.html`
- **Alt text:** `About Seekho — founder Faryal Farooqui and the instructor team`
- **Prompt:**
> Realistic environmental group photograph. Four to five Pakistani women (mix of hijabi and non-hijabi, ages 28–45, modest professional clothing) standing casually in a relaxed pose beside a clean white sedan, warm golden late-afternoon light, DHA commercial street backdrop with palm trees. Subjects occupy right 60% of frame. Left third: negative space with soft street bokeh. Natural, confident, documentary feel.

### 5.5 FAQ OG
- **Filename:** `og-faq.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/faq.html`
- **Alt text:** `Frequently asked questions about Seekho driving school Karachi`
- **Prompt:**
> Realistic photograph. Right half: a smiling young Pakistani woman in a car driver's seat, turning toward camera as if asking a question, hands relaxed on wheel. Through passenger-side open window natural light. Left half: soft out-of-focus street, negative space. Warm, approachable, documentary feel. Natural colour.

### 5.6 Programme OG
- **Filename:** `og-program.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/programs/drivers-education.html`
- **Alt text:** `Seekho driver's education programme — theory classroom and behind-the-wheel`
- **Prompt:**
> Realistic photograph, split composition. Right half: a simple whiteboard with abstract road-sign sketches (not legible), a hand with a marker pointing. Left half: through a window view of a car outside. Symbolism: theory + practical. Warm natural light, cream walls, clean, educational feel. No legible text.

### 5.7 Ladies OG
- **Filename:** `og-ladies.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/ladies-driving-school-karachi.html`
- **Alt text:** `Ladies driving school Karachi — female instructor teaching female student`
- **Prompt:**
> Realistic photograph. Right two-thirds: two Pakistani women in a car — instructor (soft cream hijab, warm smile) in passenger seat gesturing toward student (young woman, hands on wheel, focused). Warm daylight. Left third: soft out-of-focus DHA street, empty for headline overlay. Warm, empathetic, documentary feel. Both women natural and at ease.

### 5.8 DHA OG
- **Filename:** `og-dha.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/driving-school-dha-karachi.html`
- **Alt text:** `Seekho driving school DHA Karachi — training car on tree-lined phase 6 commercial street`
- **Prompt:**
> Realistic landscape photograph. Right two-thirds: a clean white sedan with "L" sticker on a tree-lined DHA Phase 6 Karachi street. Palm trees, low-rise cream buildings, soft afternoon light. Left third: empty street/sky for text overlay. Warm, documentary feel. No readable signage.

### 5.9 Clifton OG
- **Filename:** `og-clifton.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/driving-school-clifton-karachi.html`
- **Alt text:** `Seekho driving school Clifton Karachi — training car on Clifton Block 5 street`
- **Prompt:**
> Realistic landscape photograph. Right two-thirds: a white Suzuki Swift hatchback with Seekho training indicator on a Clifton Block 5 Karachi street, soft late-afternoon light, hint of sea-breeze feel, low-rise buildings, a few pedestrians blurred in distance. Left third: empty sky for overlay. Warm natural tones.

### 5.10 Automatic OG
- **Filename:** `og-automatic.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/automatic-car-driving-lessons-karachi.html`
- **Alt text:** `Automatic car driving lessons Karachi — close-up of automatic gear shifter`
- **Prompt:**
> Realistic photograph, close-up interior. Right half: close-up of a clean modern automatic gear shifter (P-R-N-D visible but abstract), a woman's hand resting near it with a bracelet. Warm sunlight through windscreen. Left half: softly blurred car interior, empty for headline. Documentary, tactile.

### 5.11 Traffic Club OG
- **Filename:** `og-traffic-club.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/traffic-club.html`
- **Alt text:** `Seekho Traffic Club — children learning road safety in Karachi school playground`
- **Prompt:**
> Realistic landscape photograph. Right two-thirds: group of Pakistani schoolchildren (ages 8–12, school uniforms) around miniature traffic cones and signs in a school playground, a female Seekho instructor gesturing. Warm morning sunshine, palm trees. Left third: empty sky for overlay. Joyful, educational, real.

### 5.12 Careers OG
- **Filename:** `og-careers.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/careers.html`
- **Alt text:** `Careers at Seekho — join Karachi's leading female driving instructor team`
- **Prompt:**
> Realistic environmental portrait. Right two-thirds: a female driving instructor in her 30s (warm smile, soft hijab, sage-green shirt) leaning confidently against a Seekho training car, holding keys. Warm daylight, DHA street backdrop. Left third: empty sky for overlay. Documentary, aspirational-but-real.

### 5.13 Press OG
- **Filename:** `og-press.jpg`
- **Dimensions:** 1200 × 630
- **Page(s):** `/press.html`
- **Alt text:** `Seekho press and media coverage — founder Faryal Farooqui`
- **Prompt:**
> Realistic environmental portrait. Right two-thirds: Faryal-style founder portrait (Pakistani woman, late 30s, confident, warm green blazer, standing beside a clean Seekho car on a DHA street). Left third: empty for headline. Warm natural afternoon light. Documentary-editorial feel, suitable for press/media preview.

---

## Image Set 6 — Favicon / App Icons

### 6.1 Brand mark — Seekho "S"
- **Filename:** `icon-source-512.png`
- **Dimensions:** 512 × 512 (source)
- **Derivatives (generate from this source at final rendering):** `favicon.ico` (16/32/48), `apple-touch-icon.png` (180×180), `icon-192.png` (192×192), `icon-512.png` (512×512 for PWA manifest)
- **Page(s):** site-wide (linked in <head>)
- **Alt text:** N/A (icon)
- **Prompt:**
> Clean flat vector-style graphic, 512×512, solid safaikaro-brand deep green background (#0D4A2F). Centered: a bold geometric sans-serif uppercase "S" letterform in lime green #6EE086, slight rounded terminals, confident weight (like a geometric grotesque similar to Sora Bold). The "S" occupies roughly 60% of the canvas, perfectly centered, optical adjustments applied. Simple, modern, works at 16px favicon size. No gradients, no drop shadow, no texture, no 3D. Pure 2-colour flat. The letterform should feel slightly playful — the curves of the S are energetic, not stiff — matching safaikaro's playful-geometric brand treatment. Output: flat PNG, transparent not required (solid green background).

---

## Delivery Checklist

When image-gen agent completes, deliver to `/home/rizki/work/autonomous/scratch/seekho/images/`:

**Heroes (8):**
- [ ] hero-homepage.jpg (800×1000)
- [ ] hero-dha.jpg (800×1000)
- [ ] hero-clifton.jpg (800×1000)
- [ ] hero-ladies.jpg (800×1000)
- [ ] hero-automatic.jpg (800×1000)
- [ ] hero-programme.jpg (1600×900)
- [ ] hero-traffic-club.jpg (1600×900)
- [ ] book-sidebar-team.jpg (600×800)

**Instructor portraits (8):**
- [ ] instructor-omaima.jpg
- [ ] instructor-farkhanda.jpg
- [ ] instructor-zainab.jpg
- [ ] instructor-tehreem.jpg
- [ ] instructor-placeholder-a.jpg
- [ ] instructor-placeholder-b.jpg
- [ ] instructor-placeholder-c.jpg
- [ ] instructor-placeholder-d.jpg

**Founder (1):**
- [ ] founder-faryal.jpg

**Contextual (6):**
- [ ] contextual-student-smile.jpg
- [ ] contextual-instruction-moment.jpg
- [ ] contextual-parallel-parking.jpg
- [ ] contextual-night-drive.jpg
- [ ] contextual-street-pov.jpg
- [ ] contextual-certificate.jpg

**OG images (13):**
- [ ] og-homepage.jpg
- [ ] og-packages.jpg
- [ ] og-book.jpg
- [ ] og-about.jpg
- [ ] og-faq.jpg
- [ ] og-program.jpg
- [ ] og-ladies.jpg
- [ ] og-dha.jpg
- [ ] og-clifton.jpg
- [ ] og-automatic.jpg
- [ ] og-traffic-club.jpg
- [ ] og-careers.jpg
- [ ] og-press.jpg

**Icons (1 source + 4 derivatives):**
- [ ] icon-source-512.png
- [ ] favicon.ico
- [ ] apple-touch-icon.png (180×180)
- [ ] icon-192.png
- [ ] icon-512.png

**Total: 37 unique assets.**

---

## Notes for the Image-gen Agent

1. **Consistency pass after generation.** Batch-review all hero and instructor images together to make sure colour grading, warmth, and style match. One outlier breaks the set.
2. **Hand-check.** Hands are AI's weak point. Review every image for malformed hands/fingers. Regenerate if obvious artefacts.
3. **Face realism.** Pakistani features — not generic South Asian, not Indian. Reference: warm olive to fair-medium complexion, expressive eyes, varied face shapes. Avoid uncanny-valley symmetry.
4. **No logos, no text anywhere in generated photos.** All text is added via CSS/HTML.
5. **Alt text is shipping text.** Keep alt-text copy as provided — it's tuned for accessibility and SEO, not internal notes.
6. **When in doubt, match safaikaro's homepage photography.** The visual target is to feel like the same production studio shot both brands.
