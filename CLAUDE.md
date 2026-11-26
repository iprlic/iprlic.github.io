# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
bundle install              # Install dependencies
bundle exec jekyll serve    # Run local dev server with live reload
bundle exec jekyll build    # Build to _site/
pkill -f "jekyll serve"     # Kill the server
```

Note: `_config.yml` changes require a server restart — livereload does not pick them up.

## Architecture

This is a Jekyll static site deployed to GitHub Pages at `prlic.io` (CNAME). It uses a remote theme (`iprlic/creative-theme-jekyll-new` via `jekyll-remote-theme` plugin), so layout and styling files are not present locally — they are downloaded at build time to a temp directory (`/var/folders/.../jekyll-remote-theme-*/`).

**One page per language, plus two redirect stubs:**

| File | URL | Lang | `ref` | Purpose |
|------|-----|------|-------|---------|
| `index.md` | `/` | en | `home` | The whole offer, one page |
| `hr/index.md` | `/hr/` | hr | `home` | Croatian equivalent |
| `ai-advisory.md` | `/ai-advisory/` | — | — | Redirect to `/#packages` |
| `hr/ai-savjetovanje.md` | `/hr/ai-savjetovanje/` | — | — | Redirect to `/hr/#packages` |
| `talks.md` | `/talks/` | en | `talks` | Conference talks, from `_data/talks.yml` via `_layouts/talks.html` |
| `hr/predavanja.md` | `/hr/predavanja/` | hr | `talks` | Croatian equivalent |
| `training.md` | `/training/` | en | `training` | Claude and AWS training courses (home layout, services + faq + contact); linked from the Team Training package and the footer |
| `hr/edukacija.md` | `/hr/edukacija/` | hr | `training` | Croatian equivalent |
| `training/claude-associate.md` | `/training/claude-associate/` | en | `training-claude-associate` | Course page: Claude for Business Teams (CCAO-F exam prep) |
| `hr/edukacija/claude-associate.md` | `/hr/edukacija/claude-associate/` | hr | `training-claude-associate` | Croatian equivalent |
| `training/claude-developer.md` | `/training/claude-developer/` | en | `training-claude-developer` | Course page: Building with Claude (CCDV-F exam prep) |
| `hr/edukacija/claude-developer.md` | `/hr/edukacija/claude-developer/` | hr | `training-claude-developer` | Croatian equivalent |
| `training/claude-architect.md` | `/training/claude-architect/` | en | `training-claude-architect` | Course page: Architecting with Claude (CCAR-F exam prep) |
| `hr/edukacija/claude-architect.md` | `/hr/edukacija/claude-architect/` | hr | `training-claude-architect` | Croatian equivalent |
| `training/claude-architect-professional.md` | `/training/claude-architect-professional/` | en | `training-claude-architect-professional` | Course page: Advanced Claude Architecture (CCAR-P exam prep) |
| `hr/edukacija/claude-architect-professional.md` | `/hr/edukacija/claude-architect-professional/` | hr | `training-claude-architect-professional` | Croatian equivalent |
| `training/build-ai-agents.md` | `/training/build-ai-agents/` | en | `training-build-ai-agents` | Course page: Build AI Agents with Claude (no-code, not exam-linked; 6-week cohort or 3 days in-house). Linked from the `#practical-ai` section |
| `hr/edukacija/ai-agenti.md` | `/hr/edukacija/ai-agenti/` | hr | `training-build-ai-agents` | Croatian equivalent |
| `training/ai-regulated-public-sector.md` | `/training/ai-regulated-public-sector/` | en | `training-ai-regulated-public-sector` | Course page: AI in Regulated and Public-Sector Organisations (2 days in-house, not exam-linked; EU AI Act, GDPR, NIS2, classified information, AI security, procurement, governance). Promo only, added 21 Nov 2026: no slides yet, CTA is "Register interest"; remove the "New course" note once the first run is booked. Linked from the `#practical-ai` section |
| `hr/edukacija/ai-regulirane-djelatnosti.md` | `/hr/edukacija/ai-regulirane-djelatnosti/` | hr | `training-ai-regulated-public-sector` | Croatian equivalent (adds Croatian law: Zakon o provedbi Opće uredbe o zaštiti podataka, Zakon o kibernetičkoj sigurnosti, Zakon o tajnosti podataka levels) |
| `privacy.md` | `/privacy/` | en | `privacy` | Privacy notice (GDPR Art. 13: controller, e-mail enquiries, Calendly, Cloudflare Web Analytics, GitHub Pages hosting, Google Fonts, retention, rights, AZOP). Linked from the footer. Update when a processor changes (e.g. if Inter is self-hosted, drop Google Fonts) |
| `hr/privatnost.md` | `/hr/privatnost/` | hr | `privacy` | Croatian equivalent |
| `training/claude-mock-exams.html` | `/training/claude-mock-exams/` | - | - | Redirect stub to `https://certdrill.io/exams/` (the old self-hosted practice app was removed); `sitemap: false`, `noindex`, canonical to certdrill.io. Keep it: the URL was public |
| `training/claude-certifications.md` | `/training/claude-certifications/` | en | `training-claude-certifications` | Guide: "Which Claude certification should I take?" One comparison table of all five exams (`comparison-table.html`), how to choose by role, FAQ. Linked from the `#claude` intro, every course page's exam section. Update it whenever an exam guide changes |
| `hr/edukacija/claude-certifikacije.md` | `/hr/edukacija/claude-certifikacije/` | hr | `training-claude-certifications` | Croatian equivalent |
| `training/claude-exam-eligibility.md` | `/training/claude-exam-eligibility/` | en | `training-claude-exam-eligibility` | Guide: who can take the Claude exams (Claude Partner Network requirement, registration via Partner Academy and Pearson VUE) and what non-partner companies can do instead. States only what the exam guides and Anthropic's eligibility page support |
| `hr/edukacija/claude-ispiti-uvjeti.md` | `/hr/edukacija/claude-ispiti-uvjeti/` | hr | `training-claude-exam-eligibility` | Croatian equivalent |
| `training/claude-confusions.md` | `/training/claude-confusions/` | en | `training-claude-confusions` | Guide: 14 pairs of Claude concepts that get mixed up, as `course-overview` cards in four sections (API, agents and extensions, Claude Code, apps/quality/exam), each with use-X-when / use-Y-when, an example and "Tested in" exam codes; FAQ with 6 questions. Facts checked against platform.claude.com and code.claude.com docs; re-check when features change (forced tool use, beta features) |
| `hr/edukacija/claude-pojmovi.md` | `/hr/edukacija/claude-pojmovi/` | hr | `training-claude-confusions` | Croatian equivalent (feature names kept in English) |
| `training/claude-certification-changes.md` | `/training/claude-certification-changes/` | en | `training-claude-certification-changes` | Dated log of Claude certification program changes, newest first, rendered by `_includes/change-log.html` from `_data/claude_cert_changes.yml` (one entry per change with `en`/`hr` text and source links; add new entries at the top). Bump `last_updated` and the "Last checked" proof/note on both pages when adding or re-checking. Linked from the `#claude` intro, the comparison page and the confusions page |
| `hr/edukacija/claude-certifikacije-promjene.md` | `/hr/edukacija/claude-certifikacije-promjene/` | hr | `training-claude-certification-changes` | Croatian equivalent (same data file, `hr` text; dates use `months_genitive` from `_data/i18n.yml`) |
| `training/for-training-providers.md` | `/training/for-training-providers/` | en | `training-providers` | For training companies and academies: white-label delivery of the Claude, practical AI and official AWS courses. Partner rates are never published here; the partner kit PDF is "on request" only. Linked from the training FAQ's training-companies answer |
| `hr/edukacija/edukacijske-kuce.md` | `/hr/edukacija/edukacijske-kuce/` | hr | `training-providers` | Croatian equivalent |

**Practice questions live on certdrill.io** (Ivan's own product, by Prlić Consulting; repo `~/Projects/claude-certification-courses/exam-site`). The self-hosted practice app at `/training/claude-mock-exams/` (index.html, questions.js, MIT notice) was removed in Nov 2026 and replaced by the redirect stub above. Course pages link to their exam's free set (`https://certdrill.io/exams/<code>/free/`), the training intros and FAQ link to `https://certdrill.io/`. Do not state prices or question counts on this site unless read from certdrill.io. `~/Projects/claude-certification-courses/mock-exams/tools/make_public.py` no longer writes into this site (default output is `mock-exams/public/questions.js`); never copy question banks here. The free CCDV-P cheat sheet PDF is at `assets/downloads/ccdv-p-cheat-sheet.pdf`.

The four course pages use the home layout with `header.compact: true` (short hero) and the sections `course-overview` (who it's for + outcomes) → `course-modules` (outline with labs) → `course-overview` (exam facts + prerequisites) → `faq` → `contact`. Each is linked from its card in the `#claude` services section of the training page. The training pages also carry a `#practical-ai` services section (right after `#claude`) for courses not tied to an exam: Build AI Agents with Claude (full course page, same structure but the third section is `formats`, cohort vs in-house, instead of exam facts), AI Strategy for Leaders and Claude Code for Engineering Teams (cards only, "outline on request"). Their slugs are translated (`ai-agenti`) since there is no certification name to keep. The Croatian certification-course slugs keep the certification name (`claude-associate`, ...) because the certification names are not translated on the Croatian pages either. Course facts (modules, labs, exam numbers) come from the course decks in `~/Projects/claude-certification-courses/<CODE>/`; when the exam guides change (CCAO-F, CCDV-F and CCAR-P content changes on 7 December 2026), update the exam facts and remove the dated `note` once the courses are reviewed. The FAQ's affiliation answer must stay: independent trainer, not official Anthropic courses, exams at Pearson VUE via the Anthropic Partner Academy.

The site used to be split into an engineering homepage and a separate `/ai-advisory/` landing page. They were merged in Sept 2026: the split duplicated four sections (clients, contact, who, crosslink) across two pages and doubled the translation burden for a solo consultancy. The two old URLs are kept as redirect stubs because they were given out in outreach — **do not delete them.** They use a meta-refresh plus `window.location.replace`, not `jekyll-redirect-from`, so no extra plugin is needed on GitHub Pages' classic build. Both carry `sitemap: false` and `noindex`, and have no `ref`, so they stay out of the sitemap and the hreflang graph.

**Never move or rename `/talks/`** (it was meant for a QR code on conference slides), and never change a talk's `id` in `_data/talks.yml`, since it is the anchor. A new talk is one entry in that file. `slides`, `video`, `event.url` and `track` are optional and render nothing when empty; "slides will be posted" shows only before the talk date. To publish slides, post a cleaned PDF under `assets/talks/<id>/` (no speaker notes, client never named) and set `slides`. Current entry: kAI? by Voogle 2026 (12 Nov 2026, HNK Varaždin, in Croatian), deliberately with no event link (Ivan's call, 26 Nov 2026). Its slides button points to `assets/talks/voogle-2026/private-claude-deployment-voogle-2026.pdf` (exported from PowerPoint, all 32 slides, no notes); `_config.yml` keeps `assets/talks` out of the sitemap. The deck carries Sedmi Odjel branding and keeps all backup slides by Ivan's choice, but the site's own text still never names it; the talk was given for Sedmi Odjel, which is never named on this site. AI2Future 2026 was removed: Ivan did not give that talk. The page labels live in each page's `labels` front matter.

Editing the site means editing `index.md` and `hr/index.md`. Both are single-page layouts defined entirely via YAML frontmatter `sections`, where each section's `type` maps to a local `_includes/` override.

**Section-level parity between languages is required** — any section added to one language must be added to the other, or the language switcher drops the visitor onto a page missing content they were just reading. **Item-level divergence inside a section is intentional** and should not be "fixed": the Croatian page targets a different market (see below). It currently carries 9 FAQ questions to the English page's 7.

### The Croatian page targets Croatia specifically

The English page sells to regulated EU/US mid-market on a data-residency wedge. The Croatian page sells to **Croatian** companies and public sector, where that wedge is much weaker: only ~15% of Croatian firms with 10+ employees use any AI technology, so the buyer's question is "where do we start and does it pay off", not "can you keep our data in the EU".

Consequences baked into the Croatian page, all deliberate:

- Sectors follow the draft national AI plan to 2032 (public administration, healthcare, energy, transport, tourism, financial services), not the English page's regulated-industry list.
- The Assessment lists a deliverable framed as technical groundwork an EU-funds consultant can use. **Never claim a call will fund the assessment itself.** On the SME digitalisation calls, advisory *is* an eligible cost but capped very low — €2,000 in the last such call, against grants of €30,000–€120,000. The money is in implementation (tools, software, equipment). The FAQ says this plainly with the figure; keep it that way, and update the figure when a new call publishes its terms.
- Croatian copy uses the vocabulary the market already uses, harvested from PwC Croatia, the EDIH network, HGK and the grant call documents: `digitalna zrelost`, `slučajevi primjene`, `prihvatljivi troškovi`, `savjetodavne usluge`, `projektni prijedlog`, `MSP`, `računalni vid`, `strojno učenje`, `uvođenje AI-ja u poslovanje`, `smanjite rizik od neuspjeha`. Do not "improve" these into more literal translations of the English — they are the terms buyers and funds consultants search for and recognise.
- Two extra FAQ entries: EU co-financing, and working in Croatian / on-site in Croatia.
- "Fractional AI vodstvo" was renamed "AI vodstvo bez stalnog zaposlenja" — "fractional" does not parse for a Croatian mid-market buyer.
- Prices are identical to the English page and stay that way. The Croatian budget problem is solved through co-financing and EDIH routes, not discounting.

## Internationalisation

No plugin. GitHub Pages builds this repo with its classic build, so only whitelisted plugins are available and `jekyll-polyglot` is not one of them. i18n is done natively:

- Each page declares `lang: en|hr` and `ref: <translation key>`. Pages sharing a `ref` are translations of each other.
- `_includes/nav.html` finds the sibling with `site.pages | where: "ref" | where_exp: "p.lang == alt_lang"` and points the language switcher at it, so switching from `/ai-advisory/` lands on `/hr/ai-savjetovanje/` rather than the homepage. It falls back to that language's home page if no sibling exists.
- `_layouts/base.html` sets `<html lang>` and emits `hreflang` alternates plus `x-default` (English) from the same `ref` grouping.
- `_data/menus.yml`, `_data/footer.yml` and `_data/i18n.yml` are all keyed by language code. `i18n.yml` holds only strings hardcoded in includes; anything in page frontmatter is translated there instead.
- English lives at `/`, Croatian under `/hr/`. Croatian slugs are translated too (`ai-savjetovanje`, not `ai-advisory`).

### Croatian YAML gotcha

A list item containing `: ` is parsed by YAML as a mapping, not a string, and renders as `{"key"=>"value"}` on the page. Croatian copy hits this far more often than English because of constructions like `Program za upravu: što financirati`. **Quote any list item containing a colon.** To check all four pages at once, parse each file's frontmatter and assert every entry in `deliverables`, `fit`, `not_fit`, `outcomes` and `questions` is a `str`.

## Titles and SEO

`jekyll-seo-tag` owns the `<title>` tag. Do not add one to `_layouts/base.html` — that produced two `<title>` tags on every page for a long time. `site.title` is the site name only (`Ivan Prlić`); the role sits in `site.tagline`. Each page sets its own `title`, and seo-tag renders `<page title> | <site title>`.

**Social preview images.** seo-tag reads `page.image`, *not* `site.image` — setting only the latter silently emits no `og:image` at all, which is what happened here. The site-wide default is set via the `defaults` block in `_config.yml`; pages override it with their own `image:`. Cards are generated by `tools/generate-og-images.py` (needs `rsvg-convert`); edit the `CARDS` dict there and re-run rather than editing PNGs.

## SEO

Handled by `jekyll-seo-tag` plus a hand-written `@graph` in `_layouts/base.html`. Things that
have bitten before, so check them after any config change:

- **`page.image` must be the object form** (`path` / `width` / `height`), not a bare string, or
  `og:image:width` and `og:image:height` are omitted and cards reflow while loading.
- **Do not add a `twitter:` block or `social.name` to `_config.yml` without a real handle.**
  With them present but empty, seo-tag emitted `twitter:site="@"` and `twitter:creator="@Ivan
  Prlić"` — neither is a valid handle. seo-tag already picks `summary_large_image` whenever an
  image is set, so the block buys nothing.
- **`social.links` drives the `sameAs`** in seo-tag's JSON-LD. Only list profiles that exist.
- **Keep the `@graph` in step with the copy.** `jobTitle`, `description` and `knowsAbout` went
  stale once, still describing a DevOps-led practice long after the site moved to AI advisory.
  `hasOfferCatalog` is emitted only on pages that render a `packages.html` section, so it never
  dangles on 404.
- Meta descriptions stay **under 160 characters** or Google truncates them.
- `jekyll-feed` is disabled in both `_config.yml` and the `Gemfile` — with no posts it produced
  an empty `feed.xml`. Re-enable both when `_posts/` has content.
- Biggest remaining lever is content: the site ranks for the brand name and little else until
  there are articles. See the To Do list.

## Frontend assets

There is no jQuery, no Bootstrap JS, no Font Awesome, and no CDN dependency except Google Fonts. That is deliberate — do not reintroduce them.

- **JS** is one local file, `assets/js/site.js`: mobile nav toggle, navbar-scrolled class, and IntersectionObserver nav highlighting. It replaced the theme's `creative.js`, which pulled in jQuery, Bootstrap's bundle, `jquery-easing` (for `easeInOutExpo`) and `magnific-popup` (for a `#portfolio` lightbox this site does not have).
- **Testing scroll behaviour in the browser tool**: programmatic `window.scrollTo` dispatches no scroll events and `IntersectionObserver` never fires inside iframe probes, so anything scroll-driven reads as broken there. Use the `computer` scroll action (real input events) on a top-level page instead, and force `scroll-behavior: auto` first — smooth scrolling is suppressed when the window is unfocused.
- **The sticky CTA is visible by default and hidden by a class.** Do not switch it to the `hidden` attribute: the UA stylesheet's `[hidden] { display: none }` beats a class-level `display` rule and kills the slide transition, and default-visible degrades correctly without JS.
- **Anchor scrolling is CSS, not JS**: `scroll-behavior: smooth` plus `[id] { scroll-margin-top: 72px }` in `main.scss`. This also fixes cold loads on a URL like `/#work`, which script-driven scrolling never handled. Don't move it back into JS.
- **Icons** are an inline SVG sprite, `_includes/icon-sprite.html`, injected once at the top of `<body>` and referenced as `<svg class="icon"><use href="#fa-brain"/></svg>`. Symbol ids match the `fa-*` names already used in front matter. Regenerate with `python3 tools/build-icon-sprite.py` after adding an icon — add it to the `ICONS` dict first. Inline rather than an external sprite file because Safari does not support cross-file `<use href="sprite.svg#id">`.
- Inter is loaded by a single non-blocking `<link>` in `base.html`. Do not add a CSS `@import` for it in `main.scss` — that fetches it twice and blocks rendering.

## Page flow

Order follows the order buyers ask questions:
`hero → clients → packages → services → work → who → faq → contacts`.

Prices land at ~1.9 screens because `header.proof` puts a price chip at the fold; without it the
first price is three screens down. `services` sits *after* `packages` on purpose: the priced
advisory ladder is the lead offer, and bespoke engineering is the "also available" tail.

Backgrounds must keep alternating (subtle / white / subtle / white / dark / subtle / dark) —
check the neighbours before adding `background_style: bg-subtle` to a new section.

Sections are sized with padding, not `min-height: 80vh`. The old min-heights stretched ~450px
of content into 720px boxes, costing ~500px of dead space per page.

Keep the Calendly CTA count low: the featured package, the nav button, the sticky mobile bar and
the contact section. Five identical "Book an intro call" links inside one section gave the reader
no signal about which to click.

The whole page is ~8.8 screens at 1440x900. The two pages it replaced were 7.1 + 11.2.

## Accessibility

Every page has a `<main id="main">` landmark and a skip link (`.skip-link`, off-screen until
focused). Touch targets are forced to 44px minimum below 992px — nav, footer, contact chips,
FAQ summaries, package CTAs and the badge links were all under it.

All body text meets WCAG AA (4.5:1). The greys are chosen for it: `#5b6b81` is the lightest grey that passes on white, `#f8fafc` and `#f1f5f9` alike, and `#15803d` is the green that passes on the `#f0fdf4` chip background. `#94a3b8` and `#16a34a` both fail — don't reach for them. On the navy sections, white text needs at least 0.5 alpha. Public sector procurement in the EU can require conformance, and that is a target segment.

**`_config.yml`** holds global settings: site title, nav title, URL, OG image, social links, plugin config.

**`_data/menus.yml`** controls nav links, keyed by language. There is a single `header` menu now; a page selects its language with `lang`. The last item in a list renders as a primary CTA button; "Book a Call" is appended separately in `_includes/nav.html` and its label/URL can be overridden per page with `nav_cta_label` / `nav_cta_url`. Set `highlight: true` on an item to accent it.

Anchor-only URLs (`#work`) are emitted bare and get the theme's smooth scroll; everything else goes through `relative_url`. Do not pipe `#foo` through `relative_url` — it becomes `/#foo` and jumps to the homepage from any subpage.

**`_data/footer.yml`** contains the footer copyright string, the analytics note, and `legal`: the company details a Croatian d.o.o. must show on its website (ZTD Art. 21 / ZET Art. 6: full name, seat, registry court and MBS 081127680, OIB, share capital and that it is paid in full, director, bank and IBAN). Keep them in step with the court register; never add Ivan's phone number.

The `_site/` directory is build output — never edit it directly, it's gitignored.

## Local Overrides

All layout/include overrides live locally and take precedence over the remote theme:

| File | Purpose |
|------|---------|
| `_layouts/base.html` | Font (Inter), JSON-LD schema, deferred JS, active nav JS |
| `_layouts/home.html` | Removes text-uppercase from hero h1, adds hero subtitle; `header.compact: true` adds `masthead-compact` (short hero, used by the course pages) |
| `_includes/nav.html` | Language-keyed menu, two CTA buttons, language switch, anchor-safe hrefs |
| `_includes/about.html` | Two-column layout with photo, badges, tech stack, and the compact `certs` chip row (certifications no longer have their own section) |
| `_includes/services.html` | Service cards with icon circles (`text` is markdownified, so links work). Optional section `intro` renders a lede under the heading; the key is `intro`, not `text`, because the home pages' services sections carry an unrendered `text` |
| `_includes/case-studies.html` | Case study cards with outcome chips. `featured: true` spans the full row (the regulated GenAI study uses it, which keeps a 5-study grid balanced) |
| `_includes/contact.html` | Dark section with contact buttons; `watermark` sets the giant background word |
| `_includes/footer.html` | Two-column: copyright left, links right |
| `_includes/packages.html` | Priced offer cards + OfferCatalog JSON-LD. `featured: true` = full width, accent border, two-column deliverables |
| `_includes/testimonials.html` | Quote cards. **Renders nothing until real `quotes` are supplied** — never invent them |
| `_includes/clients.html` | Client name chips. Takes `clients[]` of `{ name }` |
| `_includes/faq.html` | Native `<details>` accordion + FAQPage JSON-LD. No JS; answers stay crawlable while collapsed |
| `_includes/course-overview.html` | Course pages: optional `facts[]` stat row (`label`/`value`, a `<dl>`) and `columns[]` cards (`title`, `text`, ticked `items`), plus an optional `note`. Used twice per course page (overview, exam) |
| `_includes/course-schema.html` | Course JSON-LD, included from `base.html` when a page has a `course:` block (`order`, `level`, optional `exam`, `workload` as ISO 8601, optional `price_from` only where a price is published, optional `instances`). Name, outcomes, prerequisites and modules are read from the page's own sections. Never emits `educationalCredentialAwarded`: the courses are exam prep |
| `_includes/course-list-schema.html` | ItemList of the same-language course pages (ordered by `course.order`), on pages with `course_catalog: true` (the two training pages) |
| `last_updated` front matter | Renders "Last updated / Ažurirano: <month year>" under the hero (`home.html`, months in `_data/i18n.yml`) and the Course `dateModified`. Bump it when a course page changes |
| `llms.txt` (site root) | Plain-text summary for AI assistants: courses, prices, contact. Update it with the training pages |
| `_includes/comparison-table.html` | Guide pages: a table with rows as attributes and columns as the things compared (`columns[]`, `rows[]` of `label` + `cells[]`, cells markdownified inline, `<br>` for line breaks). Scrolls sideways under 992px with a sticky first column and an optional `scroll_hint` |
| `_includes/change-log.html` | Dated change log from a data file (`section.data`, default `claude_cert_changes`): entries newest first with date (`precision: month` for month only), exam chips, `what`/`who` text in the page's language and source links. Labels (`who`, `source`, `exams`) come from the section's `labels` |
| `_includes/course-modules.html` | Course pages: numbered module cards (`modules[]` of `title`, `text`, optional `lab`). "Module"/"Lab" labels come from `_data/i18n.yml` (`module`, `lab`) |

## Styling

- `assets/css/main.scss` — all custom CSS. Compiled by Jekyll.
- Design: dark navy (`#0f172a`) + blue (`#2563eb`), Inter font
- Bootstrap 4.5 is loaded via the theme — use Bootstrap grid/utilities freely
- CSS specificity: Bootstrap uses `!important` heavily. Use a `.component-class .child` selector or `!important` overrides when fighting Bootstrap rules.
- **The remote theme fights back.** Creative v6.0.4 sets `font-family: "Merriweather Sans"` (a font this site never loads, so it falls back to a system font) and its orange `#f4623a` on selectors more specific than plain element/class rules: `h1-h6` **and `.h1-.h6`**, `.btn`, `#mainNav .navbar-brand`, `#mainNav .navbar-nav .nav-item .nav-link`, `.btn-outline-primary`, and `.nav-link.active` (with `!important`). A "Remote theme overrides" block near the top of `main.scss` matches that specificity — check it first if text renders in the wrong font or something turns orange. Watch for `class="h5"` on an `<h3>` (services.html does this): the class beats a bare element selector.
- The theme colours nav links `rgba(255,255,255,0.7)` until `.navbar-scrolled` is applied, which is invisible against this site's always-white navbar. The override block pins them for both states; any new nav rule must use the full `#mainNav .navbar-nav .nav-item .nav-link` chain or it will silently lose.
- Scope component CSS to the component's own class, never to `#section-id` — includes get reused across pages under different `section_id` values. (`.about-section .about-title`, not `#about .about-title`.)
- `bg-dark` class applies `background-color: #343a40 !important` — avoid it on custom dark sections, use `.about-section { background-color: #0f172a !important }` instead

## Certifications YAML format

Certs live under the `about.html` section as a flat `certs` list of `name` + optional `url` pairs (not plain strings). They render as a compact chip row; there is no separate certifications section any more.

```yaml
certs:
  - name: Solutions Architect – Professional
    url: https://www.credly.com/badges/...
  - name: Champion Innovator – Databases   # no url = plain chip, no link
```

## Key Details

- Ruby version: 2.6.5 (see `.ruby-version`)
- Jekyll ~4.2.2, minima theme ~2.5.1
- Plugins: jekyll-feed, jekyll-sitemap, jekyll-seo-tag, jekyll-remote-theme
- Google Analytics removed (no cookie consent needed)
- OG image: `assets/img/og-image.png` (1200×630, generated from SVG)
- Favicon: `assets/img/favicon.svg` + `favicon.png` (IP initials, dark navy)
- No blog posts under `_posts/`

## Pricing

Prices are "from €X" anchors, deliberately. They filter unqualified enquiries and signal a productized practice rather than hourly work. Keep them; do not soften to "price on enquiry". Current ladder: Workshop €1,500 · Assessment €10,000 · Proof of Value €30,000 · Fractional €5,000/mo · Training €4,000.

The assessment's fee-credit offer (credited in full against a build booked within 90 days) is the mechanism that converts assessments into builds. Keep it prominent.

## To Do

- **Croatian proofread** — the Croatian copy was written by Claude, not by a native speaker, and has not been reviewed by Ivan. It was rewritten once to remove translationese, but still needs a native read before `/hr/` is promoted anywhere.
- **Testimonials** — highest impact remaining content gap. The `testimonials.html` include and a commented-out section block sit in both `index.md` and `hr/index.md`; uncomment and fill in 2-3 verbatim quotes from LinkedIn recommendations. Never invent quotes. **Status Nov 2026: there are no usable client testimonials** (Ivan's only LinkedIn recommendation is from 2013 and about .NET); this needs 2-3 real, recent quotes from Ivan (clients who agree to be quoted) before anything is added.
- **Case study numbers** — outcome chips are qualitative. Any that Ivan can back with a real figure (hours saved, cost reduced, time to market) should be restated in money, especially on the advisory page.
- **Blog / thought leadership** — write for buyers, not engineers. Suggested topics: what a production RAG system costs to run for a year; why the first AI use case should be boring; keeping AI inside the perimeter under EU data residency.
- **Five unanswered FAQ questions** — the FAQ on both pages ships with seven answered questions and five stubbed out in comments at the bottom of the `faq.html` section block: NDA/DPA, professional indemnity insurance, IP ownership, payment terms, and third-party AI tooling on client material. These are the ones enterprise procurement asks last and that most often stall a deal. Only Ivan can answer them — **do not invent answers**. When filling them in, translate into `hr/index.md` at the same time.

## Sourcing facts about Ivan

`../cv` (`~/Projects/ip-profile/cv`) holds the CV repo. `README.md` there is the most current consolidated summary; `resume/*.tex` has per-engagement detail, and `prlic-consulting-company-presentation.html` has the company boilerplate including OIB 84570551730. Use those rather than inferring. Facts already mined into the site: SOC 2 / financial-grade work at Q.ai, the Metro / Ricoh / TUI team-collaboration examples, company registration details, and the client list.

Note the CV contains **no quantified outcomes** — no percentages, cost reductions, or timings — which is why the case-study chips remain qualitative.

**IndexNow.** `.github/workflows/indexnow.yml` runs after every GitHub Pages build (`page_build` event, also runnable by hand from the Actions tab) and submits every URL in `sitemap.xml` to api.indexnow.org, which feeds Bing (and through it ChatGPT search), Yandex and others. The key file `5212ee2706c40323f81de3f6b2274329.txt` at the site root proves ownership; don't delete or rename it, and keep the key in the workflow in sync if it ever changes.
