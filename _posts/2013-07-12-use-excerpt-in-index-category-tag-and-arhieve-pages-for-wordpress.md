---
title: "Display Post Excerpts Instead of Full Content on WordPress Archives"
date: 2013-07-12 16:46:09 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /use-excerpt-in-index-category-tag-and-arhieve-pages-for-wordpress/
---

By default, WordPress displays full post content on index, category, tag, archive, and search pages. This duplicates content across multiple URLs, dilutes SEO value, slows page rendering, and forces readers to scroll through complete posts when they’re just scanning headlines.

Using excerpts instead improves page load times, reduces crawl budget waste, consolidates ranking signals to your canonical post URLs, and encourages click-through to full articles.

## Why excerpts matter

Search engines treat identical content on multiple URLs as potential duplication. Archive pages with full post bodies signal low-value content to crawlers, fragmenting ranking power across pages instead of concentrating it on single post URLs. This wastes crawl budget and compounds the problem on sites with deep archives.

Excerpts also reduce page weight significantly. A blog with 10 posts rendered in full might exceed 2MB. The same archive with excerpts typically stays under 300KB. This improves Core Web Vitals—particularly Largest Contentful Paint (LCP)—and benefits mobile users with slower connections.

## How WordPress generates excerpts

WordPress creates excerpts using this priority:

1.  **Custom excerpt** — explicitly set in the post editor’s excerpt field
2.  **Auto-generated excerpt** — first 55 words of post content, ending with `[...]`

The default `[...]` terminator isn’t functional. Most sites replace it with a clickable “Read More” link for better UX and conversion rates.

## Finding the right template

Locate your active theme:

``` bash
ls -la wp-content/themes/
```

WordPress uses this template hierarchy for listings:

- `home.php` — blog index (highest priority)
- `index.php` — fallback for any listing
- `archive.php` — category, tag, date, custom post type archives
- `search.php` — search results

If a specific template doesn’t exist, WordPress falls back to the next option. Verify which template is active by checking template debug information:

``` bash
grep -n "the_content" wp-content/themes/your-theme/*.php
```

This shows every file calling `the_content()`, which you’ll need to modify.

## Implementing excerpts in templates

Replace `the_content()` calls with a conditional that shows full content only on single posts:

``` php
<?php 
if ( is_singular() ) {
    the_content();
} else {
    the_excerpt();
    ?>
    <p>
        <a href="<?php the_permalink(); ?>" class="read-more">
            Continue reading: <?php the_title(); ?> &raquo;
        </a>
    </p>
    <?php
}
?>
```

The `is_singular()` conditional returns true only for single posts and pages. It returns false for archives, categories, tags, and search results, triggering the excerpt instead.

Apply this change to all template files containing `the_content()`:

``` bash
grep -l "the_content" wp-content/themes/your-theme/home.php wp-content/themes/your-theme/archive.php wp-content/themes/your-theme/index.php
```

Check each returned file and apply the conditional.

## Customizing excerpt length

The default 55-word excerpt may not fit your design. Add this to `functions.php`:

``` php
function custom_excerpt_length( $length ) {
    return 20; // Adjust to your preferred word count
}
add_filter( 'excerpt_length', 'custom_excerpt_length' );
```

Target 15–30 words for most layouts. Test on actual devices to ensure excerpts don’t cause layout shift on mobile screens.

## Styling the excerpt terminator

Replace the default `[...]` with a styled link:

``` php
function custom_excerpt_more( $more ) {
    return ' <a href="' . get_permalink() . '" class="read-more-link">&raquo; Read More</a>';
}
add_filter( 'excerpt_more', 'custom_excerpt_more' );
```

Add CSS to your stylesheet:

``` css
a.read-more-link {
    font-weight: bold;
    color: #0073aa;
    text-decoration: none;
    display: inline-block;
    margin-top: 0.5rem;
}

a.read-more-link:hover {
    text-decoration: underline;
}
```

## Custom post types

If your site uses custom post types, enable excerpt support:

``` php
function enable_excerpts_for_custom_types() {
    add_post_type_support( 'my_custom_type', 'excerpt' );
}
add_action( 'init', 'enable_excerpts_for_custom_types' );
```

Run this once, then verify excerpts appear in the post editor for that type.

## Best practices

**Hand-write important excerpts.** Auto-generated excerpts cut sentences mid-word and lose context. High-priority posts need custom excerpts that control messaging, include target keywords naturally, and compel clicks.

**Keep length consistent.** Decide on a target length (15–30 words) and document it for your editorial team. Visual consistency improves scannability on archive pages.

**Use keywords strategically.** Authors should naturally work target keywords into custom excerpts. This signals relevance to search engines without appearing forced.

**Test on mobile.** Use Chrome DevTools to preview how excerpts wrap on screens under 768px. Ensure “Read More” links don’t break awkwardly or cause layout shift.

**Monitor Core Web Vitals.** Check Google Search Console or Lighthouse before and after this change. You should see improvements in LCP and reductions in Cumulative Layout Shift (CLS).

**Verify Search Console.** After deploying, check Google Search Console for crawl errors or indexation issues. The change should reduce crawl depth and improve overall budget allocation.

## Expected outcomes

This approach prevents search engines from treating archive pages as duplicate content. Google concentrates crawl budget on unique content and consolidates ranking signals to canonical post URLs. Users see cleaner, faster-loading archives and explicitly choose posts they want to read.

Most sites see Core Web Vitals improvements within 2–4 weeks. Monitor Search Console and Google Analytics to measure the impact on your traffic and engagement metrics.
