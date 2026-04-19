# Seekho Pakistan — Current Website Audit

**Site audited:** https://seekhopakistan.com.pk/
**Audit date:** 2026-04-19
**Owner:** Faryal Farooqui (Founder & CEO)
**Business:** Seekho (Pvt.) Ltd. — driving academy, founded Sep 2019, Karachi
**Method:** WebFetch on homepage + section anchors, raw HTML pull for SEO/schema analysis, external press & directory cross-reference.

---

## 1. Executive Summary

- **The site is a single-page HTML file (~152 KB) masquerading as a multi-page site.** Every "page" in the nav (About, Careers, FAQ, Press, Contact, etc.) is actually a modal/anchor on `/`. The sub-URLs we were told to crawl (`/drivers-education-program/`, `/about-us/`, `/faq/`, etc.) all return **404**. This means the site is effectively invisible to Google for any query other than "Seekho" — there is no per-topic ranking possible.
- **SEO is catastrophic.** `<title>` is just `Seekho`. No meta description. No H1. No canonical. No Open Graph. No Twitter card. No LocalBusiness / Review / FAQ schema. No `sitemap.xml` (404). No `robots.txt` (404). 148 images on the page with half having empty or junk alt text ("seekho-office-image" repeated 8 times, "certificate-image" repeated 8 times).
- **No prices, no online booking, no instant signal of cost.** The three packages show names + one sentence each and then say *"contact 03202-SEEKHO"*. Only pricing disclosed anywhere is buried in the FAQ: extra BTW lesson Rs 1,800 (manual) / Rs 2,000 (auto), and three discount lines ("Rs 2,000 off if you bring your own auto vehicle", etc.). Massive conversion killer for a category where price is the #1 question.
- **The testimonials are the single biggest asset on the site: 82 genuine student reviews extracted verbatim, most naming specific instructors (Omaima, Zainab, Farkhanda, Tehreem, Muzaffar).** They read authentically, address the exact emotional drivers (road anxiety, fear, confidence). These are gold for the rewrite.
- **"Press" page is a broken promise.** Nav says "Press" — the section contains 46 unlabelled images (office photos, certificates, partner group shots) with zero article titles, dates, or links. Real press coverage exists (Aurora/Dawn 2019, Biz Today, The Nation) but the site never references it. Huge credibility leak.
- **Conversion path is WhatsApp/phone only.** Primary CTA is "Call or text 0320-2733546". No form, no online booking, no calendar picker, no pricing page, no lead capture. Every prospect has to make a cold phone call to discover price.

---

## 2. Content Inventory — Per "Page" (all live on `/` as anchor sections)

The homepage HTML is one file. Nav links open modal-style sections triggered by JS (the anchors are `#one` through `#six`, `#top`). No real URLs exist for any section; a share of "the FAQ page" is impossible.

### 2.1 Home / Hero (#top)
- **URL:** https://seekhopakistan.com.pk/
- **`<title>`:** `Seekho`
- **Meta description:** *(none)*
- **H1:** *(none — page has zero H1 tags)*
- **Hero H2:** "SEEKHO is a unique Driver's Education Program"
- **Tagline/intro copy (verbatim):**
  > "Seekho is an award-winning Driver's Education Program in Karachi comprising of professional instructors and a dynamic team that has trained over 1000+ students since 2019. At Seekho, we offer a wide variety of driver's education products tailored to your expertise and comfort level. Whether you are training to become a new driver or looking to further improve your existing skills, Our mission is to nurture confidence, courtesy and responsibility in drivers for Our Country. We provide one-on-one training in custom-designed vehicles, along with an interactive theoretical curriculum in contemporary classrooms…"
- **"Why Choose Us" (12 feature tiles, H3):** Interactive (curriculum) / Behind (the wheel) / Professional (team) / Flexible (scheduling) / Pick-up (& drop-off Defence & Clifton) / Written (tests & tips) / Student-centric (approach) / Completion (certificate) / Freebies (stickers, mechanic discounts) / Fast (and convenient) / For Everyone (18+) / Gift (vouchers)
- **Our Fleet section:** "Air-conditioned, dual-brake systems, insured and regularly inspected, clean and sanitized, dashcam surveillance, manual Swift 2016 & 2017, automatic Alto 2021, first-aid kits, masks and sanitizers."
- **CTAs:** "Call or text 0320-2733546" (primary, repeated)
- **Images/videos:** Static banner images only, no hero video. Logo `assets/images/header-images/Group 33.png`. One `<iframe>` on page (likely Google Maps or YT embed — not confirmed to render content).

### 2.2 Driver's Education Program (modal #one)
- **Section title:** "SEEKHO DRIVER'S EDUCATION PROGRAM"
- **H2:** "driver's education program" / "how does it work?"
- **Body (verbatim):**
  > "If you are a new driver then we will start with the basics in a quiet area close to where you live and gradually build your skills from full talk through to prompted to being independent at all the skills needed to become a confident, safe and responsible driver. If you have some driving experience, we will give you a driving assessment to see what level your driving skills are at so a plan can be made to get you to your goals. At Seekho, we follow a course outline keeping local and international rules of the road with a student-centric learning process in mind. Learning to drive is a two-way process hence the trainers will listen to what you would like to learn as well as offer advice on what needs to be learn."
- **CTAs:** None visible inside modal.

### 2.3 Theoretical Lessons (modal #two)
- **Section title:** "SEEKHO THEORETICAL LESSONS"
- **H3 a — Introduction to Driver's Education (60 min):**
  > "As part of the course, all students at Seekho are provided an introductory session (60 minutes; online/on-site) entailing vehicle anatomy, dashboard signs, engine checks thoroughly explained before they sit behind-the wheel, introduced to the program schedule and road safety and road anxiety tips"
- **H3 b — Basic Tool Management, Vehicle maintenance and Road Safety workshop (120 min):**
  > "Towards the end of the course, every student attends a group workshop (120 minutes) focusing on life skills such as changing a flat tyre demo, jump-starting a vehicle demo, vehicle maintenance guide, under the hood components, road safety signs, distracted and defensive driving and fire and safety information. The session concludes with a theory test, worksheets, completion certificate and giveaways. Also includes occasional guest speaker sessions. (Every Saturday 11:30am - 1:30pm)"

### 2.4 About Us (modal #three)
- **H2:** "About Us"
- **Body (verbatim):**
  > "SEEKHO goes above and beyond expectations to provide a safe learning experience and to shape a safer country for everyone. As a driver, you are not only taking the safety of your passengers into your hands, but you are also responsible for the safety of pedestrians who share our roads. This is why it is very important for driver's to know and adhere to traffic rules. We believe in teaching not just the basics of driving, but also providing the knowledge to handle specific emergency situations should the need arise. It's a comprehensive training program which develops an important life skill and prepares you to be ready to take the road anywhere and everywhere in the world!"
- **Founder card:** "FARYAL FAROOQUI — Founder & CEO"
- **Note:** No founder bio, no founding year on this section (year 2019 appears elsewhere in hero), no photo alt text.

### 2.5 Careers (modal #four)
- **H2:** "CAREERS"
- **Body:** "Do you want to join our team and play your role in our social welfare initiative?"
- **Roles listed (H3):** Program Coordinator / Driving Training Officer / Road Safety Speaker / Internship
- **Apply:** "Please share your CVs on info@seekhopakistan.com.pk"
- **Images (alt text):** `Accountant.JPG`, `Driving Training Officer.jpg`, `Road Safety Trainer.JPG`, `Internship Program.JPG` — 4 role photos.

### 2.6 Traffic Club (modal)
- **H2:** "TRAFFIC CLUB"
- **Body (verbatim):**
  > "Seekho Traffic Club (STC) is an initiative by Seekho to create awareness regarding road safety amongst children. Inspiring young minds to learn all about road safety is key to preventing accidents later on in life and helping them make better choices. Road safety is something that needs to be done continuously and even subtly at times. STC provides an educational but entertaining way to prepare little ones to be safer and to develop road and traffic awareness."
- **CTA:** "download your file" → `Seekho Leaflet1.jpg`
- **No age range, no school list, no photos of events, no testimonials from parents/schools in copy.** (Some traffic-club photos appear in the Press slideshow with no captions.)

### 2.7 Press (modal)
- **H2:** "press"
- **Body:** *None.* Just a 46-image slideshow (labelled 1/46, 2/46 …) with no captions, no links, no dates. Image alt text groups: `seekho-office-image` (×8), `certificate-image` (×8), `children-road-safety-images` (×7), "collaboration" (×7), `learner-license` (×8), `employee-performance-award` (×8).

### 2.8 Students Voice (modal)
- **H2:** "STUDENTS VOICE"
- **82 testimonials** — see Section 3.

### 2.9 FAQ (modal)
- **H2:** "FAQ"
- **Not a real Q&A format** — it's a bulleted list of ~13 policy statements. See Section 8.

### 2.10 Downloads (modal)
- **H2:** "downloads"
- **19 downloadable resources listed** — see Section 10.

### 2.11 Our Partners (modal)
- Partner logos only, no body copy, no descriptions/quotes. See Section 7.

### 2.12 Contact Us (modal)
- **H2:** "contact us"
- Address + phones + emails + bank details + socials. See Section 10.

---

## 3. All Testimonials (Students Voice) — 82 Reviews Verbatim

These are organized in the order they appear on the site. Instructor name is noted in brackets when mentioned by the student. Package is never disclosed in any testimonial (no one says "I took Teach Me Everything").

| # | Name | Instructor mentioned | Review (verbatim) |
|---|---|---|---|
| 1 | Ania Khan | Fari & Zainab | "Just wanted to say, this was a great driving school. I had two teachers Fari and Miss Zainab, both of whom were very patient, calm and helped in boosting my confidence. Would recommended to others!" |
| 2 | Aksah | Zainab | "Thank you so much, had an amazing experience with seekho. Miss Zainab is such a patient and excellent instructor, loved her personality and driving techniques." |
| 3 | Bushra.P | — | "Had a great experience and now really enjoying taking to the streets of Karachi!" |
| 4 | Kim | — | "Lovely experience! Thank you for making me feel confident." |
| 5 | Samina | Tehreem | "Very nice experience. Tehreem is really very good tutor. I am really happy. Thanks Tehreem!" |
| 6 | M. Qureshi | Mian saab | "Absolutely loved it! Mian saab was EPIC!! Many regards and best wishes." |
| 7 | Sara | — | "Had a great time learning with Seekho!" |
| 8 | Shazmeneh | Omaima | "Loved my experience. My instructor, Omaima, really helped me overcome my fears! The whole experience was amazing. Thanks!" |
| 9 | Nawal | Omaima | "Had an amazing experience with Seekho! Omaima made driving very easy and really helped me gain confidence. Thank you!" |
| 10 | Sarah | Omaima | "Omaima is awesome. She is patient and an amazing driver. Also young and hip so it is fun learning from her. Thank you Seekho! (P.S I loved learning how to jumpstart a car and how to change a tyre)" |
| 11 | Noor-ul-Ain | Tehreem & Farkhanda | "Had a great experience of learning with Tehreem and Farkhanda. Thanks and regards" |
| 12 | Alina | Farkhanda | "It was amazing with Farkhanda. I learned a lot with her." |
| 13 | Anum Bilal | — | "I could not do it without you guys. You have given girls like me a great opportunity to learn and be confident enough to drive independently. You guys will go to places!" |
| 14 | Fatimah | Tehreem | "I had a great time learning with Miss Tehreem. Got over all my fears. Thank you!" |
| 15 | Javeria | Farkhanda | "I actually loved the entire experience. My instructor Farkhanda was amazing. She was a really cool and fun person to learn from. I am glad I chose Seekho to learn my driving from. I was able to overcome my road/driving fear!" |
| 16 | Zain | Muzzafar | "Absolutely life-changing experience. Had a wonderful time with Mr.Muzzafar. Overall, an absolutely great experience." |
| 17 | Alyan | Muzzafar | "Had a wonderful experience with Mr. Muzzafar. Learned a lot and have gained the confidence to drive every day." |
| 18 | Bakhtawar | Farkhanda | "I made the best choice choosing Seekho. I am super confident on the roads now, and had an amazing time learning with Farkhanda" |
| 19 | Ayra.K | Zainab | "Had an amazing experience with Zainab. She made me feel very confident during the sessions and my road anxiety is almost nonexistent now. Thank you so much for everything." |
| 20 | Sijyl | — | "I had a great time learning with Seekho it was an amazing experience and would differently recommend it to my friends who would like to learn!" |
| 21 | Anam | Farkhanda | "Had an amazing experience, Seekho and Farkhanda made driving so easy and fun. I can now finally say I know how to drive!! Thank you so much!" |
| 22 | Sana J | Omaima | "Had an amazing 11 sessions with Omaima. No more anxiety" |
| 23 | Emaad | — | "A very enlightening experience that gave me the skills and confidence to drive" |
| 24 | Momina Ahmad | — | "Never thought I could drive with Seekho I found confidence and motivation to drive because driving is a necessity everyone must learn and Seekho is the place to be" |
| 25 | Nadia Siddique | — | "I never thought I would do it! But they gave me hope thank you Seekho!" |
| 26 | Aksah Motiwala | — | "Had an amazing experience with Seekho got to learn so much early appreciate the time and effort they put into me" |
| 27 | Rabia S | — | "Had a wonder full hands on experience with Seekho! I gained a lot of confidence on the road and thoroughly enjoyed driving with Seekho" |
| 28 | Zunaira S | — | "I was so scared of driving before my experience at Seekho I am so glad I chose Seekho. Had an incredible experience" |
| 29 | Hiba Farooqi | — | "Never knew that I would gain confidence while driving and learn it so quickly! Amazing driving experience at Seekho really enjoyed driving! No more road anxiety" |
| 30 | Mk | — | "Loved every minute hope to drive like a pro soon" |
| 31 | Daniyal | Muzaffar | "A very good experience with my instructor as Sir Muzaffar taught me well, thank you Seekho!" |
| 32 | Nida | — | "The best learning experience! The best professional trainers! Very amazing & inspirational" |
| 33 | Yasi | — | "Loved learning with Seekho was an amazing experience!" |
| 34 | Abeeha | — | "Had a great learning experience! Never thought could learn how to drive! Thank you" |
| 35 | Alyzeh | Tehreem | "Tehreem was best! love it at Seekho" |
| 36 | Mahaa | — | "Loved learning at Seekho learning to desire was a personal goal and I am glad I was alive to live it Seekho" |
| 37 | Sascha | — | "Driving at Seekho helped me overcome my fears on the road!" |
| 38 | Tajwer Tather | — | "I had an amazing experience with Seekho and my trainer overcome all my fears with road would definite recommend others. Thank you Seekho!!!" |
| 39 | Abdul Rahman | — | "Seekho was a good informative experience. I appreciated how convenient and easy it was to register and arrange for classes." |
| 40 | Hiba | — | "Amazing Experience! I can finally drive stress free and enjoy it!" |
| 41 | Mahnoor S | — | "Loved my experience at Seekho, helped me overcome my car anxiety and I am confident now! My trainer was also amazing. Thank you Team Seekho!" |
| 42 | Rabail | Omaima | "Experience at Seekho was amazing! Omaima is the best at her job. Seekho has been a really good and the best academy for beginners like me. All the best!" |
| 43 | Aisha Z | — | "Had an amazing experience. I had the most amazing trainer ever. I am glad I came to Seekho!" |
| 44 | Inaya | Zainab | "I was hesitant to join at first because I felt that driving a manual car would be challenging for me since I had no experience with it whatsoever I had heard of other institutes and how they can be very strict and how the trainers there are not really bothered with actually teaching their students Many of my friends and family members recommend Seekho , therefore , it was my first choice. I really appreciate the professionalism of your institute. The best part for me was that I felt safe with my trainer and I also really appreciate the fact that Covid SOPs were strictly followed throughout the sessions that I had. My trainer, Zainab, was great. She actually made me look forward to driving manual (which was a big deal for me). I loved how she was always very calm and understanding. Even when I would make mistakes, she never raised her voice or repremanded me in any way. She was also compromising - I was late for a session so she waited outside my house for 20 minutes- She could tell that I was nervous and scared during my first few lessons so she would try her best to encourage me and build up my confidence. My BTW lessons were never boring , I actually had fun 10/10 experience with Seekho" |
| 45 | Maha | Zainab | "Zainab was so great and patient highly recommended" |
| 46 | Sanjina Kimari | Zainab | "Thanks to Seekho and Zainab for helping me overcome my anxiety on the road and go from learning basics to being able to drive" |
| 47 | Zain Raza | — | "It is a great experience would recommend to everyone who wants to learn everything about driving" |
| 48 | Yousuf | — | "A great learning experience Seekho" |
| 49 | Arooj | — | "Great experience, very calm and humble instructor best of luck to seekho" |
| 50 | Anusha | — | "It was a very helpful experience I learnt a lot and had fun driving" |
| 51 | Aria | — | "Great experience with Seekho driving school! Professional amazing teachers would highly recommend!" |
| 52 | Shizah | — | "I had a lot of fun learning from Seekho it taught me a lot of things!" |
| 53 | Kiran | Farkhanda | "Had an amazing time with Seekho Farkhanda was a professional and really helped me gain my confidence while driving" |
| 54 | Zehra | — | "My experience at Seekho could not have been better! Highly recommend" |
| 55 | Superna Kumari | Farkhanda | "It was really great experience with Farkhanda and Seekho team their cooperation is highly appreciating. Thank you for boosting my confidence and helping me in overcoming my fears" |
| 56 | Aleena | — | "Great experience love driving now!" |
| 57 | Hadiyyah | Omaima | "Had the most amazing experience with Seekho and Omaima I feel comfortable and confident driving now! Truly the best!" |
| 58 | Nimras | — | "Loved every class and very crazy ride! Definitely a lot more comfortable driving!" |
| 59 | Sidra Emmad | Farkhanda | "My trainer Farkhanda I looked forward to every class will miss my session!" |
| 60 | Sama | Omaima | "Had amazing 11 sessions with Omaima! No more anxiety for me" |
| 61 | Maha (2) | Zainab | "The lessons with Seekho were just what I needed to great on the road! Zainab was so consistent and encouraging thank you" |
| 62 | Nazish Mirza | Omaima | "Very impressed with Seekho! Extremely professional and clean made me want to learn Omaima kept me very calm on the road too which is what I needed thank you" |
| 63 | Soha | Omaima | "Had an amazing time! Omaima was my trainer and she is so good at her job. Seekho leadership is amazing also love Seekho!" |
| 64 | Amna | — | "It was a great experience looking forward to put my driving skills to use!" |
| 65 | Asmia | — | "Thank you Seekho it was great learning from you! You guys helped me overcome my fear of speed & be confident on the road" |
| 66 | Dua | — | "Loved every bit of an amazing experience every lesson was thoroughly taught" |
| 67 | Ayesha | Omaima | "Had a lot of fun learning how to drive + Omaima is the best teacher" |
| 68 | Ryan. T | Omaima | "Omaima is hands down the best instructor patient & funny great experiences" |
| 69 | Neha Monnoo | Omaima | "Thank you Seekho!! Had an amazing time Omaima is the best trainer" |
| 70 | Sm | — | "Thank you Seekho for great instructor and finally training me how to drive!" |
| 71 | Shahrina | — | "My experience with Seekho was fantastic and so much fun!" |
| 72 | Rejah | — | "Amazing experience! Love! Love! Love!" |
| 73 | Bushra P (2) | — | "Had a great experience and now really enjoying taking it to the streets of Karachi!" |
| 74 | Kiran (2) | Tehreem | "Had a really good experience with Seekho. My trainer Tehreem was so polite and encouraging and helped me overcome all my fears related to parking" |
| 75 | Samra | — | "I am really happy that I chose Seekho training program. I will definitely soon ride on my own. Thank you!" |
| 76 | Maria | Farkhanda | "Had an absolutely amazing experience with Seekho! My instructor Farkhanda did an excellent job, I never thought I would be able to get behind the wheel with so much confidence! So, all thanks to Seekho and Farkhanda!" |
| 77 | Zoha | Tehreem | "Extremely good at what they do! Never thought I will learn how to drive so quickly and effortlessly. Thank you Seekho and thank you Tehreem" |
| 78 | Dr.Roshni | — | "Really helped me overcome my fear of driving after crashing in my own gate! Thank you Seekho. Forever grateful!" |
| 79 | Habiba | Farkhanda | "Better experience than I thought. A huge thank you to Farkhanda and Seekho. Felt comfortable, looked forward every day, became more confident and had fun! Love the Team!" |
| 80 | Rayyan | — | "Originally didn't know how to drive manual but now I can drive both automatic and manual very well – overall very informative experience" |
| 81 | Salma | — | "Good experience overall. Thank you Team Seekho" |
| 82 | Nashmiya | Tehreem | "I loved learning with Seekho, thank you for the experience Tehreem. She was super helpful. So glad to have come here for experience" |

**Instructor mention tally (popularity signal):**
- Omaima — 14 mentions (most-loved; gets "young and hip", "funny", "best at her job")
- Farkhanda — 11 mentions
- Zainab — 9 mentions (gets the longest love-letter review — Inaya, #44)
- Tehreem — 8 mentions
- Muzaffar / Mr. Muzzafar — 3 mentions (only male instructor with testimonial presence)
- Fari (Faryal) — 1 mention
- "Mian saab" — 1 mention

**Dominant emotional theme:** fear/anxiety → confidence. ~30+ testimonials use the exact words "fear", "anxiety", "scared", "nervous", or "overcame". This is the core jobs-to-be-done we must speak to in the rewrite.

---

## 4. Pricing Intel

**What's disclosed on the site (all in the FAQ list — nowhere near the packages):**

| Item | Price |
|---|---|
| Extra / additional BTW session — manual | **Rs 1,800 per lesson** |
| Extra / additional BTW session — automatic | **Rs 2,000 per lesson** |
| Discount: bring your own automatic vehicle | **Rs 2,000 off** |
| Discount: Half & Half (manual/automatic) option | **Rs 1,000 off** |
| Discount: no pickup/drop-off needed | **Rs 1,800 off** |

**What's hidden (the big numbers):**
- Base price of "Teach Me Everything" (manual + automatic) — NOT DISCLOSED
- Base price of "Enhance My Skills" (manual + automatic) — NOT DISCLOSED
- Base price of "Student Bundle" — NOT DISCLOSED
- Any pricing for Traffic Club (kids' program) — NOT DISCLOSED
- Gift voucher amounts — NOT DISCLOSED
- Corporate / defensive driving — NOT DISCLOSED (mentioned as future in Aurora 2019 article)

**Policy signals around price (verbatim):**
> "All prices are fixed and payment has to be made upon registration/blocking slots (non-refundable)"
> "Sessions can not be rescheduled and will be counted as conducted if not attended or cancelled"

**Implication for redesign:** Aurora magazine (2019) confirmed lessons are **45 minutes each**, "Teach Me Everything" = 12 lessons (9 practical + 3 theoretical), "Enhance My Skills" = 9 lessons (6 practical + 3 theoretical). We should push Faryal for current base prices — competitors (Dawood, Ehsan) publish theirs, and hiding price is the #1 conversion killer.

---

## 5. Package Structure

The site presents packages in **two tabs: MANUAL and AUTOMATIC**, with the same 3 packages in each tab. The copy is identical between tabs — only the extras pricing differs.

| Package | Tagline / description (verbatim) | Lessons (per Aurora 2019) | Target |
|---|---|---|---|
| **Teach Me Everything** | "Our best-seller, complete course for a new driver on the road entailing interactive lessons; behind-the-wheel and theoretical sessions" | 12 lessons × 45 min (9 BTW + 3 theory) | Brand-new drivers |
| **Enhance My Skills** | "A short refresher course for people who want to practice their existing driving skills on the roads of Karachi, re-build confidence and reduce road anxiety" | 9 lessons × 45 min (6 BTW + 3 theory) | Have-license-never-drove, returning drivers, confidence-building |
| **Student Bundle** | "A comprehensive course for students studying in Schools and Universities encouraging them to learn this valuable skill from professionals. (I.D card required)" | *Not disclosed* | School / uni students with ID |

**HIDDEN 4th PACKAGE (HTML-commented-out but still in source):**
- **Economy Saver** — "An economical course for people who would not require drivers guide-book, pick-up and drop-off service and air-con in the vehicle"
  → This is currently disabled via HTML comment `-->`. Worth asking Faryal whether to revive (price-sensitive tier) or kill (quality concerns: "no air-con" is a rough sell).

**Footnote below packages (verbatim):**
> "*Please contact 03202-SEEKHO if you require extra classes for supervised practice after the course"

**Manual vs Automatic — how they differ:**
- Same package names on both.
- Only documented difference: extra-lesson price (Rs 1,800 manual / Rs 2,000 auto) and the 3 discount options.
- Fleet: manual = Suzuki Swift 2016 & 2017; automatic = Suzuki Alto 2021.

---

## 6. Team / Instructors

From the site's "our team" section and cross-referenced against testimonial mentions:

| Name | Role | Testimonial mentions | Notes |
|---|---|---|---|
| **Faryal Farooqui** | Founder & CEO | 1 (as "Fari") | Ex-marketing: Aman Foundation, Barclays Bank, Hascol, GSK (per Aurora 2019). Founded Seekho Sep 2019 after personal frustration with existing schools. |
| **Omaima** | Driving Training Officer | **14** | Most popular female instructor; multiple "best teacher" / "hip" / "funny" mentions |
| **Farkhanda** | Driving Training Officer | **11** | Heavily praised for confidence-building |
| **Zainab** | Driving Training Officer | **9** | Subject of the longest glowing testimonial (Inaya) |
| **Tehreem** | Driving Training Officer | **8** | Mentioned in team section context; parking specialist per reviews |
| **Muzaffar / "Mr. Muzzafar" / "Sir Muzaffar"** | Driving Training Officer | 3 | Only male instructor in testimonials |
| **"Mian saab"** | *not in official team section* | 1 | Mentioned in review #6 as "EPIC" — possibly a senior instructor or theory teacher |

**Bios:** None on site. Zero. No photos with names, no years-of-experience disclosed, no background stories. **Big opportunity** for the rewrite — add individual instructor cards with photo + years experience + specialty + a short quote.

Aurora (2019) states hiring criteria: university-educated, 5+ years driving experience, teaching-certified — branded as "Training Executives or Officers" rather than "instructors" for professionalism positioning.

---

## 7. Press / Awards / Partners

### 7.1 Press (external — NOT on the current site)
The "Press" modal on seekhopakistan.com.pk contains **no articles or links**, only unlabelled photos. Real coverage found externally:

| Outlet | Article | Date | URL |
|---|---|---|---|
| **Aurora Magazine (Dawn)** | "Seekho the right way" (by Anusha Zahid) | Nov-Dec 2019 | https://aurora.dawn.com/news/1143603/seekho-the-right-way |
| **Biz Today** | "Seekho opens its doors for learners" | Oct 2, 2019 | https://www.biztoday.news/2019/10/02/seekho-opens-its-doors-for-learners/ |
| **The Nation** | "Seekho opens its doors for learners" | Sep 29, 2019 | https://www.nation.com.pk/29-Sep-2019/seekho-opens-its-doors-for-learners |
| **Blog Pakistan listicle** | "11 Best Driving Schools in Karachi" (listed with a Google-reviews visual asset) | 2023 | https://blogpakistan.pk/driving-schools-in-karachi/ |
| **LinkedIn profile** | Seekho Pakistan | Ongoing | https://www.linkedin.com/in/seekho-pakistan-191759191/ |

**Key quotes usable for the rewrite:**
- Inaugurated by the **Commissioner of Karachi, Iftikhar Ali Shallwani** (Sep 2019) — big legitimacy signal, currently unused on the site.
- Aurora: "first of its kind Driver's Education Program" — but avoid, now dated.
- "Theoretical classes led by Motorway and National Highway officials" — Aurora 2019. Worth confirming if still true.

### 7.2 Awards
- The site repeatedly calls itself "award-winning" but **does not name a single award**. Placeholder text or real? Should ask Faryal.
- "Employee performance award" photos (8 images) appear in the Press slideshow — these look like *internal* awards Seekho gives to staff, not industry awards the school has won.

### 7.3 Partners (logos listed on site)
Carnelian · Dolmen Cares · FM 89 (radio) · SAC (Sindh Academy of Cadet? — clarify) · SIUT · Southshore College · SZABIST · Technology Links · Lecole · Mechanic Ustaad

No partnership descriptions, no case studies, no quotes. Opportunity: turn these logos into a real social-proof bar + one-paragraph context.

---

## 8. FAQ Inventory (verbatim — but note: not Q&A format)

The site's "FAQ" is a bulleted policy list, not Q&A. Here it is raw, all 13 items:

1. "Sessions can be conducted thrice a week or even everyday (upon availability)"
2. "Subsidized rate for learning on your own automatic vehicle on your own automatic vehicle (Rs. 2000 off) or Half&Half manual/automatic option also available (Rs. 1000 off)"
3. "If you don't require pick-up and drop-off service (Rs. 1800 off)."
4. "You must be of legal age to drive (18 years) and to learn with Seekho. Learner's or Permanent driving license is mandatory for Seekho Lessons. (Ask for guidance)"
5. "The final theory session (120 minutes) entailing Tyre-changing demo, Jump-starting vehicle, Under the hood demo, Safety signs, Road safety, First-Aid, Completion certificate, Q/A and Theory test is conducted by a professor, mechanic and the team on almost every Saturday 11:30 am - 1:30 pm (fixed-time/mandatory)"
6. "Introductory theory session (Basics of Driver's Education) is conducted online or in the training room before commencing BTW sessions (60 minutes)"
7. "Sessions can not be rescheduled and will be counted as conducted if not attended or cancelled"
8. "All vehicles are equipped with dual brakes, air-con, dashcams, insurance, first-aid kits, bottled water, masks and sanitizers"
9. "All prices are fixed and payment has to be made upon registration/blocking slots (non-refundable)"
10. "Masks and sanitization are mandatory"
11. "Additional/extra BTW session in Seekho Vehicle (Rs. 1800 per lesson - manual, Rs. 2000 per lesson - automatic)"
12. "Seekho has both male and female trainers available"
13. "Sessions are also available on Sundays"

**Gaps we should proactively answer in the rewrite (no coverage today):**
- How do I get a learner's license? (They link externally to `dls.sindhpolice.gov.pk` but with no hand-holding.)
- How long does the full course take (calendar weeks)?
- What happens if I'm not ready after 12 lessons?
- Is insurance included / what happens if I crash?
- Can I bring a companion in the car?
- Do you teach in Urdu?
- Age upper limit?
- Do I get a completion certificate that's legally recognized?
- Refund policy nuances (currently: blunt "non-refundable")
- Pick-up drop-off for Clifton/Defence only — what about other areas?

---

## 9. Traffic Club

**Concept (verbatim, entire copy on site):**
> "Seekho Traffic Club (STC) is an initiative by Seekho to create awareness regarding road safety amongst children. Inspiring young minds to learn all about road safety is key to preventing accidents later on in life and helping them make better choices. Road safety is something that needs to be done continuously and even subtly at times. STC provides an educational but entertaining way to prepare little ones to be safer and to develop road and traffic awareness."

**What's missing:**
- Age range (says "little ones" only)
- Activities list (workshops? visits? school assemblies?)
- Schools that have hosted it
- Whether it's free, paid, or sponsored by a partner (Dolmen Cares? FM 89? SIUT?)
- How to book / request a session for your school
- Any photos with captions (photos exist in Press slideshow but no context)
- Faryal's personal passion angle — **completely undersold**. The brief tells us this is her kids' road-safety passion project; the site doesn't convey that at all.

**Only CTA:** a generic "download your file" link pointing to `Seekho Leaflet1.jpg`.

**Huge rewrite opportunity:** dedicated Traffic Club page with Faryal's founder story, age brackets, session formats (30-min / 60-min / half-day), partner schools (use the 10 logos), request-a-visit form.

---

## 10. Contact Info

| Channel | Value |
|---|---|
| Phone / SMS | **+92 320 273 3546** (also shown as 0320-SEEKHO) |
| Secondary phone | **0335 3515519** (surfaced in Instagram bio, not on homepage) |
| Email (primary) | **info@seekhopakistan.com.pk** |
| Email (backup) | **seekhopakistan12@gmail.com** |
| Address | **67-E/1, 7th Jami Commercial St, Phase 7 Ext, D.H.A Karachi, Pakistan** (postal code ~75500 per Waze) |
| Google Maps place ID | **ChIJI0HJoRs9sz4RHDQpPnRmNhs** (confirmed via Waze listing) |
| Facebook | https://www.facebook.com/Seekho.org |
| Instagram | https://www.instagram.com/seekho.pk/ (handle `@seekho.pk`, ~4,056 followers per search snapshot) |
| Twitter/X | https://twitter.com/seekhoorg (handle `@SeekhoOrg` — not linked on site) |
| LinkedIn | https://www.linkedin.com/in/seekho-pakistan-191759191/ (not linked on site) |
| YouTube / TikTok | **None found** (one `<iframe>` in source but site has no YT channel linked) |
| WhatsApp | Phone number is SMS-reachable; no explicit WhatsApp deep link on site (`wa.me/` absent). **Big miss — add WhatsApp click-to-chat.** |

**Hours (from Zameen blog + Waze cross-ref, NOT on the site):**
- Mon–Sat: 09:00 – 18:00
- Sun: 10:00 – 15:00
- Mandatory Saturday theory session: 11:30 – 13:30

**Bank details (currently public on site — maybe too public):**
- Account Title: Seekho
- Bank: Meezan Bank, Phase 2 Ext
- A/C: 0115-0103960082
- IBAN: PK58MEZN0001150103960082
- STN: 5450332-4

> **Note:** Displaying full bank account + IBAN on the public homepage is unusual for a consumer-facing business and creates a phishing/fraud vector (someone can make a fake Seekho page, use the same bank details, and pocket deposits). Flag for Faryal — usually these go on an invoice, not the site.

---

## 11. SEO Audit

### 11.1 On-page fundamentals
| Check | Result |
|---|---|
| `<title>` | Just **"Seekho"** — 6 chars, zero keywords. |
| Meta description | **Missing** |
| H1 | **Zero H1 tags** on the page. 18 H2s, 36 H3s. |
| Canonical URL | **Missing** |
| Open Graph tags | **Missing** (no `og:title`, `og:image`, `og:description`) |
| Twitter cards | **Missing** |
| `lang` attribute on `<html>` | Not declared (English content, but no `lang="en"`) |
| Favicon | Present |
| Viewport meta | Present (`width=device-width, initial-scale=1`) |

### 11.2 Schema markup
- **ZERO JSON-LD or microdata schema detected.** No `LocalBusiness`, no `Organization`, no `Review`/`AggregateRating`, no `FAQPage`, no `BreadcrumbList`, no `Course`.
- Massive missed opportunity. A driving school is the textbook case for `LocalBusiness` + `AggregateRating` (with 82 reviews) + `FAQPage` schema — huge rich-result wins.

### 11.3 URL structure
- **Only one real URL: `/`.** All "sub-pages" are modals on the homepage. Every nav link currently navigates to the same URL (or anchor on same URL).
- Sub-page URLs promised by nav (`/faq/`, `/about-us/`, `/contact-us/`, etc.) return **404 from LiteSpeed**.
- **For the redesign:** every section should be a real crawlable URL with its own title, meta, H1.

### 11.4 Sitemap / robots
- `https://seekhopakistan.com.pk/robots.txt` → **404**
- `https://seekhopakistan.com.pk/sitemap.xml` → **404**

### 11.5 Performance (quick curl check)
| Metric | Value |
|---|---|
| Homepage HTML size | 151,894 bytes (~148 KB raw, not gzipped) |
| TTFB / total download | ~850 ms over curl |
| HTTP version | Served via **LiteSpeed Web Server** |
| HTTP → HTTPS | Homepage loads HTTPS fine; but no HSTS observed in response |
| Total images on home | **148 img tags** (everything loads on the single page, since all modals are preloaded) — likely huge LCP issue on 3G |
| Framework | Static HTML + jQuery + Slick carousel (cdn.jsdelivr.net/gh/kenwheeler/slick@1.8.0) — not React/Angular/Vue/WordPress |
| Google Analytics | **Present** (gtag detected) |
| Facebook Pixel | **Not present** — missing retargeting opportunity for a consideration-heavy service |

### 11.6 Image alt text quality
- **148 images total**
- **16 with empty `alt=""`** (decorative-fine if intentional, but some are content images)
- **Many alts are garbage-duplicated**: 8× `seekho-office-image`, 8× `certificate-image`, 8× `employee-performance-award`, 7× `children-road-safety-image`. Zero descriptive alt text.
- Image file names also sloppy: `Group 33.png`, `Mask Group 4.png`, spaces in filenames (`Driving Training Officer.jpg`), uppercase `.JPG`.
- Hero logo is reused 8+ times as header branding across modals — inefficient.

### 11.7 Other SEO issues
- External `<a>` tags to socials are missing `rel="noopener"` (security).
- Mixed case and inconsistent nav labels: "about" vs "About Us", "press" vs "Media" — internal confusion.
- One internal CTA points to Sindh Police portal (`https://dls.sindhpolice.gov.pk/home/getAppointment`) — good touch for the learner's-license flow; keep in rewrite.

### 11.8 Estimated keyword ranking
- Given the "Seekho" title and no content structure, the site essentially only ranks for brand queries ("seekho driving school Karachi"). It will **not** rank for "driving academy Karachi", "driving school DHA", "learn automatic driving Karachi", "women driving school Karachi" — all high-intent terms it should own.

---

## 12. Conversion Audit

### 12.1 User path to booking
Current best-case path from homepage to booked lesson:
1. Land on homepage (no H1 so unclear what exactly this is at first glance)
2. Click "packages" → see 3 package names with one-sentence descriptions, **no prices**
3. Read the footnote: "contact 03202-SEEKHO"
4. Either dial or WhatsApp the number
5. Cold phone conversation to discover price, availability, pickup area
6. Manual bank transfer to Meezan Bank IBAN
7. Wait for Seekho to confirm the slot

**Clicks from home → committed:** effectively one CTA ("Call 0320-2733546") + an off-site phone conversation + bank transfer. **No online booking anywhere.**

### 12.2 Friction / conversion killers (ranked by severity)

| # | Issue | Why it kills conversion |
|---|---|---|
| 1 | **No prices disclosed anywhere** | In Karachi driving-school category, price is the first question. Forcing a phone call loses 60-80% of cold traffic. |
| 2 | **No online booking** | No form, no calendar picker, no instant slot selector. In 2026, many users won't place a cold phone call to a school they don't know. |
| 3 | **No WhatsApp click-to-chat** | Pakistan's dominant comms channel for small businesses. `wa.me/923202733546` is a one-line fix. |
| 4 | **Single-page with modals = shareability dead** | Can't share "the FAQ page" or "the Omaima testimonial" — no URL exists for it. |
| 5 | **No H1, weak title** | Reduces organic arrivals from anyone not already searching "Seekho". |
| 6 | **"Press" modal is images only** | Strong social proof (Aurora, Dawn, Commissioner inauguration) is effectively invisible. |
| 7 | **No Google reviews embed or count** | Site never shows a star rating. 82 testimonials exist but no context ("over 1000+ students since 2019" is the only number). |
| 8 | **Packages differentiated only by copy** | No comparison table, no "what's included" tick-list, no sample schedule. Makes packages feel interchangeable. |
| 9 | **Rigid refund policy front-and-center** | "Non-refundable, non-reschedulable" is true but leading with it is off-putting. Bury or reframe ("Guaranteed slots" vs "non-refundable"). |
| 10 | **Pick-up area limited to Defence/Clifton** | Stated explicitly — OK, but no tier or add-on for other areas. Every customer outside those zones hits a dead end. |
| 11 | **Bank IBAN publicly displayed** | Creates trust concerns + phishing risk. |
| 12 | **No gender/tone cues on landing** | Despite ~80% of testimonials being female-named and Aurora framing it as "women/students/housewives", the hero makes no explicit "women-friendly driving school" promise. Leaves a differentiation win on the table. |

### 12.3 Above-the-fold homepage analysis
- **Hero H2:** "SEEKHO is a unique Driver's Education Program" — abstract, passive. No pain/promise, no location cue ("Karachi"), no tangible outcome.
- **No price tease, no rating, no CTA button** (the phone number appears but isn't a big button).
- **Weak hero image** (banner image with no caption or overlay copy).
- **No reassurance strip** (dual brakes / female instructors / insured cars / 1000+ students).

### 12.4 Mobile experience (inferred)
- 148 images on a single page = heavy scroll + LCP risk on 3G Karachi networks.
- Modals-as-pages on mobile are clunky: you tap "FAQ" and get a full-screen overlay that scrolls within a modal instead of a fresh mobile page.
- Slick carousels (v1.8, 2017 library) have touch-scroll quirks.
- The sticky nav is visible but many labels ("press", "downloads", "students voice") are unclear to first-time mobile users.

---

## 13. Design Assessment

| Aspect | Verdict | Reuse? |
|---|---|---|
| Visual style | Dated (2019 web aesthetic — banner carousels, card grids, serif nav) | No |
| Typography | Google Roboto only; not hierarchical; H2/H3 sizes too similar | No |
| Color palette | Red/white/black, no documented system, inconsistent shades | Re-derive, use red as anchor (strong for traffic/brake association) |
| Photography — vehicles | Decent — clear shots of Swift / Alto with Seekho branding | **Yes — reuse if current** |
| Photography — instructors | Appears to exist (career section has 4 role shots) but not used on main team section | Maybe — need higher-res originals |
| Photography — students | Lots of certificate and classroom photos | **Yes** — great social proof if captioned |
| Photography — Traffic Club | Kids' road safety photos exist but are uncaptioned in slideshow | **Yes — huge emotional asset if properly used** |
| Iconography | Generic Font Awesome-ish; inconsistent sizes | No — redo |
| Layout | Everything scrolls on one page; modal overlays break flow | Rebuild from scratch |
| Logo | "Group 33.png" — unclear it's even the current logo; check source assets | **Flag — confirm current brand mark with Faryal** |

---

## 14. Google Business Presence

I could not load the Seekho Google Maps listing via WebFetch (Google blocks scraping and returns a shell page). However:

- **Confirmed Google Maps place ID:** `ChIJI0HJoRs9sz4RHDQpPnRmNhs` (surfaced via Waze directions page for "Seekho Driving Academy, 7th Jami Commercial Street 11, Karachi")
- **Confirmed address on Google:** 67-E/1, 7th Jami Commercial Street 11, D.H.A. Phase 7, Defence Housing Authority, Karachi 75500
- **Confirmed hours on Google:** Mon-Sat 09:00-18:00, Sun 10:00-15:00
- **Star rating + review count:** **not retrievable via scraping** — blogpakistan.pk listicle mentions that a Google reviews visual is shown but no number is captured.

**Recommendation:** ask Faryal to share her GMB dashboard screenshot (or give us manager access) so we can capture the current star rating and review count, then surface both prominently on the new site. If the rating is 4.5+ with 50+ reviews, it will single-handedly carry the hero section. This is also required for any `AggregateRating` schema on the new site.

---

## Appendix A — Complete Downloads List (19 files, as listed on site)

1. Auto-maintenance by Mechanic Ustaad for Seekho students (PDF)
2. Car-Care Tips (JPG)
3. Dashboard Signs (PDF)
4. Defensive Driving (PDF)
5. Guidelines for Driving License (DOCX)
6. How to Change a Flat Tyre (PDF)
7. Know Your Vehicle (JPG)
8. Parallel Parking (PDF)
9. Practice Test — 100 QS True/False (DOCX)
10. Penalties and Challans (PDF, under NHSO-2000)
11. Safety Signs 1 (JPG)
12. Safety Signs 2 (JPG)
13. Seekho Driver Guidebook (PDF)
14. Seekho Welcome Letter (PDF)
15. Terms & Conditions (DOCX)
16. Test of Competence (PDF)
17. Vehicle Anatomy (JPG)
18. COVID Waiver Form (DOCX)
19. COVID-19 SOPs (JPG)

**Observations:** A mix of JPG/DOCX/PDF — unprofessional format mix. COVID forms are dated (2020-21). Welcome Letter + Guidebook could be the basis for a new gated lead-magnet ("Karachi Learner Driver Starter Kit") in the redesign.

## Appendix B — Partner List

Carnelian · Dolmen Cares · FM 89 · SAC · SIUT · Southshore College · SZABIST · Technology Links · Lecole · Mechanic Ustaad

## Appendix C — Confirmed Facts Worth Preserving

- Founded **September 2019** by Faryal Farooqui
- **Inaugurated by Commissioner of Karachi**, Iftikhar Ali Shallwani
- **1,000+ students trained since 2019** (site's own claim)
- Covered in **Aurora (Dawn)** Nov-Dec 2019 issue
- Theoretical curriculum led by Motorway / National Highway officials (per Aurora — reconfirm with Faryal)
- Instructors recruited with university degrees + 5+ years' driving experience
- Fleet: Suzuki Swift 2016 & 2017 (manual), Suzuki Alto 2021 (automatic) — dual brakes, dash-cams, insurance
- Pick-up/drop-off: Defence & Clifton only
- Male + female instructors; Sunday sessions available
- Runs Seekho Traffic Club (STC) — road safety program for children
- Registered entity: **Seekho (Pvt.) Ltd.** (copyright 2021 on footer — footer needs updating)

## Appendix D — Immediate Fix List for the New Static Site

High-ROI items to not forget in the redesign, ranked:

1. Real URL per section (`/packages/`, `/students/`, `/instructors/`, `/faq/`, `/traffic-club/`, `/contact/`)
2. Unique `<title>` + meta description per page
3. One H1 per page; clear heading hierarchy
4. JSON-LD schema: `LocalBusiness` + `AggregateRating` + `FAQPage` + `Course` on package pages
5. **Publish prices** — at least "from Rs XX,XXX" with tier comparison table
6. WhatsApp click-to-chat button (sticky)
7. Online booking form (at minimum: name, phone, package, preferred start date → sent as email/WhatsApp lead)
8. Google Reviews embed with live rating + review count
9. Instructor profile cards with photo + years + testimonials-per-instructor (Omaima alone has 14)
10. Press strip with real article links (Aurora, Dawn, Biz Today, The Nation)
11. Traffic Club dedicated page — Faryal's story + school booking CTA
12. Sitemap.xml + robots.txt
13. Remove public bank details from homepage (invoice-only)
14. Descriptive image alt text + compressed WebP images
15. Update footer copyright (currently 2021)
16. Consider reviving or killing the commented-out "Economy Saver" tier
