---
title: "Setting Up HTTP 301 Redirects in PHP"
date: 2013-07-12 16:46:11 +0000
layout: post
canonical: https://www.systutorials.com/permanent-redirect-with-http-301-in-php/
---

HTTP 301 (Moved Permanently) redirects tell browsers and search engines that a resource has permanently moved to a new location. This preserves SEO value and prevents broken links when restructuring your site or changing domains.

## Basic Implementation

The simplest approach uses PHP’s `header()` function with an explicit 301 status code:

``` php
<?php
header("Location: https://www.systutorials.com/", true, 301);
exit();
?>
```

The `exit()` call is critical—it stops script execution immediately, preventing any additional output that could interfere with the HTTP response.

For explicit control (useful in older PHP versions or debugging scenarios), set the status line first:

``` php
<?php
header("HTTP/1.1 301 Moved Permanently");
header("Location: https://www.systutorials.com/");
exit();
?>
```

Order matters. Setting the status line first ensures PHP sends 301 instead of defaulting to 302 (temporary redirect), which search engines treat differently.

## Common Redirect Patterns

**Preserve query strings and paths:**

``` php
<?php
$redirect_url = "https://www.systutorials.com/" . $_SERVER['REQUEST_URI'];
header("Location: " . $redirect_url, true, 301);
exit();
?>
```

**Domain migration redirect:**

``` php
<?php
if ($_SERVER['HTTP_HOST'] === 'old-domain.com') {
    header("Location: https://new-domain.com" . $_SERVER['REQUEST_URI'], true, 301);
    exit();
}
?>
```

**Conditional redirect with fallback:**

``` php
<?php
$new_url = get_new_page_url($_GET['old_id']);

if (!$new_url) {
    http_response_code(410); // Gone
    exit("Page not found");
}

header("Location: " . $new_url, true, 301);
exit();
?>
```

**Redirect old numeric IDs to slugs:**

``` php
<?php
if (is_numeric($_GET['post_id'])) {
    $slug = get_post_slug_by_id($_GET['post_id']);
    header("Location: /blog/{$slug}", true, 301);
    exit();
}
?>
```

## Server-Level Redirects (Preferred for Performance)

PHP redirects execute after the server processes the request, adding latency. For high-traffic sites, use server configuration instead.

**Apache with .htaccess:**

``` apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]

RewriteRule ^old-page\.html$ /new-page/ [R=301,L]
RewriteRule ^products/(.*)$ /shop/$1 [R=301,L]
```

**Nginx:**

``` nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}

location /old-page {
    return 301 /new-page;
}

location ~ ^/products/(.*)$ {
    return 301 /shop/$1;
}
```

Server-level redirects are faster because they occur before your application runs. Use PHP redirects only when you need application logic to determine the target URL.

## Avoiding Common Pitfalls

**Header restrictions:** The `header()` function must execute before any output. Common issues:

- Whitespace or newlines after `?>`
- UTF-8 BOM at file start (configure your editor to omit it)
- Output from included files
- HTML or spaces before `<?php`

If you hit “headers already sent” errors, check these first.

**Status code selection:**

- **301**: Permanent redirect—use for restructured pages, domain migrations
- **302**: Temporary redirect—use for maintenance or short-term changes
- **307/308**: Preserve HTTP method on POST requests
- **410**: Gone—signal that content was permanently deleted (no redirect)

**HTTPS enforcement:** Always redirect to HTTPS unless you have specific requirements otherwise. Modern browsers and search engines penalize HTTP-only sites.

## Testing Redirects

Verify the status code with `curl`:

``` bash
curl -I https://yoursite.com/old-page
```

Expected output:

    HTTP/2 301
    location: https://yoursite.com/new-page

Check the `location` header matches your target and the status is 301, not 302.

For redirect chains (A→B→C), follow the full path:

``` bash
curl -L -I https://yoursite.com/old-page
```

The `-L` flag follows redirects. Chains should resolve in 2-3 hops maximum; anything longer indicates misconfiguration.

## When to Avoid PHP Redirects

If your site handles significant traffic, move redirect logic to your web server. Use PHP redirects only when the redirect target requires database lookups, user context, or complex business logic. Otherwise, you’re wasting application resources on every request.

For WordPress sites, use the Redirection plugin or built-in REST endpoint redirects rather than manual PHP code. They integrate with the admin interface and maintain redirect logs across updates.
