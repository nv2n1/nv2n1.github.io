---
title: "Redirect Non-WWW URLs to WWW with .htaccess"
date: 2018-03-24 11:51:21 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-redirect-non-www-domain-to-www-domain-in-htaccess/
---

The most common approach is using Apache’s `mod_rewrite` module. Add this to your `.htaccess` file in your document root:

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_HOST} !^www\. [NC]
    RewriteCond %{HTTP_HOST} !^$
    RewriteRule ^(.*)$ http://www.%{HTTP_HOST}/$1 [L,R=301]
</IfModule>
```

This uses a 301 permanent redirect, which tells browsers and search engines that the www version is canonical. The conditions ensure you’re not rewriting:

- Requests that already have `www.`
- Requests with an empty host (prevents malformed redirects)

## Using HTTPS (recommended)

If your site uses HTTPS, adjust the rewrite target:

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_HOST} !^www\. [NC]
    RewriteCond %{HTTP_HOST} !^$
    RewriteRule ^(.*)$ https://www.%{HTTP_HOST}/$1 [L,R=301]
</IfModule>
```

Or use the `%{REQUEST_SCHEME}` variable to handle both HTTP and HTTPS dynamically:

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_HOST} !^www\. [NC]
    RewriteCond %{HTTP_HOST} !^$
    RewriteRule ^(.*)$ %{REQUEST_SCHEME}://www.%{HTTP_HOST}/$1 [L,R=301]
</IfModule>
```

## Alternative: Redirect www to non-www

If you prefer the opposite direction, swap the logic:

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_HOST} ^www\. [NC]
    RewriteRule ^(.*)$ https://%{HTTP_HOST:4}/$1 [L,R=301]
</IfModule>
```

The `%{HTTP_HOST:4}` strips the first 4 characters (`www.`) from the hostname.

## Modern alternative: Server configuration

For better performance and clearer intent, use your web server configuration instead of `.htaccess`. In Apache’s `httpd.conf` or a site config file:

``` apache
<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com

    <IfModule mod_rewrite.c>
        RewriteEngine On
        RewriteCond %{HTTP_HOST} !^www\. [NC]
        RewriteRule ^(.*)$ https://www.example.com/$1 [L,R=301]
    </IfModule>
</VirtualHost>
```

This is faster than `.htaccess` since the file isn’t parsed on every request.

## For Nginx users

If you’re running Nginx, use a server block instead:

``` nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    return 301 https://www.example.com$request_uri;
}

server {
    listen 443 ssl http2;
    server_name www.example.com;
    # your actual config here
}
```

## Testing your redirect

Verify the redirect is working:

``` bash
curl -I https://example.com
```

Look for a `301 Moved Permanently` response header and check the `Location` header points to the www version.

## Common issues

**Redirect loops**: Ensure your `.htaccess` condition excludes `www.` correctly. If you see a 310-redirect limit exceeded error, double-check the rewrite conditions.

**mod_rewrite not enabled**: The `<IfModule>` wrapper prevents errors if the module isn’t loaded, but the rule won’t execute. Enable it with:

``` bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

**Query strings**: The rules above preserve query strings automatically, but test with URLs like `example.com/page?param=value` to confirm.

**Subdomain preservation**: The rules work correctly with subdomains—`api.example.com` becomes `www.api.example.com`. If you want to exclude subdomains from redirects, add this condition:

``` apache
RewriteCond %{HTTP_HOST} ^[^.]+\.[^.]+$ [NC]
```

This only matches second-level domains (no subdomains present).

## Web Server Best Practices

Keep your web server configuration clean and well-documented. Use version control for configuration files so changes can be tracked and rolled back. Always test configuration changes in a staging environment before applying to production.

Enable gzip compression and browser caching for better performance. Configure proper security headers including Content-Security-Policy, X-Frame-Options, and Strict-Transport-Security for HTTPS sites. Regularly update all server software to patch security vulnerabilities.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
