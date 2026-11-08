---
title: "Enabling .htaccess in Apache2"
date: 2018-03-24 11:47:51 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-allow-websites-htaccess-files-in-apache2/
---

By default, Apache2 ignores `.htaccess` files. The `AllowOverride` directive controls which directives in `.htaccess` Apache will process. To enable `.htaccess`, you need to configure Apache to allow overrides.

## Enable AllowOverride

Edit your Apache configuration file. On Ubuntu/Debian, this is typically:

```wp-block-code
sudo nano /etc/apache2/apache2.conf
```

Find the `<Directory /var/www/>` block and change `AllowOverride None` to `AllowOverride All`:

```wp-block-code
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>
```

For specific virtual hosts, edit the virtual host configuration instead:

```wp-block-code
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/example

    <Directory /var/www/example>
        AllowOverride All
    </Directory>
</VirtualHost>
```

After making changes, restart Apache:

```wp-block-code
sudo systemctl restart apache2
```

## AllowOverride Options

The `AllowOverride` directive accepts several values:

- `All` — Allow all directives in .htaccess
- `None` — Disable .htaccess completely (default for performance)
- `AuthConfig` — Allow authentication directives (AuthType, Require, etc.)
- `FileInfo` — Allow document type directives (ErrorDocument, Redirect, RewriteEngine, etc.)
- `Indexes` — Allow directory indexing directives
- `Limit` — Allow host access control (Allow, Deny, Order)
- `Options` — Allow Options directive

For URL rewriting (most common use of .htaccess), you need at least `FileInfo`:

```wp-block-code
AllowOverride FileInfo
```

For the least privilege approach, only enable what you need rather than `All`.

## Testing .htaccess

Create a test `.htaccess` file:

```wp-block-code
# /var/www/html/.htaccess
RewriteEngine On
RewriteRule ^test$ test.html [L]
```

Enable the rewrite module (required for RewriteEngine):

```wp-block-code
sudo a2enmod rewrite
sudo systemctl restart apache2
```

Test by accessing `http://your-server/test` — it should serve `test.html`.

## Common .htaccess Use Cases

**Redirect www to non-www:**

```wp-block-code
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]
```

**Force HTTPS:**

```wp-block-code
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
```

**Custom error pages:**

```wp-block-code
ErrorDocument 404 /errors/404.html
ErrorDocument 500 /errors/500.html
ErrorDocument 403 /errors/403.html
```

## Performance Impact

Apache looks for and parses `.htaccess` files on every request, for every directory in the path. This has a measurable performance cost:

- With `AllowOverride None`, Apache skips .htaccess lookups entirely
- With `AllowOverride All`, Apache checks every parent directory for .htaccess files

For production sites, consider moving .htaccess rules into the main Apache configuration file inside `<Directory>` blocks. This eliminates the per-request file lookup overhead.

## Troubleshooting

**.htaccess not working:**

```wp-block-code
# Check Apache error log
sudo tail -f /var/log/apache2/error.log

# Verify AllowOverride is set
apache2ctl -S | grep -i override

# Check if rewrite module is loaded
apache2ctl -M | grep rewrite
```

**500 Internal Server Error after .htaccess change:**

This usually indicates a syntax error in .htaccess. Check the error log for the specific line number, or temporarily rename .htaccess to disable it and confirm.

## Security Hardening with .htaccess

Once enabled, use .htaccess for common security hardening:

**Block access to sensitive files:**

```wp-block-code
<FilesMatch "\.(env|log|ini|sh|sql)$">
    Order allow,deny
    Deny from all
</FilesMatch>
```

**Disable directory listing:**

```wp-block-code
Options -Indexes
```

**Prevent hotlinking:**

```wp-block-code
RewriteEngine On
RewriteCond %{HTTP_REFERER} !^$
RewriteCond %{HTTP_REFERER} !^https?://(www\.)?example\.com [NC]
RewriteRule \.(jpg|jpeg|png|gif|mp4)$ - [F,NC]
```

**Set security headers:**

```wp-block-code
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

These headers protect against clickjacking, MIME-type sniffing, and cross-site scripting attacks.

## Enabling .htaccess per Directory

For shared hosting or multi-site setups, enable .htaccess for specific directories:

```wp-block-code
<Directory /var/www/site1>
    AllowOverride FileInfo AuthConfig
</Directory>

<Directory /var/www/site2>
    AllowOverride All
</Directory>
```

This granular approach lets you control which sites can use .htaccess and which directives they’re allowed to override, balancing flexibility with security.

## Checking Effective Configuration

To see what Apache is actually using for a specific URL:

```wp-block-code
# Install apache2-utils if not present
sudo dnf install httpd-tools    # Fedora/RHEL
sudo apt install apache2-utils  # Ubuntu/Debian

# Check effective config for a URL
apachectl -S  # Show virtual host settings
```
