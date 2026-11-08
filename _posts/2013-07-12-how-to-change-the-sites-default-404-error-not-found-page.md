---
title: "Configuring Custom Error Pages on Apache and Nginx"
date: 2013-07-12 16:46:09 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-sites-default-404-error-not-found-page/
---

Apache’s default 404 error page is generic and often displays hosting provider branding. Customizing it gives you control over the user experience when they land on missing pages. The same applies to other HTTP error responses like 403 Forbidden or 500 Internal Server Error.

## Apache: Using ErrorDocument Directive

The `ErrorDocument` directive in Apache accepts two formats:

    ErrorDocument code /path/to/file.html
    ErrorDocument code https://example.com/path/to/file.html

The first serves a local file relative to your document root (preferred — faster and more reliable). The second redirects to an external URL, which can break if the external server is unavailable.

### Setup in .htaccess

Add this to `.htaccess` in your document root:

    ErrorDocument 404 /404.html
    ErrorDocument 403 /403.html
    ErrorDocument 500 /500.html
    ErrorDocument 503 /503.html

Test your custom page works:

``` bash
curl -i https://example.com/nonexistent-page
```

You should see a 404 status code and your custom page content.

### Setup in Virtual Host Configuration

For better performance, add `ErrorDocument` directly to your Apache virtual host config instead of `.htaccess`. This avoids parsing `.htaccess` on every request:

    <VirtualHost *:80>
        ServerName example.com
        DocumentRoot /var/www/html

        ErrorDocument 404 /404.html
        ErrorDocument 403 /403.html
        ErrorDocument 500 /500.html
        ErrorDocument 503 /503.html
    </VirtualHost>

Reload Apache after changes:

``` bash
sudo systemctl reload apache2
```

## Which Error Codes to Customize

Not all error codes are worth customizing. Monitoring tools and API clients rely on specific HTTP responses. Only override codes users might encounter directly in a browser:

| Code | Meaning               | Customize?        |
|------|-----------------------|-------------------|
| 400  | Bad Request           | No                |
| 401  | Unauthorized          | Sometimes         |
| 403  | Forbidden             | Yes               |
| 404  | Not Found             | Yes (most common) |
| 405  | Method Not Allowed    | No                |
| 500  | Internal Server Error | Yes               |
| 502  | Bad Gateway           | No                |
| 503  | Service Unavailable   | Yes               |

## Dynamic Error Pages with PHP

For more control, point `ErrorDocument` to a PHP script instead of a static file:

    ErrorDocument 404 /errors/handler.php

Inside the script, access error details via environment variables:

``` php
<?php
$status = $_SERVER['REDIRECT_STATUS'] ?? 'Unknown';
$requested_uri = $_SERVER['REDIRECT_URL'] ?? $_REQUEST_URI'];

http_response_code($status);
echo "Error $status: The page you requested ($requested_uri) was not found.";
?>
```

This approach lets you log errors, display context-specific messages, redirect to search results, or track 404s for dead link analysis. Set proper file permissions:

``` bash
chmod 644 /var/www/html/errors/handler.php
```

## Nginx Configuration

If you’re running Nginx, use the `error_page` directive in your server block:

``` nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/html;

    error_page 404 /404.html;
    error_page 403 /403.html;
    error_page 500 502 503 /50x.html;

    location = /404.html {
        internal;
    }

    location = /50x.html {
        internal;
    }
}
```

The `internal;` directive prevents direct access to the error page files themselves and is a best practice.

For a dynamic error handler in Nginx:

``` nginx
error_page 404 /errors/handler.php;

location ~ \.php$ {
    fastcgi_pass unix:/var/run/php-fpm.sock;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include fastcgi_params;
}
```

Reload Nginx after changes:

``` bash
sudo systemctl reload nginx
```

## Common Pitfalls

**Redirect loops**: Don’t point an `ErrorDocument` to a page that itself returns an error. If `/404.html` doesn’t exist, you’ll trigger an infinite loop. Always verify the error page file exists before deploying.

**File permissions**: Ensure your error page files are readable by the web server process:

``` bash
chmod 644 /var/www/html/404.html
```

On Debian/Ubuntu, Apache runs as `www-data`. On RHEL/CentOS, it’s `apache`. Wrong permissions will trigger a 500 error instead of your custom page.

**Absolute paths required**: Use paths relative to your document root with a leading slash:

    ErrorDocument 404 /404.html    # correct
    ErrorDocument 404 404.html     # avoid — ambiguous

**Verifying in logs**: Check your access logs to confirm requests hit your error handler:

``` bash
tail -f /var/log/apache2/access.log | grep 404
```

## Application-Level Error Handling

Modern web frameworks (Django, Laravel, Express.js, FastAPI) handle error pages more elegantly than web server configuration. They give you access to request context, session data, application state, and logging. This approach scales better and is easier to maintain.

If you’re building a new application, implement error handling at the application layer. Use web server directives only for static sites or as a fallback.
