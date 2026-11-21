---
title: "Migrating from WordPress to GitHub Pages: A Practical Guide"
date: 2026-11-21
slug: wordpress-to-github-pages
url: /wordpress-to-github-pages/
canonical: /wordpress-to-github-pages/
categories:
  - meta
tags:
  - wordpress
  - github-pages
  - hugo
  - migration
  - static-site
author: "Eric Ma"
authors: [zma]
---

We migrated SysTutorials — 1,346 blog posts plus 56,253 Linux man pages — from WordPress to a Hugo static site on GitHub Pages. The result: a single binary, single config, single CI job that builds in ~8 seconds (down from 12 minutes), zero URL drift, free hosting, and a completely static attack surface with no PHP, no database, and no plugin stack to maintain.

## Why migrate from WordPress to a static site on GitHub Pages

### Maintenance burden eliminated

Running WordPress means constant upgrades (core, plugins, themes), backups, database monitoring, PHP version management, and server patching. A static site on GitHub Pages removes all of that:

- **No upgrades** — Hugo is a single binary; updates are a one-line change in CI
- **No database** — content is Markdown files in git; backups are `git push`
- **No monitoring** — GitHub handles uptime, DDoS protection, and TLS
- **No server costs** — GitHub Pages is free for public repos

### Security: the final push

Running WordPress means running a full **PHP stack** — and that stack has been under relentless attack. Between Q3 2025 and today, the combined vulnerability surface across WordPress core, plugins, themes, and PHP itself made the risk untenable.

**The compounding risk:** A WordPress site exposes PHP runtime, WordPress core (1M+ lines of PHP), 60k+ plugins/themes (frequent supply-chain compromises like Gravity Forms, WP Fastest Cache, LiteSpeed Cache), web server config, MySQL database, and the OS kernel — all simultaneously.

**Recent critical examples (2024–2025):**
- **WordPress plugins:** Wordfence RCE series (1M+ sites), GutenKit/Hunk Companion arbitrary file upload, Fluent Forms RCE via contact form, Elementor Pro broken access control → RCE
- **PHP runtime:** CVE-2024-4577 (CGI argument injection → RCE), CVE-2024-11236 (phar deserialization → RCE), CVE-2024-8925 (mbstring heap overflow)
- **Infrastructure:** OpenSSH regreSSHion (CVE-2024-6387, unauthenticated RCE as root), Linux kernel netfilter/nftables privilege escalation

**Static sites eliminate the entire PHP+WordPress+plugin+database stack.** The only remaining surface is the CDN (GitHub Pages) serving static HTML/CSS/JS — no interpreter, no database, no plugin architecture, no dynamic code execution.

## Why Hugo over Jekyll

We originally ran Jekyll on GitHub Pages. Hugo won for four reasons:

1. **Build speed** — ~8 seconds vs 12 minutes for 57k pages. Hugo's parallel rendering and single-binary architecture scale linearly; Jekyll's Ruby pipeline does not.

2. **No Ruby dependency** — GitHub Pages' Jekyll version is pinned and lags. Hugo is a single binary we control; upgrades are a one-line CI change.

3. **Module mounts** — Merging the separate man-site (56k pages) into the main repo required Hugo's `[module.mounts]`. Jekyll has no equivalent; we'd need artifact merging across repos.

4. **Taxonomy & permalink parity** — Hugo's `[permalinks]` and `[taxonomies]` config mirrors WordPress's `/category/slug/` and `/author/slug/` exactly. Jekyll needs plugins for the same.

## How to migrate: step-by-step

This is the exact process we used for **SysTutorials** (1,346 posts, ~56k Linux man pages).

### 1. Export from MariaDB/MySQL

WordPress stores everything in MySQL/MariaDB. We used a direct database dump instead of the WXR export — it gives full control over every field and avoids XML parsing issues.

```bash
# Dump the WordPress database
mysqldump -u wp_user -p wp_database > wp_dump.sql

# Or if using a managed host, use their backup tool to get a .sql file
```

Then extract the key tables:

- `wp_posts` — all posts, pages, revisions, attachments
- `wp_postmeta` — custom fields (canonical URLs, SEO data, etc.)
- `wp_terms`, `wp_term_taxonomy`, `wp_term_relationships` — categories/tags
- `wp_users`, `wp_usermeta` — authors
- `wp_options` — site settings (home URL, etc.)

### 2. Convert database rows to Markdown with front matter

We wrote a Python script that reads the SQL dump (via `mysql-connector-python` or by loading into a local MariaDB instance) and:

- Iterates `wp_posts` where `post_type = 'post'` and `post_status = 'publish'`
- Converts `post_content` (HTML) → Markdown using `html2text` with custom rules
- Extracts `post_title`, `post_date`, `post_author`, `post_name` (slug)
- Joins `wp_term_relationships` → categories/tags
- Reads `_yoast_wpseo_canonical` (or equivalent SEO plugin field) from `wp_postmeta` for the canonical URL
- Writes each post as `content/posts/YYYY-MM-DD-slug.md` with full front matter

```python
# Key: canonical URL becomes Hugo's url: front matter
# This guarantees zero URL drift
front_matter["url"] = front_matter["canonical"]
```

### 3. Clean the Markdown

WordPress content contains shortcodes (`[gallery]`, `[caption]`, etc.), inline styles, and HTML that won't render in Hugo. Strip or convert them:

```bash
# Remove WordPress shortcodes
sed -i 's/\[caption.*\]//g' *.md
sed -i 's/\[\/caption\]//g' *.md
# Convert [gallery] to simple markdown lists
# ... custom rules per site
```

### 4. Organize content structure

```
content/
  posts/           # all blog posts (YYYY-MM-DD-slug.md)
  _index.md        # home page
  archive/         # year/month archives (auto-generated by Hugo)
  tools/           # static tool pages (e.g., BBCode editor)
  man/             # mounted from man-src/ (see step 7)
data/
  authors.yml      # author slug → display name
  topics.yml       # category taxonomy metadata
static/
  files/           # uploaded assets (images, PDFs)
  docs/linux/man/man.css
```

### 5. Configure Hugo taxonomies and permalinks

`hugo.toml` key sections:

```toml
[taxonomies]
  category = "categories"
  author = "authors"

[permalinks.term]
  categories = "/category/:slug/"
  authors = "/author/:slug/"

[frontmatter]
  lastmod = ["modified", "date"]
```

This mirrors WordPress's `/category/slug/` and `/author/slug/` URLs exactly.

### 6. Preserve canonical URLs for every post

Every post **must** have both `url:` and `canonical:` in front matter:

```yaml
---
title: "Post Title"
date: 2026-01-15
url: /my-canonical-slug/
canonical: /my-canonical-slug/
---
```

The `url:` field tells Hugo where to render the page. The `canonical:` field is used in `<link rel="canonical">` and Open Graph tags. We derived both from the original WordPress permalink (stored in `wp_postmeta` by the SEO plugin).

### 7. Merge separate sites with module mounts

SysTutorials had a separate `man-site/` Hugo instance for ~56k Linux man pages. We merged it into the main site:

```toml
[module]
  [[module.mounts]]
    source = "man-src"
    target = "content/man"
```

Now one `hugo --minify` builds everything. The man pages keep their `/docs/linux/man/` URLs.

### 8. Sitemaps and feeds

- **Blog sitemap**: custom template at `layouts/sitemap.xml` (excludes `/docs/`)
- **Man sitemap**: chunked index via `scripts/gen-man-sitemap.py` (50k URL limit per file)
- **Atom feed**: `layouts/index.feed.xml` from 10 most recent posts

Fix: the man sitemap index had a bug pointing to `/docs/docs/sitemap-N.xml` — corrected to `/docs/sitemap-N.xml`.

### 9. CI/CD: one build step

GitHub Actions workflow (`.github/workflows/pages.yml`):

```yaml
- uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: 'latest'
- run: python3 scripts/gen-man-page-length.py man-src data
- run: hugo --minify
- run: python3 scripts/gen-man-sitemap.py public/docs public/docs
- run: touch public/.nojekyll
```

**Result**: ~8 seconds vs 12 minutes previously. No Ruby, no Jekyll, no artifact merging.

## Tools and configuration summary

| Tool | Purpose |
| --- | --- |
| Hugo (extended) | Static site generator |
| Python + MariaDB connector | DB dump → Markdown conversion |
| GitHub Actions | CI/CD (free for public repos) |
| GitHub Pages | Hosting (free, TLS, CDN) |
| Git | Version control + backup |

Key config files to copy/adapt:

- `hugo.toml` — site config, taxonomies, permalinks, module mounts
- `layouts/_default/baseof.html` — site chrome (header, footer, GA4, ads)
- `layouts/posts/single.html` — post template (breadcrumbs, meta, ads)
- `layouts/_default/term.html` — category/author listing pages
- `data/authors.yml` — author slug → display name mapping
- `data/topics.yml` — category metadata (title, academy, path)
- `scripts/gen-man-sitemap.py` — chunked sitemap for >50k URLs
- `.github/workflows/pages.yml` — CI pipeline

## AI-assisted migration

This entire migration was driven by **OpenCode** with **GLM 5.3 / 5.3-Flash** (via Z.AI's coding plan). The AI handled:

- MariaDB parsing and Markdown conversion logic
- Hugo template porting from Jekyll originals (1:1 visual parity)
- Taxonomy and permalink configuration
- URL parity verification (1,447 URLs matched exactly)
- Internal link audit across 57k pages
- Sitemap/feed parity checks
- PR authoring and conflict resolution

Human role: strategic decisions (URL structure, taxonomy design), final review, and `gh pr create`.

## Result: SysTutorials on GitHub Pages

- **1,346 posts**
- **56,253 man pages** in the same build
- **Single binary, single config, single CI job**
- **Zero URL drift** — all canonical URLs preserved from the MariaDB export
- **Free hosting, zero server maintenance, static security**

The site is live at [systutorials.com](https://www.systutorials.com) — this very post you're reading is served from the Hugo + GitHub Pages stack.

---

*This post documents the migration that landed in PR [#62](https://github.com/nv2n1/nv2n1.github.io/pull/62). The blog post itself was added in PR [#66](https://github.com/nv2n1/nv2n1.github.io/pull/66).*

To leave comments or report issues, please create a PR or report an issue at [https://github.com/nv2n1/nv2n1.github.io](https://github.com/nv2n1/nv2n1.github.io).