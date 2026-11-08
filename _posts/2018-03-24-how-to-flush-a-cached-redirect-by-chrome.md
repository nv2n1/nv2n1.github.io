---
title: "Clear Cached Redirects in Chrome: A Developer\u2019s Guide"
date: 2018-03-24 11:40:21 +0000
author: "Eric Ma"
layout: post
categories: [databases-storage]
canonical: /how-to-flush-a-cached-redirect-by-chrome/
---

Chrome aggressively caches HTTP redirects—especially 301 (permanent) and 308 redirects—as a performance optimization. The cache persists across browser sessions, which causes real problems when you’ve updated redirect rules and need to test them immediately.

## Understanding Chrome’s Redirect Cache Behavior

Chrome stores redirect information at the browser level, separate from typical page caches. This means:

- 301 and 308 redirects are cached indefinitely (until explicitly cleared)
- 302 and 307 redirects are cached per-session only
- The cache survives browser restarts and even reinstalls in some cases
- Standard cache clearing doesn’t always remove redirect caches

## Method 1: Clear Site Data (Most Effective)

This is the fastest way to clear cached redirects for a specific domain:

1.  Navigate to the affected domain in Chrome
2.  Click the lock icon (or info icon) in the address bar
3.  Select “Cookies and site data”
4.  Click “Manage” to open the detailed storage view
5.  Click “Remove all shown” to delete all cached data for that domain

This clears cookies, localStorage, sessionStorage, cache storage, and cached redirects in a single action. Use this approach when you’ve changed redirects and need to test immediately.

## Method 2: Clear All Browser Cache (Nuclear Option)

When targeted clearing doesn’t work:

1.  Press `Ctrl+Shift+Delete` (Windows/Linux) or `Cmd+Shift+Delete` (macOS)
2.  Set the time range to “All time”
3.  Check “Cookies and other site data” and “Cached images and files”
4.  Click “Clear data”

This removes cached data across all sites, so reserve it for situations where you can’t identify which specific domain is causing issues.

## Method 3: DevTools Hard Refresh

For quick testing during development:

1.  Open DevTools (`F12` or `Ctrl+Shift+I`)
2.  Right-click the browser refresh button
3.  Select “Empty cache and hard refresh”

This bypasses the cache for a single page load but doesn’t permanently clear the redirect cache. Chrome will re-cache the redirect on the next visit, so use this only for immediate testing.

## Prevent Redirect Caching During Development

The most reliable approach is to avoid permanent redirects altogether. Use temporary status codes during development:

- **301/308**: Permanent redirects—Chrome caches indefinitely. Avoid during active development.
- **302/307**: Temporary redirects—Chrome caches per-session only. Use these while testing.

For example, temporarily redirect with a 302 instead of a 301:

``` bash
# Quick test redirect with 302 (temporary)
curl -i -L https://example.com/old-path
```

## Disable Caching with HTTP Headers

Configure your web server to prevent caching on redirect endpoints:

**Apache (.htaccess)**:

``` apache
<IfModule mod_headers.c>
    Header set Cache-Control "no-store, no-cache, must-revalidate, max-age=0"
    Header set Pragma "no-cache"
</IfModule>
```

**Nginx**:

``` nginx
location /old-path {
    add_header Cache-Control "no-store, no-cache, must-revalidate, max-age=0";
    add_header Pragma "no-cache";
    return 302 /new-path;
}
```

**Node.js/Express**:

``` javascript
app.get('/old-path', (req, res) => {
    res.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
    res.set('Pragma', 'no-cache');
    res.redirect(302, '/new-path');
});
```

## Verify Redirects Server-Side

Use `curl` to test redirect behavior without relying on browser caching:

``` bash
# Show headers and follow redirects
curl -i -L https://example.com/old-path

# Check specific status code without following
curl -I https://example.com/old-path

# Verbose output for debugging
curl -v https://example.com/old-path
```

The `-i` flag shows response headers; `-L` follows redirects. This approach bypasses browser caching entirely and shows you exactly what the server is returning.

## Test in Incognito Mode

For quick validation, open an incognito/private window. Each incognito session starts with a clean cache:

1.  Press `Ctrl+Shift+N` (Windows/Linux) or `Cmd+Shift+N` (macOS)
2.  Test your redirect in the new window
3.  The incognito cache doesn’t persist after the window closes

This is useful for verifying changes without manually clearing caches repeatedly.

## Other Browsers

**Firefox**: Press `Ctrl+Shift+Delete`, select “All” for time range, check “Cache”

**Safari**: Enable the Develop menu in preferences, then select Develop → “Empty Web Caches”

**Edge**: Uses Chromium’s cache system; follow the same methods as Chrome

## Production Troubleshooting

Always verify redirect behavior server-side first using `curl` or web server logs rather than relying on browser-side debugging. Browser caching can mask actual server-side issues, so check your redirect configuration and HTTP status codes directly before assuming a browser cache problem.
