---
title: "How to Set Up 301 Redirects for Domain Migrations in Apache and Nginx"
date: 2013-07-12 16:46:09 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-redirect-old-domain-to-new-domain-using-htaccess-redirect/
---

Moving a domain requires more than DNS changes. If you have existing traffic, backlinks, or search engine indexing pointing to your old domain, a proper 301 redirect ensures users and search engines find your content at the new location while preserving SEO rankings.

## Why 301 Redirects Matter

A 301 (“Moved Permanently”) response tells browsers and search engines that your content has permanently moved. Users hitting the old URL get silently redirected to the new one. Search engines transfer accumulated ranking signals to the new domain rather than treating it as a duplicate or broken link.

Other redirect codes work differently: 302 (temporary), 303 (see other), and 307 (temporary redirect) tell search engines the move might be temporary, which can harm rankings. Use 301 for permanent migrations.

## Apache .htaccess Redirects

The .htaccess method works on Apache servers with mod_rewrite enabled. Most shared hosting providers have this set up by default.

Create or edit `.htaccess` in your old domain’s root directory:

``` apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP_HOST} ^(www\.)?old-domain\.com$ [NC]
  RewriteRule ^(.*)$ https://www.newdomain.com/$1 [R=301,L]
</IfModule>
```

This rule:

- Checks the HTTP_HOST header explicitly to handle both `old-domain.com` and `www.old-domain.com`
- Captures every request path with `^(.*)$` and forwards it to your new domain
- Preserves the URL path via `$1` (so `/blog/post/` becomes `/blog/post/` on the new domain)
- Sends a 301 response with `R=301` and stops processing further rules with `L`
- Uses `[NC]` for case-insensitive matching

The explicit host check is important if multiple domains point to the same server, preventing unintended redirects.

### Redirecting Multiple Domain Variants

If you need to redirect both `old-domain.com` and `www.old-domain.com`:

``` apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP_HOST} ^old-domain\.com$ [OR]
  RewriteCond %{HTTP_HOST} ^www\.old-domain\.com$
  RewriteRule ^(.*)$ https://www.newdomain.com/$1 [R=301,L]
</IfModule>
```

The `[OR]` operator allows matching multiple conditions.

### Excluding Specific Paths During Gradual Migration

If you’re migrating gradually and need to keep certain paths on the old domain temporarily:

``` apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP_HOST} ^(www\.)?old-domain\.com$ [NC]
  RewriteCond %{REQUEST_URI} !^/staging/ [NC]
  RewriteCond %{REQUEST_URI} !^/api/ [NC]
  RewriteRule ^(.*)$ https://www.newdomain.com/$1 [R=301,L]
</IfModule>
```

This keeps `/staging/` and `/api/` on the old domain while redirecting everything else. Add additional `RewriteCond` lines with the `!` (negation) operator for each path to exclude.

## Nginx Configuration

On Nginx servers, .htaccess doesn’t work. Add a server block for the old domain:

``` nginx
server {
    server_name old-domain.com www.old-domain.com;
    return 301 https://www.newdomain.com$request_uri;
}
```

Reload Nginx after making changes:

``` bash
systemctl reload nginx
```

For configuration syntax validation before reloading:

``` bash
nginx -t
```

## WordPress Domain Migration

.htaccess and Nginx redirects handle the HTTP layer, but WordPress stores the domain in the database. You must update these entries or you’ll encounter redirect loops and mixed content issues.

WordPress stores domain references in two key options:

- `siteurl` — the WordPress installation URL
- `home` — the site’s front page URL

Back up your database first:

``` bash
mysqldump -u username -p database_name > backup.sql
```

Update the database options via the WordPress admin dashboard (Settings \> General) or directly:

``` sql
UPDATE wp_options SET option_value = 'https://www.newdomain.com' WHERE option_name = 'siteurl';
UPDATE wp_options SET option_value = 'https://www.newdomain.com' WHERE option_name = 'home';
```

WordPress also stores domain references in post content, comments, and plugin settings. Use WP-CLI to update internal links across all tables:

``` bash
wp search-replace 'https://old-domain.com' 'https://www.newdomain.com' --all-tables
```

Verify changes first with `--dry-run`:

``` bash
wp search-replace 'https://old-domain.com' 'https://www.newdomain.com' --all-tables --dry-run
```

This command searches across all WordPress tables, including `postmeta`, `wp_posts`, and custom tables. After the dry run, review the output carefully before running without the flag.

If you have serialized data in WordPress options or postmeta that contains URLs, WP-CLI handles those automatically. For complex scenarios with unserialized data or custom post types, verify the changes in your database afterward.

## Testing the Redirect

Verify the redirect works correctly using curl:

``` bash
curl -I https://old-domain.com/some-page
```

Look for output like:

    HTTP/2 301
    location: https://www.newdomain.com/some-page

Check multiple paths to ensure redirects preserve the full URL structure.

Browser testing is equally important — some browsers cache redirects aggressively. Use a private/incognito window or clear your cache before testing. Some CDNs and intermediate proxies may also cache 301s, so testing with curl first is more reliable.

Test from multiple locations if your site uses geolocation-based routing, as edge caches may behave differently by region. If using a CDN like Cloudflare, test with a direct IP connection to bypass the cache:

``` bash
curl -I --resolve old-domain.com:443:YOUR_IP https://old-domain.com/some-page
```

## Post-Migration Checklist

Keep the old domain’s DNS and hosting active for at least 3–6 months after migration. Search engines need time to crawl and re-index your content. Killing the old domain too quickly results in lost traffic and ranking penalties.

- **Monitor Google Search Console and Bing Webmaster Tools** for redirect errors and crawl issues. Add the new domain as a property and verify ownership.
- **Set up 404 monitoring** to identify links that didn’t redirect properly (broken internal links, third-party references)
- **Check your analytics** for traffic anomalies during the transition period. Compare traffic week-over-week to detect drops.
- **Verify SSL certificates** are valid on both domains during the overlap period. Expired certificates break redirects.
- **Update DNS records** for other services (email, subdomains, API endpoints) pointing to the old domain
- **Notify external partners or vendors** of the domain change. Check for references in API documentation, partner integrations, or third-party services.

### Check for Redirect Chains

Redirect chains (A → B → C) slow down crawling and can lose ranking signals. Check server logs:

``` bash
grep "301" /var/log/apache2/access.log | head -20
```

For Nginx, check access logs:

``` bash
grep "301" /var/log/nginx/access.log | tail -20
```

If you see chains, update internal references directly to the final destination rather than relying on intermediate redirects.

### Monitoring After Migration

Use this command to monitor new requests hitting the old domain over time:

``` bash
tail -f /var/log/apache2/access.log | grep "old-domain.com"
```

Traffic should decline steadily over weeks as search engines and users update their bookmarks. A sudden drop to zero indicates DNS issues or hosting problems — the domain may have gone offline.

## Control Panel Alternatives

Most modern hosting panels (cPanel, Plesk, DirectAdmin) provide UI-based redirects that handle the HTTP redirect configuration. These are convenient but less transparent than .htaccess or server configuration files. If you use a control panel, verify the actual redirect rules it creates via SSH to ensure they’re correct.
