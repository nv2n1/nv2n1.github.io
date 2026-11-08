---
title: "Remove WordPress Canonical Tags from HTML Head"
date: 2018-03-24 08:04:50 +0000
layout: post
canonical: https://www.systutorials.com/disable-wordpress-built-in-canonical-url-link-tag-in-html-head/
---

WordPress has included automatic canonical URL generation since version 2.9. While this is usually beneficial for SEO, certain scenarios require disabling it — for example, when forum plugins generate incorrect canonical URLs that point all threads to a single page.

## The Problem

Canonical URLs tell search engines which version of a page is authoritative. When a forum plugin sets the same canonical URL for all threads (pointing to the page containing a shortcode), it prevents Google from indexing individual forum posts, treating them all as duplicate content.

## Global Removal

To disable WordPress’s built-in canonical link tag across your entire site, add this to your theme’s `functions.php` or a custom plugin:

``` php
remove_action( 'wp_head', 'rel_canonical' );
```

This removes the `wp_head` hook that WordPress uses to inject the canonical link tag.

## Conditional Removal

If you only want to disable canonical URLs for specific contexts, use a conditional approach. For example, to disable them only on pages while keeping them for posts:

``` php
add_action( 'wp_head', function() {
    if ( is_page() ) {
        remove_action( 'wp_head', 'rel_canonical' );
    }
}, 5 );
```

The priority `5` ensures this runs before WordPress’s default canonical action (priority 10).

## Custom Canonical URL Implementation

For more fine-grained control, remove the default canonical tag and implement your own:

``` php
remove_action( 'wp_head', 'rel_canonical' );

add_action( 'wp_head', function() {
    if ( is_singular() ) {
        $url = get_permalink();
        echo '<link rel="canonical" href="' . esc_url( $url ) . '" />' . "\n";
    }
}, 10 );
```

This approach lets you define your own canonical URL logic.

## Forum Plugin Example

If you’re using a forum plugin like Mingle Forum that generates incorrect canonical URLs, you can override its behavior in the plugin’s class file. Locate the function that outputs the canonical tag and conditionally apply it:

``` php
function setup_header() {
    $this->setup_links();
    global $user_ID;

    if ( is_page( $this->get_pageid() ) ) {
        // Custom canonical for forum pages
        $this->generate_canonical_tag();
    } else {
        // Use WordPress default for other content
        wp_rel_canonical();
    }
}

function generate_canonical_tag() {
    $url = '';

    if ( $this->options['forum_use_seo_friendly_urls'] ) {
        $uri = $this->get_seo_friendly_query();

        if ( ! empty( $uri ) && ! empty( $uri['action'] ) && ! empty( $uri['id'] ) ) {
            switch ( $uri['action'] ) {
                case 'thread':
                    $url = $this->get_threadlink( $uri['id'] );
                    break;
                case 'forum':
                    $url = $this->get_forumlink( $uri['id'] );
                    break;
                case 'group':
                    $url = $this->get_grouplink( $uri['id'] );
                    break;
            }
        }
    }

    if ( ! empty( $url ) ) {
        echo '<link rel="canonical" href="' . esc_url( $url ) . '" />' . "\n";
    }
}
```

This ensures each forum thread has its own unique canonical URL instead of all pointing to the container page.

## Testing Your Changes

After modifying canonical URL behavior:

1.  **Check the page source** — inspect the HTML head for the canonical link tag to verify it’s present or absent as intended
2.  **Validate with Search Console** — upload your sitemap and monitor coverage reports to ensure Google properly indexes all pages
3.  **Use SEO tools** — tools like Screaming Frog or Ahrefs can identify canonical tag issues across your site

## SEO Considerations

Before disabling canonical URLs globally:

- **Posts and pages** typically benefit from explicit canonical tags, especially if you have URL parameters or pagination
- **Archive pages** should use their canonical URLs to avoid duplicate content penalties
- **Dynamically generated content** (forums, user profiles) needs correct canonical URLs to be indexed individually

Remove canonical URLs only for the specific content types that need it, rather than globally, unless you have a clear reason to do so site-wide.
