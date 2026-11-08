---
title: "Enabling SEO-Friendly URLs in MediaWiki with Apache and Nginx"
date: 2013-07-15 12:56:47 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /search-engine-friendly-url-for-mediawiki/
---

MediaWiki’s default URL structure — `www.example.com/w/index.php?title=TITLE` — works functionally but creates poor SEO signals and awkward shareable links. Clean URLs like `www.example.com/w/TITLE` improve search visibility, readability, and user experience while making pages easier to reference.

## LocalSettings.php Configuration

Open `LocalSettings.php` in your MediaWiki root directory and add these settings:

``` php
$wgScript = "/w/index.php";
$wgArticlePath = "/w/$1";
```

The `$wgScript` variable points to your MediaWiki installation directory — adjust `/w/` if your installation lives elsewhere. The `$wgArticlePath` uses `$1` as a placeholder for the article title and generates the clean URL structure.

If MediaWiki runs in your document root rather than a subdirectory:

``` php
$wgScript = "/index.php";
$wgArticlePath = "/$1";
```

## Apache Setup with mod_rewrite

### Enable the Module

First, enable `mod_rewrite`:

``` bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

Verify the module is active:

``` bash
apache2ctl -M | grep rewrite
```

You should see `rewrite_module (shared)` in the output.

### Configure AllowOverride

Update your Apache site configuration to allow `.htaccess` overrides for the MediaWiki directory:

``` apache
<Directory /var/www/html/w>
    AllowOverride All
</Directory>
```

Then reload Apache:

``` bash
sudo systemctl reload apache2
```

### Create .htaccess Rules

Create or update `.htaccess` in your MediaWiki directory:

``` apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !^/w/api\.php
RewriteCond %{REQUEST_URI} !^/w/load\.php
RewriteCond %{REQUEST_URI} !^/w/rest\.php
RewriteRule ^(.*)$ /w/index.php?title=$1 [L,QSA]
```

The first two `RewriteCond` lines skip rewriting for actual files and directories — this prevents breaking CSS, images, JavaScript, and other assets. The three specific endpoint conditions protect MediaWiki’s API and resource loader from being rewritten. The `RewriteRule` passes the requested path as a title parameter while preserving any existing query strings with `[QSA]` (Query String Append).

For root-level MediaWiki installations, adjust the paths:

``` apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !^/api\.php
RewriteCond %{REQUEST_URI} !^/load\.php
RewriteCond %{REQUEST_URI} !^/rest\.php
RewriteRule ^(.*)$ /index.php?title=$1 [L,QSA]
```

## Nginx Configuration

If using Nginx, add this to your server block:

``` nginx
location /w {
    rewrite ^/w/(.*)$ /w/index.php?title=$1 last;
}

location ~ \.php$ {
    include fastcgi_params;
    fastcgi_pass unix:/run/php-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```

Adjust the PHP-FPM socket path based on your system. Check `/etc/php-fpm.d/www.conf` or your distribution’s PHP-FPM configuration. Common paths include `/var/run/php-fpm.sock` or versioned sockets like `/run/php8.3-fpm.sock`.

For root-level MediaWiki on Nginx:

``` nginx
location / {
    rewrite ^/(.*)$ /index.php?title=$1 last;
}

location ~ \.php$ {
    include fastcgi_params;
    fastcgi_pass unix:/run/php-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```

Validate the configuration:

``` bash
nginx -t
sudo systemctl reload nginx
```

## Troubleshooting

### 404 Errors on Apache

Verify `mod_rewrite` is loaded:

``` bash
apache2ctl -M | grep rewrite
```

Check Apache error logs:

``` bash
tail -f /var/log/apache2/error.log
```

Test with `curl` to bypass browser caching:

``` bash
curl -I https://example.com/w/Main_Page
```

Ensure the `.htaccess` file exists in your MediaWiki directory and `AllowOverride All` is set in your Apache configuration.

### 404 Errors on Nginx

Validate syntax:

``` bash
nginx -t
```

Check Nginx error logs:

``` bash
tail -f /var/log/nginx/error.log
```

Verify the rewrite rules match your directory structure. If MediaWiki is in a subdirectory, ensure all path references are correct.

### Broken API or REST Endpoints

If `api.php`, `rest.php`, or `load.php` return 404 errors, verify they’re excluded from rewrite rules as shown above. Test an API call directly:

``` bash
curl 'https://example.com/w/api.php?action=query&titles=Main_Page&format=json'
```

On Nginx, make sure `*.php` location blocks are evaluated before the rewrite rules.

### Cache and Redirect Issues

Clear your browser cache or test in an incognito window. Check PHP-FPM error logs:

``` bash
tail -f /var/log/php-fpm/error.log
```

Verify `index.php` exists in your MediaWiki directory.

## URL Encoding

MediaWiki handles URL encoding automatically. Article titles with spaces become underscores, and non-ASCII characters are percent-encoded. No additional configuration is needed.

## Verification

Test the new URL structure by visiting an article — you should see `https://example.com/w/Article_Title` in the address bar instead of the query string format. Verify:

- Click through several pages and check that URLs remain clean
- Edit an article and verify the editor loads correctly
- Check the article history page
- Confirm special pages like `Special:RecentChanges` work
- Test API calls with external tools or bots

A working API call should return valid JSON:

``` bash
curl 'https://example.com/w/api.php?action=query&titles=Main_Page&format=json' | jq .
```
