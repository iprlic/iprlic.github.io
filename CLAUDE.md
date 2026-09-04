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

**There are two pages in two languages — four files, and they must stay in sync:**

| File | URL | Lang | `ref` | Audience |
|------|-----|------|-------|----------|
| `index.md` | `/` | en | `home` | CTOs, VPs Eng, Toptal referrals. Sells capability. |
| `ai-advisory.md` | `/ai-advisory/` | en | `advisory` | Executives at regulated EU mid-market firms. Sells priced packages. |
| `hr/index.md` | `/hr/` | hr | `home` | as above, Croatian |
| `hr/ai-savjetovanje.md` | `/hr/ai-savjetovanje/` | hr | `advisory` | as above, Croatian |

Keep the two *pages* distinct: do not merge advisory framing back into the homepage, the split exists so neither audience gets a diluted message.

**Section-level parity between languages is required** — any section added to one language must be added to the other, or the language switcher drops the visitor onto a page missing content they were just reading. **Item-level divergence inside a section is intentional** and should not be "fixed": the two advisory pages target different markets (see below). As of the Croatian repositioning the HR advisory page has 6 fit items vs 5, 5 not-fit vs 4, and 9 FAQ questions vs 7.

### The HR advisory page targets Croatia specifically

`/ai-advisory/` sells to regulated EU/US mid-market on a data-residency wedge. `/hr/ai-savjetovanje/` sells to **Croatian** companies and public sector, where that wedge is much weaker: only ~15% of Croatian firms with 10+ employees use any AI technology, so the buyer's question is "where do we start and does it pay off", not "can you keep our data in the EU".

Consequences baked into the HR page, all deliberate:

- Sectors follow the draft national AI plan to 2032 (public administration, healthcare, energy, transport, tourism, financial services), not the EN page's regulated-industry list.
- The Assessment lists a deliverable framed as technical groundwork an EU-funds consultant can use. **Never claim a call will fund the assessment itself.** On the SME digitalisation calls, advisory *is* an eligible cost but capped very low — €2,000 in the last such call, against grants of €30,000–€120,000. The money is in implementation (tools, software, equipment). The FAQ says this plainly with the figure; keep it that way, and update the figure when a new call publishes its terms.
- Croatian copy uses the vocabulary the market already uses, harvested from PwC Croatia, the EDIH network, HGK and the grant call documents: `digitalna zrelost`, `slučajevi primjene`, `prihvatljivi troškovi`, `savjetodavne usluge`, `projektni prijedlog`, `MSP`, `računalni vid`, `strojno učenje`, `uvođenje AI-ja u poslovanje`, `smanjite rizik od neuspjeha`. Do not "improve" these into more literal translations of the English — they are the terms buyers and funds consultants search for and recognise.
- Two extra FAQ entries: EU co-financing, and working in Croatian / on-site in Croatia.
- "Fractional AI vodstvo" was renamed "AI vodstvo bez stalnog zaposlenja" — "fractional" does not parse for a Croatian mid-market buyer.
- Prices are identical to the EN page and stay that way. The Croatian budget problem is solved through co-financing and EDIH routes, not discounting.

All four are single-page layouts defined entirely via YAML frontmatter `sections`. Each section has a `type` field that maps to a local `_includes/` override. Editing the site means editing these four files.

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

## Frontend assets

There is no jQuery, no Bootstrap JS, no Font Awesome, and no CDN dependency except Google Fonts. That is deliberate — do not reintroduce them.

- **JS** is one local file, `assets/js/site.js`: mobile nav toggle, navbar-scrolled class, and IntersectionObserver nav highlighting. It replaced the theme's `creative.js`, which pulled in jQuery, Bootstrap's bundle, `jquery-easing` (for `easeInOutExpo`) and `magnific-popup` (for a `#portfolio` lightbox this site does not have).
- **Testing scroll behaviour in the browser tool**: programmatic `window.scrollTo` dispatches no scroll events and `IntersectionObserver` never fires inside iframe probes, so anything scroll-driven reads as broken there. Use the `computer` scroll action (real input events) on a top-level page instead, and force `scroll-behavior: auto` first — smooth scrolling is suppressed when the window is unfocused.
- **The sticky CTA is visible by default and hidden by a class.** Do not switch it to the `hidden` attribute: the UA stylesheet's `[hidden] { display: none }` beats a class-level `display` rule and kills the slide transition, and default-visible degrades correctly without JS.
- **Anchor scrolling is CSS, not JS**: `scroll-behavior: smooth` plus `[id] { scroll-margin-top: 72px }` in `main.scss`. This also fixes cold loads on a URL like `/#work`, which script-driven scrolling never handled. Don't move it back into JS.
- **Icons** are an inline SVG sprite, `_includes/icon-sprite.html`, injected once at the top of `<body>` and referenced as `<svg class="icon"><use href="#fa-brain"/></svg>`. Symbol ids match the `fa-*` names already used in front matter. Regenerate with `python3 tools/build-icon-sprite.py` after adding an icon — add it to the `ICONS` dict first. Inline rather than an external sprite file because Safari does not support cross-file `<use href="sprite.svg#id">`.
- Inter is loaded by a single non-blocking `<link>` in `base.html`. Do not add a CSS `@import` for it in `main.scss` — that fetches it twice and blocks rendering.

## Page flow

The advisory page order is deliberate and follows the order buyers ask questions:
`clients → fit → packages → proof → who → process → readiness → faq → crosslink → contacts`.
Proof sits immediately after the prices it justifies, and `who` right after it because for a
solo consultancy the person is the product. Both were four screens further down before.

Backgrounds must keep alternating (subtle / white / subtle / white / dark …) — check the
neighbours before adding `background_style: bg-subtle` to a new section.

`header.proof` renders a chip strip under the hero CTA. It exists so the published price is
visible at the fold; without it the first price is ~3 screens down.

Sections are sized with padding, not `min-height: 80vh`. The old min-heights stretched ~450px
of content into 720px boxes, costing ~500px of dead space per page.

Keep the Calendly CTA count low. It is on the featured package only, plus the nav button, the
readiness result and the contact section. Five identical "Book an intro call" links inside one
section gave the reader no signal about which to click.

## Accessibility

Every page has a `<main id="main">` landmark and a skip link (`.skip-link`, off-screen until
focused). Touch targets are forced to 44px minimum below 992px — nav, footer, contact chips,
FAQ summaries, package CTAs and the badge links were all under it.

All body text meets WCAG AA (4.5:1). The greys are chosen for it: `#5b6b81` is the lightest grey that passes on white, `#f8fafc` and `#f1f5f9` alike, and `#15803d` is the green that passes on the `#f0fdf4` chip background. `#94a3b8` and `#16a34a` both fail — don't reach for them. On the navy sections, white text needs at least 0.5 alpha. Public sector procurement in the EU can require conformance, and that is a target segment.

**`_config.yml`** holds global settings: site title, nav title, URL, OG image, social links, plugin config.

**`_data/menus.yml`** controls nav links, keyed by menu name then language. `header` is the homepage menu; `advisory` is the advisory-page menu. A page selects one with `nav_menu: <key>` (defaults to `header`) and its language with `lang`. The last item in a list renders as a primary CTA button; "Book a Call" is appended separately in `_includes/nav.html` and its label/URL can be overridden per page with `nav_cta_label` / `nav_cta_url`. Set `highlight: true` on an item to accent it.

Anchor-only URLs (`#work`) are emitted bare and get the theme's smooth scroll; everything else goes through `relative_url`. Do not pipe `#foo` through `relative_url` — it becomes `/#foo` and jumps to the homepage from any subpage.

**`_data/footer.yml`** contains the footer copyright string.

The `_site/` directory is build output — never edit it directly, it's gitignored.

## Local Overrides

All layout/include overrides live locally and take precedence over the remote theme:

| File | Purpose |
|------|---------|
| `_layouts/base.html` | Font (Inter), JSON-LD schema, deferred JS, active nav JS |
| `_layouts/home.html` | Removes text-uppercase from hero h1, adds hero subtitle |
| `_includes/nav.html` | Per-page menu selection, two CTA buttons, anchor-safe hrefs |
| `_includes/about.html` | Two-column layout with photo, badges, tech stack |
| `_includes/services.html` | Service cards with icon circles (`text` is markdownified, so links work) |
| `_includes/case-studies.html` | Case study cards with outcome chips |
| `_includes/certifications.html` | Cert chips, supports optional `url` for links |
| `_includes/contact.html` | Dark section with contact buttons; `watermark` sets the giant background word |
| `_includes/footer.html` | Two-column: copyright left, links right |
| `_includes/packages.html` | Priced offer cards + OfferCatalog JSON-LD. `featured: true` = full width, accent border, two-column deliverables |
| `_includes/fit.html` | Two-column "good fit / not a fit" qualification lists |
| `_includes/process.html` | Numbered engagement timeline with connector line |
| `_includes/readiness-check.html` | Self-scoring checklist, client-side only, banded verdict at <40% / <75% / ≥75% |
| `_includes/testimonials.html` | Quote cards. **Renders nothing until real `quotes` are supplied** — never invent them |
| `_includes/crosslink.html` | Full-width band linking the engineering and advisory tracks. `variant: dark` available, but place a light band between a light and a dark section so it reads as its own block |
| `_includes/clients.html` | Client name chips. Takes `clients[]` of `{ name }` |
| `_includes/faq.html` | Native `<details>` accordion + FAQPage JSON-LD. No JS; answers stay crawlable while collapsed |

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

Certs use `name` + optional `url` object pairs (not plain strings):

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

## Pricing on the advisory page

Prices are "from €X" anchors, deliberately. They filter unqualified enquiries and signal a productized practice rather than hourly work. Keep them; do not soften to "price on enquiry". Current ladder: Workshop €1,500 · Assessment €10,000 · Proof of Value €30,000 · Fractional €5,000/mo · Training €4,000.

The assessment's fee-credit offer (credited in full against a build booked within 90 days) is the mechanism that converts assessments into builds. Keep it prominent.

## To Do

- **Croatian proofread** — the Croatian copy was written by Claude, not by a native speaker, and has not been reviewed by Ivan. Proofread before promoting `/hr/` anywhere.
- **Testimonials** — highest impact remaining content gap. The `testimonials.html` include and a commented-out section block are already in `ai-advisory.md` and `hr/ai-savjetovanje.md`; uncomment and fill in 2-3 verbatim quotes from LinkedIn recommendations. Never invent quotes.
- **Case study numbers** — outcome chips are qualitative. Any that Ivan can back with a real figure (hours saved, cost reduced, time to market) should be restated in money, especially on the advisory page.
- **Blog / thought leadership** — write for buyers, not engineers. Suggested topics: what a production RAG system costs to run for a year; why the first AI use case should be boring; keeping AI inside the perimeter under EU data residency.
- **Homepage services** — still 8 cards organized by technology. Fine for the engineering audience, but worth collapsing to 4-5 organized by problem if the homepage ever needs to work harder.
- **Five unanswered FAQ questions** — the FAQ on both advisory pages ships with seven answered questions and five stubbed out in comments at the bottom of the `faq.html` section block: NDA/DPA, professional indemnity insurance, IP ownership, payment terms, and third-party AI tooling on client material. These are the ones enterprise procurement asks last and that most often stall a deal. Only Ivan can answer them — **do not invent answers**. When filling them in, translate into `hr/ai-savjetovanje.md` at the same time.

## Sourcing facts about Ivan

`/Users/ip/Projects/cv/ip` holds the CV repo. `README.md` there is the most current consolidated summary; `resume/*.tex` has per-engagement detail, and `prlic-consulting-company-presentation.html` has the company boilerplate including OIB 84570551730. Use those rather than inferring. Facts already mined into the site: SOC 2 / financial-grade work at Q.ai, the Metro / Ricoh / TUI team-collaboration examples, company registration details, and the client list.

Note the CV contains **no quantified outcomes** — no percentages, cost reductions, or timings — which is why the case-study chips remain qualitative.
