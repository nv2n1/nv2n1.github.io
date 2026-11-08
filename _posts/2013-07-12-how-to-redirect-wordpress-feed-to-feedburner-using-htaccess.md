---
title: "Using .htaccess to Redirect WordPress Feeds to Feedburner"
date: 2013-07-12 16:46:12 +0000
modified: 2026-04-11 17:48:48 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-redirect-wordpress-feed-to-feedburner-using-htaccess/
---

Feed redirection lets you centralize analytics and distribution while keeping your original feed accessible to feed aggregators. By routing requests through Feedburner (or similar services), you gain subscriber tracking, ads, and optimization features without breaking feed readers that depend on your WordPress feed URL.

## How It Works

The redirect strategy intercepts feed requests and conditionally routes them based on the User-Agent header:

- Requests from Feedburner and known feed aggregators pass through to your actual WordPress feed
- Requests from browsers and regular feed readers redirect to your Feedburner URL
- This keeps Feedburner subscribed to fresh content while readers get the optimized version

## .htaccess Implementation

Add this to your `.htaccess` file in your WordPress root directory:

``` apache
# Redirect WordPress feeds to FeedBurner
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{REQUEST_URI} ^/?(feed.*|.*\.xml)$ [NC]
  RewriteCond %{HTTP_USER_AGENT} !FeedBurner [NC]
  RewriteCond %{HTTP_USER_AGENT} !Feedfetcher [NC]
  RewriteCond %{HTTP_USER_AGENT} !feed [NC]
  RewriteCond %{HTTP_USER_AGENT} !Podcast [NC]
  RewriteRule ^(.*)$ https://feeds.feedburner.com/systutorials [L,R=301]
</IfModule>
```

Replace `https://feeds.feedburner.com/systutorials` with your actual Feedburner URL.

### What This Matches

- `/feed/` — main post feed
- `/feed/comments/` — comments feed
- `/sitemap.xml` and any other XML feeds
- Feed requests from browsers and generic readers

### Rule Breakdown

- `RewriteCond %{REQUEST_URI}` — matches feed and XML URLs
- `RewriteCond %{HTTP_USER_AGENT} !FeedBurner` — excludes FeedBurner’s crawler
- `RewriteRule ^(.*)$` — redirects everything else to Feedburner
- `[L,R=301]` — use permanent (301) redirects for proper SEO and caching

Use 301 (permanent) rather than 302 redirects — it preserves ranking signals and tells crawlers this is permanent.

## Testing the Rules

Before deploying, verify the rewrite works correctly:

``` bash
# Test a normal browser request (should redirect)
curl -A "Mozilla/5.0" -I /feed/

# Test FeedBurner's request (should pass through with 200)
curl -A "FeedBurner" -I /feed/

# Test with verbose output to see redirect chain
curl -v -A "Mozilla/5.0" /feed/
```

Browser requests should return a 301 status code. FeedBurner requests should return 200 (allowed through).

## Troubleshooting

**Redirects not working:**

- Verify mod_rewrite is loaded:

  ``` bash
  apache2ctl -M | grep rewrite
  ```

- Check your virtual host allows .htaccess overrides:

  ``` apache
  <Directory /var/www/html>
    AllowOverride All
  </Directory>
  ```

- Review Apache error logs for rewrite errors:

  ``` bash
  tail -f /var/log/apache2/error.log
  ```

- Verify no conflicting rewrite rules exist earlier in your `.htaccess` file

**Feeds returning 404:**

- Ensure WordPress permalinks are enabled (Settings → Permalinks)
- Check that your feed URL actually exists: `curl https://your-site.com/feed/`

## WordPress Hook Alternative

For sites where .htaccess changes are restricted, handle redirects within WordPress instead. Add this to a custom plugin or `functions.php`:

``` php
add_action( 'template_redirect', function() {
    if ( is_feed() ) {
        $user_agent = $_SERVER['HTTP_USER_AGENT'] ?? '';

        // Allow FeedBurner and known aggregators through
        $allowed_agents = [ 'FeedBurner', 'Feedfetcher', 'Podcast' ];
        $is_approved = false;

        foreach ( $allowed_agents as $agent ) {
            if ( stripos( $user_agent, $agent ) !== false ) {
                $is_approved = true;
                break;
            }
        }

        // Redirect everyone else
        if ( ! $is_approved ) {
            wp_safe_remote_get( 'https://feeds.feedburner.com/your-feed' );
            wp_redirect( 'https://feeds.feedburner.com/your-feed', 301 );
            exit;
        }
    }
});
```

This approach:

- Works in restricted hosting environments
- Integrates with WordPress’s hook system
- Avoids .htaccess complexity
- Performs slightly slower than server-level redirects on high traffic

The `.htaccess` method remains more efficient for high-traffic sites since redirects happen before WordPress loads.

## Important: Feedburner Deprecation

Google deprecated standalone Feedburner in 2021 and fully shut it down in 2024. If you’re still relying on it, migrate to:

- **Substack** — built-in newsletter distribution and paid content support
- **Ghost** — self-hosted or managed, native email lists and analytics
- **Mailchimp** — RSS-to-email automation with list management
- **Convertkit** — author-focused newsletter platform with automation
- **Self-hosted** — RSS plugins like Mailpoet or direct email integrations

If you maintain Feedburner redirects for legacy reasons, test periodically to ensure they still function before visitors encounter breakage.
