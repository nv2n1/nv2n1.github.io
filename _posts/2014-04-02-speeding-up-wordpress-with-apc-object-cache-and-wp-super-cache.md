---
title: "WordPress Performance Tuning: OPcache, Caching, and Asset Optimization"
date: 2014-04-02 17:34:13 +0000
modified: 2026-04-11 16:22:45 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /speeding-up-wordpress-with-apc-object-cache-and-wp-super-cache/
---

WordPress performance depends on three complementary caching layers: PHP bytecode caching (OPcache), page caching (WP Super Cache), and asset optimization (Autoptimize). Combined properly, they’ll cut your Time to First Byte in half and significantly improve Core Web Vitals.

## Enable OPcache in PHP

OPcache caches compiled PHP bytecode in shared memory, eliminating parse and compile overhead on every request. It’s bundled with PHP 7.0+ and is often enabled by default, but verify it’s active:

``` bash
php -i | grep -i opcache
```

Or check via a quick PHP script:

``` php
<?php
if (extension_loaded('Zend OPcache')) {
    echo "OPcache is enabled\n";
    echo "Version: " . phpversion('Zend OPcache') . "\n";
} else {
    echo "OPcache is not enabled\n";
}
?>
```

If disabled, enable it by adding to your php.ini (typically `/etc/php/8.x/fpm/php.ini` for PHP-FPM or `/etc/php/8.x/cli/php.ini`):

``` ini
zend_extension=opcache.so
opcache.enable=1
opcache.enable_cli=1
opcache.memory_consumption=256
opcache.interned_strings_buffer=16
opcache.max_accelerated_files=20000
opcache.max_wasted_percentage=5
opcache.validate_timestamps=1
opcache.revalidate_freq=2
opcache.log_verbosity_level=1
```

Key settings:

- **memory_consumption**: RAM allocated for bytecode cache. Start with 256 MB for WordPress; monitor with `opcache_get_status()` and increase if usage exceeds 90%.
- **max_accelerated_files**: Maximum files to cache. Set to ~20% above your actual file count. Check with `find /path/to/wordpress -type f -name "*.php" | wc -l`.
- **validate_timestamps**: Check if files changed on disk. Set to `1` for development, `0` for production (requires manual cache clear on deploys).
- **revalidate_freq**: Seconds between timestamp checks. Use `2` for development, `60+` for production.
- **interned_strings_buffer**: Intern duplicate strings. 16 MB is standard for WordPress.

Restart PHP-FPM after changes:

``` bash
sudo systemctl restart php-fpm
```

Or for Apache with mod_php:

``` bash
sudo systemctl restart apache2
```

Monitor OPcache stats in production:

``` php
<?php
$stats = opcache_get_status();
echo "Hit rate: " . round($stats['opcache_statistics']['hits'] / ($stats['opcache_statistics']['hits'] + $stats['opcache_statistics']['misses']) * 100, 2) . "%\n";
echo "Memory used: " . round($stats['memory_usage']['used_memory'] / 1024 / 1024, 2) . " MB\n";
echo "Files cached: " . $stats['opcache_statistics']['num_cached_scripts'] . "\n";
?>
```

Aim for 95%+ hit rate. Low hit rates indicate insufficient memory or frequent file changes.

## Install and Configure WP Super Cache

WP Super Cache stores static HTML versions of pages, bypassing PHP execution for repeat visitors.

Go to **Plugins → Add New**, search for “WP Super Cache”, install, and activate. Then navigate to **Settings → WP Super Cache**.

Enable caching with these configurations:

- **Cache logged-in users**: Disable in production. Enable only for debugging specific user sessions.
- **Cache timeout**: Default 3600 seconds (1 hour) works for most sites. Reduce to 600 seconds if content updates frequently; increase to 7200 if static.
- **Preload**: Enable to automatically generate cached pages on schedule rather than wait for first user visit.
- **Mobile caching**: Enable if serving different content to mobile users.
- **CDN support**: Enable if using Cloudflare, AWS CloudFront, or similar. Configure URLs for static asset offloading.

Advanced settings worth tuning:

- **Cache location**: Store in `/wp-content/cache/` (default) or separate `tmpfs` mount for speed.
- **Garbage collection**: Set to `3600` or higher to clean expired cache files periodically.
- **Cache footer**: Enable to cache dynamic footers (useful for dated content).

Test that caching works:

``` bash
curl -I https://yoursite.com/sample-post/
# Look for Cache-Control or X-Cache-* headers indicating cached response
```

Add cache-busting on content updates by editing your theme’s `functions.php`:

``` php
function flush_wp_super_cache_on_publish($post_id) {
    if (function_exists('wp_cache_post_change')) {
        wp_cache_post_change($post_id);
    }
}
add_action('publish_post', 'flush_wp_super_cache_on_publish');
add_action('publish_page', 'flush_wp_super_cache_on_publish');
```

## Minify and Optimize Assets with Autoptimize

Autoptimize minifies CSS, JavaScript, and HTML, reducing payload size and HTTP requests.

Install from **Plugins → Add New**, activate, and configure under **Settings → Autoptimize**.

**JavaScript optimization:**

- Enable “Optimize JavaScript code”
- Check “Defer JavaScript” to defer non-critical scripts (prevents render-blocking)
- Enable “Inline small JS” to embed tiny scripts directly in HTML

**CSS optimization:**

- Enable “Optimize CSS code”
- Check “Inline and defer CSS” only if your critical CSS is \<10 KB
- Enable “Inline critical CSS” and configure which CSS should load immediately for above-the-fold content
- Skip “Generate data: URIs” unless you have \<5 KB images in CSS

**HTML optimization:**

- Enable “Optimize HTML code” to remove comments and whitespace
- Disable “Keep HTML comments” in production (safe in development for debugging)

**Image optimization:**\
Autoptimize doesn’t handle images well—use a dedicated plugin:

- **ShortPixel** (free tier: 100 images/month)
- **Imagify** (free tier: up to 25 MB/month)
- **Smush** (WordPress native integration)

Or optimize via command line before uploading:

``` bash
# Install ImageMagick first
sudo apt install imagemagick

# Bulk convert and compress
for img in *.jpg; do convert "$img" -quality 82 -strip "${img%.jpg}_compressed.jpg"; done
```

**Test thoroughly** after enabling each option—some theme or plugin combinations break with aggressive minification:

1.  Clear all caches: Dashboard → WP Super Cache → Purge Cache
2.  Clear OPcache: Restart PHP-FPM
3.  Load a page and check browser Network tab for aggregated/minified assets
4.  Test form submissions, search, and dynamic content
5.  Check Console for JavaScript errors

If issues arise, disable Autoptimize, clear cache, and re-enable one setting at a time to identify conflicts.

## Monitor Performance

Measure improvements with tools that report real user metrics:

``` bash
# Using curl with timing
curl -w "@curl-format.txt" -o /dev/null -s https://yoursite.com/

# Time to First Byte (TTFB)
# DNS Lookup
# Server Processing
# Content Transfer
```

Track in Google Search Console:

- Core Web Vitals → LCP (Largest Contentful Paint), FID (First Input Delay), CLS (Cumulative Layout Shift)

Use Lighthouse (Chrome DevTools → Lighthouse) for detailed performance audits.

## Caching Layer Summary

These tools work in sequence:

1.  **OPcache** compiles PHP once and caches bytecode (server-side, lowest latency)
2.  **WP Super Cache** serves static HTML, bypassing PHP entirely for repeat visitors
3.  **Autoptimize** minifies and defers assets, reducing payload and render-blocking resources

Together, they reduce TTFB by 40-70%, Largest Contentful Paint by 30-50%, and bandwidth by 30-60% depending on theme complexity and plugin count.

For additional gains, add a CDN (Cloudflare, AWS CloudFront) to cache static assets geographically closer to users, or layer Varnish as a reverse proxy cache in front of your web server for highly dynamic content.
