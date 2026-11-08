---
title: "WordPress Multisite: Running from a Subdirectory"
date: 2018-03-24 08:18:05 +0000
modified: 2026-04-11 16:06:59 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /installing-wordpress-in-a-sub-directory-while-working-for-the-whole-site/
---

Installing WordPress in a subdirectory keeps your site root cleaner and makes it easier to manage core files separately from content. Here’s how to configure WordPress so the admin and core files live in `/wordpress` while the site appears at your domain root.

## Creating the Subdirectory Structure

First, create the WordPress directory and set proper permissions:

``` bash
mkdir -p /var/www/html/wordpress
chown www-data:www-data /var/www/html/wordpress
chmod 755 /var/www/html/wordpress
```

Use `www-data` (Debian/Ubuntu) or `apache` (RHEL/CentOS) depending on your web server user. Verify with `ps aux | grep -E 'apache|nginx|www-data'`.

## Configuring WordPress Settings

Before moving files, update WordPress configuration in the admin panel:

1.  Log in to WordPress at its current location
2.  Navigate to **Settings → General**
3.  Set **WordPress Address (URL)** to `https://example.com/wordpress`
4.  Set **Site Address (URL)** to `https://example.com`
5.  Click **Save Changes**

You may see a 404 error after saving—this is expected. Don’t attempt to access the site yet.

## Moving Core Files

Move all WordPress core files (except `index.php` and `.htaccess`) to the subdirectory:

``` bash
cd /var/www/html
# Move all WordPress files except index.php and .htaccess
rsync -av --exclude='index.php' --exclude='.htaccess' --exclude='wp-content' /wordpress/ /wordpress/
# Or manually move wp-admin, wp-includes, wp-config.php, etc.
mv wp-admin /wordpress/
mv wp-includes /wordpress/
mv wp-config.php /wordpress/
# Move other core files but keep wp-content at root if desired
```

If you want to serve `wp-content` from the subdirectory instead, move it:

``` bash
mv /var/www/html/wp-content /var/www/html/wordpress/
```

Then add to `wp-config.php`:

``` php
define('WP_CONTENT_DIR', dirname(__FILE__) . '/wordpress/wp-content');
define('WP_CONTENT_URL', 'https://example.com/wordpress/wp-content');
```

## Updating Root Files

Copy `.htaccess` and `index.php` from the subdirectory to the root:

``` bash
cp /var/www/html/wordpress/index.php /var/www/html/index.php
cp /var/www/html/wordpress/.htaccess /var/www/html/.htaccess
```

If you’re using Nginx instead of Apache, you don’t have `.htaccess`—configure rewrites in your server block instead.

## Modifying Root index.php

Edit `/var/www/html/index.php` and change the require statement:

``` php
<?php
/**
 * Front to the WordPress application. This file doesn't do anything, but loads
 * wp-blog-header.php which does and tells WordPress to load the theme.
 */

/**
 * Tells WordPress to load the WordPress theme and output it.
 */
require( dirname( __FILE__ ) . '/wordpress/wp-blog-header.php' );
```

## Updating .htaccess for Pretty Permalinks

If using pretty permalinks, your root `.htaccess` needs rewrite rules:

``` apache
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
```

After moving files, log in at `https://example.com/wordpress/wp-admin/` and go to **Settings → Permalinks**. WordPress will attempt to update the `.htaccess` file automatically. If you see “Update .htaccess” message, copy the displayed rules manually into your root `.htaccess`.

## Nginx Configuration

If using Nginx, add this to your server block:

``` nginx
location / {
    try_files $uri $uri/ /index.php?$args;
}

location ~ \.php$ {
    fastcgi_pass unix:/run/php/php-fpm.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```

Reload Nginx:

``` bash
nginx -t && systemctl reload nginx
```

## Troubleshooting

**File permissions errors:** Ensure the web server user owns all WordPress files:

``` bash
chown -R www-data:www-data /var/www/html/
```

**404 on subpages:** Verify `.htaccess` is present and `mod_rewrite` is enabled:

``` bash
a2enmod rewrite
systemctl reload apache2
```

**Admin pages not found:** Check that `wp-config.php` is in `/wordpress/` and references are correct. Verify the `WP_HOME` and `WP_SITEURL` constants aren’t set in `wp-config.php` (they should be set via the admin panel).

**Uploads broken:** If `wp-content` moved to the subdirectory, ensure `WP_CONTENT_URL` constant is properly defined and the uploads directory is writable.

Your site should now be fully functional with WordPress core files in a subdirectory while the public site loads from the domain root.
