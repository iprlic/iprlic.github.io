# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
bundle install              # Install dependencies
bundle exec jekyll serve    # Run local dev server with live reload
bundle exec jekyll build    # Build to _site/
```

## Architecture

This is a Jekyll static site deployed to GitHub Pages at `prlic.io` (CNAME). It uses a remote theme (`iprlic/creative-theme-jekyll-new` via `jekyll-remote-theme` plugin), so layout and styling files are not present locally.

**Content is almost entirely in `index.md`** — the homepage is a single-page site defined via YAML frontmatter sections (hero, services, CTA, contact). Editing the site means editing this file.

**`_config.yml`** holds global settings: site title/URL, Google Analytics ID, social links, and plugin configuration.

**`_data/footer.yml`** contains the footer copyright string.

The `_site/` directory is build output — never edit it directly, it's gitignored.

## Key Details

- Ruby version: 2.6.5 (see `.ruby-version`)
- Jekyll ~4.2.2, minima theme ~2.5.1
- Plugins: jekyll-feed, jekyll-sitemap, jekyll-seo-tag, jekyll-remote-theme
- No blog posts currently exist under `_posts/`
