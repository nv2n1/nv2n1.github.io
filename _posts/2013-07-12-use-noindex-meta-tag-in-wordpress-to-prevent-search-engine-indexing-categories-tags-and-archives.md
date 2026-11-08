---
title: "How to Add noindex Meta Tags to WordPress Archives"
date: 2013-07-12 16:46:10 +0000
layout: post
canonical: https://www.systutorials.com/use-noindex-meta-tag-in-wordpress-to-prevent-search-engine-indexing-categories-tags-and-archives/
---

WordPress automatically generates archive pages, category listings, tag pages, and author archives. While these pages serve users browsing your site, they often contain duplicate or thin content that clutters search results. The `noindex` meta tag prevents search engines from indexing these secondary pages while still allowing them to crawl and follow links.

## How noindex Works

When a search engine like Google encounters `noindex` on a page, it removes that page from search results but continues crawling the page to discover links. This differs from `robots.txt` with `Disallow:`, which prevents crawling entirely. For WordPress archives, `noindex,follow` is typically the right choice — you want Google to follow links to your actual posts without listing the archive page itself.

## Adding noindex via Theme Functions (Recommended)

The most reliable approach works across all theme types and survives updates. Add this to your theme’s `functions.php` or a custom plugin:

``` php
add_action( 'wp_head', function() {
    if ( is_author() || is_date() || is_search() || is_category() || is_tag() ) {
        echo '<meta name="robots" content="noindex,follow">' . "\n";
    }
});
```

If you’re using a child theme, place this code in `wp-content/themes/your-child-theme/functions.php`. This survives parent theme updates.

For block themes that may not have a traditional `header.php`, the hook method above is essential.

## Selective noindex Rules

You can target specific archive types instead of blocking all of them. For example, to index category archives but block tag archives:

``` php
add_action( 'wp_head', function() {
    if ( is_author() || is_date() || is_search() || is_tag() ) {
        echo '<meta name="robots" content="noindex,follow">' . "\n";
    }
});
```

To block only specific category IDs (useful for housekeeping categories):

``` php
add_action( 'wp_head', function() {
    if ( is_category( array( 3, 7, 15 ) ) ) {
        echo '<meta name="robots" content="noindex,follow">' . "\n";
    }
});
```

Block author archives but allow everything else:

``` php
add_action( 'wp_head', function() {
    if ( is_author() ) {
        echo '<meta name="robots" content="noindex,follow">' . "\n";
    }
});
```

## Using SEO Plugins

If you prefer not to edit code, most modern SEO plugins provide GUI controls:

- **Yoast SEO**: Settings → Search Appearance → Archives. Toggle noindex for each archive type.
- **Rank Math**: Settings → Titles & Meta → Archives. Configure per-archive settings.
- **All in One SEO**: Search Appearance → Archives. Select which types to noindex.

Plugin-based approaches are more user-friendly and survive theme updates, though they add a small performance cost.

## Verifying Implementation

After adding noindex tags, confirm they’re present:

``` bash
curl -s https://yoursite.com/category/example/ | grep -i "noindex"
```

This should return the meta tag if correctly implemented.

For larger verification, use Google Search Console:

1.  Go to **Indexing** → **Coverage**
2.  Filter by “Excluded” pages
3.  Look for pages with “Blocked by noindex” status
4.  This typically takes 3-7 days after implementation

You can also verify in your browser’s developer tools. Open a category page, press F12, and search the `<head>` section for `noindex`.

## Performance and Link Equity Considerations

Using `noindex,follow` preserves internal link equity — your site’s authority still flows through archive pages to individual posts. This is better than blocking with `robots.txt`, which prevents crawling entirely and can waste crawl budget on pages you don’t want indexed anyway.

If an archive page is truly low-value, consider whether you need it at all. WordPress tag archives with a single post or empty pagination aren’t useful for users either. In these cases, disabling tag archives entirely via `register_taxonomy()` arguments may be cleaner.

## Common Pitfalls

- **Using bitwise OR (`|`) instead of logical OR (`||`)** in conditionals will cause syntax errors. Always use `||`.
- **Placing code before `wp_head()`** means your tag won’t output. Use the `wp_head` hook to guarantee execution.
- **Forgetting to clear caches** — if you use a page cache or CDN, flush caches after implementing noindex so Google sees the updated headers.
- **Mixing plugin and code solutions** — avoid adding noindex both via Yoast and functions.php, which can create conflicts.

## Testing Before Deployment

If you’re uncertain about which archives to block, test on a staging site first. Monitor Google Search Console for a week to see which archive pages currently receive traffic. You may find that some archives (like year-based archives on an active blog) are actually valuable to users and worth indexing.
