---
title: "WordPress Twenty Thirteen: Using Excerpts on Archive Pages"
date: 2018-03-24 08:17:50 +0000
modified: 2026-04-12 14:18:44 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /excerpt-in-homepage-category-tag-and-author-pages-for-wordpress-theme-twenty-thriteen/
---

WordPress Twenty Thirteen theme shows full post content on archive pages by default. Using excerpts instead keeps archive pages clean and improves page load speed by showing just a summary of each post.

## Enable Excerpts on Archive Pages

Add this to your theme’s `functions.php` or a custom plugin:

```wp-block-code
function twentythirteen_excerpts_on_archives($content) {
    if (is_archive() || is_home()) {
        return the_excerpt();
    }
    return $content;
}
add_filter('the_content', 'twentythirteen_excerpts_on_archives');
```

Or modify the archive template directly. Edit `archive.php` and replace `the_content()` with `the_excerpt()`:

```wp-block-code
// In archive.php, find:
<?php the_content(); ?>

// Replace with:
<?php the_excerpt(); ?>
```

## Custom Excerpt Length

Control how many words the excerpt displays:

```wp-block-code
// Set excerpt length to 30 words
function custom_excerpt_length($length) {
    return 30;
}
add_filter('excerpt_length', 'custom_excerpt_length');

// Change the [...] to a read more link
function custom_excerpt_more($more) {
    return '... <a href="' . get_permalink() . '">Continue reading →</a>';
}
add_filter('excerpt_more', 'custom_excerpt_more');
```

## Manual Excerpts

WordPress supports two types of excerpts:

- **Auto-generated** — WordPress takes the first 55 words of the post and adds \[…\] at the end
- **Manual** — You write a custom summary in the Excerpt meta box on the post editor screen

To enable the Excerpt meta box: Screen Options (top right of post editor) → check “Excerpt”. Write a hand-crafted summary for important posts.

## Using the WordPress REST API

For headless WordPress setups, the REST API returns both rendered and plain text excerpts:

```wp-block-code
// GET /wp-json/wp/v2/posts
{
    "excerpt": {
        "rendered": "<p>Post summary text...</p>\n",
        "protected": false
    }
}
```

Use the `excerpt.rendered` field for display in your frontend application.

## Excerpts vs Read More Tag

Two different approaches to truncating content:

- **Excerpts** — Automatic or manual summaries, stripped of HTML formatting, consistent length across all posts
- **Read More tag** — Manual placement with `<!--more-->` in the editor, preserves HTML formatting, shows the content up to the tag

For archive pages, excerpts are generally better because they’re consistent in length and don’t break layouts with unexpected HTML.

## Adding Featured Images to Excerpts

Display a thumbnail alongside each excerpt:

```wp-block-code
function excerpt_with_thumbnail() {
    if (has_post_thumbnail()) {
        echo '<div class="excerpt-thumb">';
        the_post_thumbnail('thumbnail');
        echo '</div>';
    }
    the_excerpt();
}
```

Style the thumbnail with CSS to float it left or right of the excerpt text.

## Modern Theme Approaches (2026)

If you’re using a block theme (Full Site Editing), use the Query Loop block with Post Excerpt blocks instead of modifying PHP templates. The block editor provides built-in excerpt display options without code changes.

For classic themes still in use, the PHP approach above works on Twenty Thirteen and most other themes derived from it.

## Performance Benefits of Excerpts

Using excerpts on archive pages significantly improves page load times. Full post content on archive pages means loading all images, embedded videos, and shortcodes for every post on the page. With 10 posts per page, that can mean loading dozens of images the user never scrolls to see.

Excerpts strip all HTML and media, resulting in much smaller page sizes. For a site with 1,000+ posts, the bandwidth savings are substantial. Users on mobile connections particularly benefit from the reduced data transfer.

Excerpts also improve SEO by reducing duplicate content. When full posts appear on both the single post page and archive pages, search engines may see this as duplicate content. Excerpts provide unique text on each page type, helping search engines understand the purpose of each page.

## Plugin Alternatives

Several WordPress plugins handle excerpt management without editing theme files:

- **Advanced Excerpt** – Control excerpt length, HTML tags preserved, and ending text
- **Excerpt Editor** – Bulk edit excerpts from the post list screen
- **WP Excerpt** – Auto-generate excerpts with configurable settings

For sites that cannot modify theme files, a plugin is the safer approach that survives theme updates.
