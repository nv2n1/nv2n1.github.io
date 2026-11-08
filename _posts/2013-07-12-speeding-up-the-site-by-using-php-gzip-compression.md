---
title: "When and How to Use GZIP Compression in PHP"
date: 2013-07-12 16:46:12 +0000
modified: 2026-04-11 17:45:51 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /speeding-up-the-site-by-using-php-gzip-compression/
---

Compressing HTTP responses with gzip reduces bandwidth usage and improves page load times. However, **server-level compression should be your first choice**—PHP-level compression is a workaround for constrained hosting environments.

## How GZIP Compression Works

When a browser sends a request with `Accept-Encoding: gzip` in its headers, the server can compress the response body before transmission. The browser automatically decompresses it—the process is transparent to end users.

## Check If Your Server Already Compresses

Before adding PHP compression, verify your web server isn’t already handling this more efficiently:

``` bash
curl -I -H "Accept-Encoding: gzip" https://yoursite.com | grep -i content-encoding
```

If you see `Content-Encoding: gzip`, your server is already compressing responses. **Stop here.** PHP-level compression would be redundant and wasteful.

## Enable Server-Level Compression (Recommended)

### Nginx

Add to your server block:

``` nginx
gzip on;
gzip_types text/plain text/css text/javascript application/json application/javascript application/xml text/xml;
gzip_min_length 1000;
gzip_vary on;
gzip_proxied any;
```

The `gzip_min_length` setting avoids compressing files smaller than 1KB (compression overhead isn’t worth it). The `gzip_vary on` directive adds the `Vary: Accept-Encoding` header, essential for cache correctness.

### Apache

In your `.htaccess` or VirtualHost config:

``` apache
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    <IfModule mod_headers.c>
        Header append Vary Accept-Encoding
    </IfModule>
</IfModule>
```

Server-level compression is more efficient because:

- The web server can cache compressed assets and reuse them
- No per-request CPU overhead for dynamic content (with proper caching)
- Works transparently across all frameworks and languages

## PHP-Level Compression (When Server Config Isn’t Available)

If you’re on shared hosting without gzip support or need per-script control, use PHP’s output buffering:

``` php
<?php
// Place at the absolute start of your entry point (index.php, config file, etc.)
// Before any output, including whitespace or comments

if (isset($_SERVER['HTTP_ACCEPT_ENCODING']) && 
    strpos($_SERVER['HTTP_ACCEPT_ENCODING'], 'gzip') !== false) {
    ob_start('ob_gzhandler');
} else {
    ob_start();
}

// Rest of your application code
```

**Critical:** This code must be the first executable code in your file. Even a single space before the opening `<?php` tag will break output buffering.

### For WordPress Themes

Add to `functions.php`:

``` php
<?php
if (!function_exists('custom_gzip_start')) {
    function custom_gzip_start() {
        if (isset($_SERVER['HTTP_ACCEPT_ENCODING']) && 
            strpos($_SERVER['HTTP_ACCEPT_ENCODING'], 'gzip') !== false) {
            ob_start('ob_gzhandler');
        } else {
            ob_start();
        }
    }
    add_action('wp_loaded', 'custom_gzip_start', 0);
}
```

Using a hook is safer than modifying theme files directly.

## Performance Trade-offs

Compression costs CPU cycles to save bandwidth. On high-traffic sites, compressing every response can increase server load significantly.

If you use PHP compression:

- Monitor CPU usage before and after enabling it
- Consider only compressing for larger responses (\> 10KB)
- Use `gzip_level` to adjust compression ratio vs. CPU cost (1-9, default 6, lower = faster):

``` php
ini_set('zlib.output_compression_level', 6);
ob_start('ob_gzhandler');
```

- For REST APIs returning JSON, compression often provides 70-85% size reduction
- For HTML pages with external stylesheets/scripts, compression is less beneficial (those assets should be served pre-compressed or with server-level gzip)

## Verify Compression Works

Test your implementation:

``` bash
# Check response headers
curl -I -H "Accept-Encoding: gzip" https://yoursite.com

# Compare actual sizes
COMPRESSED=$(curl -s -H "Accept-Encoding: gzip" https://yoursite.com | wc -c)
UNCOMPRESSED=$(curl -s https://yoursite.com | wc -c)
echo "Compressed: $COMPRESSED bytes"
echo "Uncompressed: $UNCOMPRESSED bytes"
echo "Ratio: $(echo "scale=1; 100*$COMPRESSED/$UNCOMPRESSED" | bc)%"
```

Text-based content (HTML, JSON, CSS, JavaScript) typically compresses to 20-40% of original size.

## Best Practices

- **Prefer server-level compression** with proper `Vary: Accept-Encoding` headers
- **Don’t compress binary formats** (JPEG, PNG, WebP, video) in PHP—they’re already compressed
- **Cache aggressively**—compressed responses should be cached in HTTP caches and CDNs
- **Monitor after deployment**—watch CPU usage and response times, not just bandwidth savings
- **Test with real clients**—use curl, Firefox DevTools, or Chrome DevTools to verify the `Content-Encoding` header is present
