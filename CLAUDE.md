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

**Content is almost entirely in `index.md`** — the homepage is a single-page site defined via YAML frontmatter sections. Each section has a `type` field that maps to a local `_includes/` override. Editing the site means editing this file.

**`_config.yml`** holds global settings: site title, nav title, URL, OG image, social links, plugin config.

**`_data/menus.yml`** controls nav links. The last item renders as a primary CTA button; "Book a Call" is hardcoded in `_includes/nav.html` as a second button.

**`_data/footer.yml`** contains the footer copyright string.

The `_site/` directory is build output — never edit it directly, it's gitignored.

## Local Overrides

All layout/include overrides live locally and take precedence over the remote theme:

| File | Purpose |
|------|---------|
| `_layouts/base.html` | Font (Inter), JSON-LD schema, deferred JS, active nav JS |
| `_layouts/home.html` | Removes text-uppercase from hero h1, adds hero subtitle |
| `_includes/nav.html` | Nav with two CTA buttons (Contact + Book a Call) |
| `_includes/about.html` | Two-column layout with photo, badges, tech stack |
| `_includes/services.html` | Service cards with icon circles |
| `_includes/case-studies.html` | Case study cards with outcome chips |
| `_includes/certifications.html` | Cert chips, supports optional `url` for links |
| `_includes/contact.html` | Dark section with contact action buttons |
| `_includes/footer.html` | Two-column: copyright left, links right |

## Styling

- `assets/css/main.scss` — all custom CSS. Compiled by Jekyll.
- Design: dark navy (`#0f172a`) + blue (`#2563eb`), Inter font
- Bootstrap 4.5 is loaded via the theme — use Bootstrap grid/utilities freely
- CSS specificity: Bootstrap uses `!important` heavily. Use `#section-id .class` selectors or `!important` overrides when fighting Bootstrap rules.
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

## To Do

- **Testimonials** — highest impact remaining content gap. Pull 2-3 quotes from LinkedIn recommendations. Add a `testimonials.html` include and new section in `index.md`.
- **Blog / thought leadership** — even 1-2 articles would help rank beyond the name. Suggested topics: RAG architecture on Bedrock, Fractional CTO for startups, multi-cloud trade-offs.
