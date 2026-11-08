---
title: "Redirect HTTP to HTTPS Using Apache mod_rewrite"
date: 2018-03-24 11:42:11 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-redirect-http-to-https-in-apache-with-mod_rewrite/
---

If you want to force HTTPS on your site, add this to your `.htaccess` file:

``` apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

The key parts:

- `RewriteCond %{HTTPS} off` — matches only HTTP requests
- `^(.*)$` — matches any request
- `https://%{HTTP_HOST}%{REQUEST_URI}` — rebuilds the URL with HTTPS
- `[L,R=301]` — uses a permanent redirect (301) and stops processing further rules

## Redirect specific domains only

If you’re running multiple domains and only want HTTPS on some:

``` apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteCond %{HTTP_HOST} ^(www\.)?example\.com$ [NC]
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

The `[NC]` flag makes the match case-insensitive.

## Exclude specific paths

To allow HTTP on certain paths (useful for ACME challenges):

``` apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteCond %{REQUEST_URI} !^/\.well-known/acme-challenge/ [NC]
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

## VirtualHost method (preferred for production)

For better performance and security, use VirtualHost configuration instead of `.htaccess`. Add this to your Apache config:

``` apache
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    RewriteEngine On
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com
    SSLEngine on
    SSLCertificateFile /path/to/cert.pem
    SSLCertificateKeyFile /path/to/key.pem
    # Your site content here
</VirtualHost>
```

VirtualHost redirects are faster because they don’t require `.htaccess` parsing on every request.

## Using HSTS for extra security

After redirecting to HTTPS, add HTTP Strict-Transport-Security (HSTS) headers to prevent downgrade attacks:

``` apache
<VirtualHost *:443>
    ServerName example.com
    SSLEngine on
    # ... SSL config ...
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
</VirtualHost>
```

This tells browsers to always use HTTPS for your domain. Start with a short `max-age` for testing:

``` apache
Header always set Strict-Transport-Security "max-age=300"
```

## Enable mod_rewrite if needed

If rewrites aren’t working, verify `mod_rewrite` is enabled:

``` bash
a2enmod rewrite
systemctl restart apache2
```

For `.htaccess` files to work, your VirtualHost must allow overrides:

``` apache
<Directory /var/www/example.com>
    AllowOverride All
</Directory>
```

## Check your setup

Test the redirect:

``` bash
curl -I http://example.com
```

You should see:

    HTTP/1.1 301 Moved Permanently
    Location: https://example.com/

Then verify HTTPS works:

``` bash
curl -I https://example.com
```

Use the VirtualHost approach in production for better performance. Reserve `.htaccess` for shared hosting where you can’t edit the main config files.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Web Server Best Practices

Keep your web server configuration clean and well-documented. Use version control for configuration files so changes can be tracked and rolled back. Always test configuration changes in a staging environment before applying to production.

Enable gzip compression and browser caching for better performance. Configure proper security headers including Content-Security-Policy, X-Frame-Options, and Strict-Transport-Security for HTTPS sites. Regularly update all server software to patch security vulnerabilities.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
