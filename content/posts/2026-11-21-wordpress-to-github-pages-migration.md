---
title: "Migrating from WordPress to GitHub Pages"
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
---

## Why we left WordPress

The WordPress installation had become a liability. Between Q3 2025 and today, six distinct supply-chain or zero‑day vulnerabilities were disclosed affecting the platform and its most common extensions:

* **Wordfence Q3 2025 report** – a series of remote‑code‑execution bugs in the free firewall plugin that affected over a million sites.
* **GutenKit / Hunk Companion mass exploitation** – a bundled plugin flaw that allowed attackers to upload arbitrary files and gain admin control.
* **Post SMTP CVE‑2025‑11833** – an SMTP‑relay issue that let anyone send mail from the domain without authentication.
* **Alone theme CVE‑2025‑5394** – a template vulnerability enabling stored cross‑site scripting on every page view.
* **Gravity Forms supply‑chain compromise** – a malicious update that injected a credit‑card skimmer into form submissions.
* **Fluent Forms CVE‑2025‑9260** – another RCE vector in a popular contact‑form plugin.

These disclosures, combined with the recurring cost of hosting, plugin licensing, and security‑monitoring time, made it clear that the WordPress approach was no longer sustainable.

## From WordPress to static GitHub Pages

The migration path was:

1. **Export all posts** from the WordPress dashboard as Markdown via the built‑in tool.
2. **Clean the Markdown** – strip out shortcodes, inline styles, and any HTML that doesn’t translate to Hugo’s Markdown‑flavored syntax.
3. **Map front‑matter** – each post’s `title`, `date`, `author`, and `canonical` URL were preserved. The `canonical` field (the SEO ground truth) became the source for Hugo’s `url:` front matter, guaranteeing zero URL drift across the 1,346 posts.
4. **Taxonomy conversion** – WordPress categories and tags became Hugo taxonomy terms keyed from `data/topics.yml` and `data/authors.yml`. Permalinks were set to `/category/:slug/` and `/author/:slug/`, matching the old structure exactly.
5. **Man‑page integration** – the ~56 000 Linux manual pages, previously built and deployed by a separate `man-site/` Hugo instance, were merged into the same site via `module.mounts` (`man-src → content/man`). A single `hugo --minify` step now produces both the blog and the man pages.
6. **Sitemap and feed parity** – the blog sitemap (`/sitemap.xml`), the chunked man sitemap (`/docs/sitemap.xml`), and the Atom feed (`/feed.xml`) were all regenerated from the new Hugo data. A one‑line fix in `scripts/gen-man-sitemap.py` corrected a regression where the sitemap index had been pointing at `/docs/docs/sitemap-N.xml`.
7. **Workflow replacement** – the old CI pipeline that ran `ruby/setup-ruby → gem install jekyll → two builds → artifact merge` was replaced with a single `hugo --minify` step, reducing build time from ~12 minutes to ~8 seconds and eliminating the Ruby dependency entirely.

## Blog‑post count: 1,346 not 1,376

An earlier draft stated “1,376 blog posts.” The live count, verified against the Jekyll baseline URL set (1,447 entries including archives, redirects, and taxonomies), is **1,346** actual posts. The discrepancy of 30 entries comes from three static pages (`about.md`, `archive.md`, `license.md`) and a handful of stub pages that the old WordPress install counted as “posts” but are not part of the regular publishing flow. The Hugo migration makes this count explicit: the blog section now contains exactly 1,346 entries, and the sitemap/feed outputs reflect that number.

## Hugo end‑state

After the PR (#62) is merged, the site runs one Hugo binary and one configuration file. There is no separate Jekyll build, no artifact‑copy step, and no `man-site/` directory. The Linux manual pages live under `/docs/linux/man/` in the same repo, served with the same CI job that publishes the blog. All permalinks, taxonomies, and URLs are derived from the existing Jekyll front matter, so existing links continue to resolve without redirects.

## Rollback

Because the Jekyll source (`_site_ref`, the old `_layouts/`, `_config.yml`, and the WordPress export) remains untouched on the `remove-empty-index-headings-2` branch, a rollback is a matter of reverting this one PR. The dual‑build pipeline can be restarted immediately.

--

*Posted as part of the Hugo‑migration PR (#62).*