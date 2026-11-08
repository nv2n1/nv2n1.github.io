---
title: "Meta Refresh Redirects: When and Why to Avoid Them"
date: 2013-07-12 16:46:08 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /using-meta-tag-in-hmtl-head-to-redirect-pages/
---

The `<meta>` refresh tag provides a client-side redirect mechanism when server-side options aren’t available. While inferior to HTTP redirects for SEO and performance, it serves legitimate use cases: static hosting environments without backend access, transition screens for deprecated pages, or temporary migration notices.

## Basic Syntax

``` html
<meta http-equiv="refresh" content="delay; url=destination">
```

The `content` attribute contains two parts:

- **delay**: seconds before the redirect triggers (use `0` for immediate)
- **url**: the target URL to redirect toward

## Immediate Redirect

For instant redirection without user feedback:

``` html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=/">
    <title>Redirecting...</title>
  </head>
  <body>
    <p>If you are not redirected automatically, follow this <a href="/">link to systutorials.com</a>.</p>
  </body>
</html>
```

Always include a fallback link. Some users have JavaScript disabled, use screen readers, or experience slow connections.

## Delayed Redirect with Countdown

A delayed redirect with visible countdown gives users context and time to react:

``` html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5; url=/">
    <title>Page Moved</title>
    <style>
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        text-align: center;
        padding: 50px;
        max-width: 600px;
        margin: 0 auto;
      }
      .countdown {
        font-size: 2em;
        font-weight: bold;
        color: #0066cc;
        margin: 20px 0;
      }
      a {
        color: #0066cc;
        text-decoration: underline;
      }
    </style>
  </head>
  <body>
    <h1>This page has moved</h1>
    <p>Redirecting to <a href="/">systutorials.com</a> in <span class="countdown">5</span> seconds...</p>
    <script>
      let count = 5;
      const span = document.querySelector('.countdown');
      const timer = setInterval(() => {
        count--;
        span.textContent = count;
        if (count <= 0) clearInterval(timer);
      }, 1000);
    </script>
  </body>
</html>
```

## Preserving Query Parameters

Meta refresh doesn’t automatically carry query strings. Use JavaScript to forward parameters dynamically:

``` html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <script>
      const params = new URLSearchParams(window.location.search);
      const newUrl = `/page?${params.toString()}`;
      window.location.replace(newUrl);
    </script>
  </head>
  <body>
    <p><a href="/page">Continue if not redirected</a></p>
  </body>
</html>
```

Alternatively, hardcode the full target URL with parameters:

``` html
<meta http-equiv="refresh" content="0; url=/page?id=123&cat=linux">
```

## Meta Refresh vs. Server-Side Redirects

**Use meta refresh when:**

- Hosting static HTML on shared hosting without backend access
- Providing a transition or deprecation notice
- You need a grace period before redirecting users

**Use server-side redirects (HTTP 301/302) when:**

- You control the server configuration
- Permanently moving content (301 preserves SEO better)
- Redirecting API endpoints or dynamic routes
- Performance and SEO matter

Server-side redirects are faster (happen before the page loads), preserve search engine rankings better, and work reliably across all clients. If your host supports it, use `.htaccess` (Apache) or Nginx configuration:

``` apache
# Apache .htaccess
Redirect 301 /old-page /new-page
```

``` nginx
# Nginx
server {
  location /old-page {
    return 301 /new-page;
  }
}
```

For other servers, check documentation for redirect modules or rewrite rules.

## Accessibility Considerations

Always include a visible, clickable fallback link with descriptive text. Screen reader users need context. Never rely solely on meta refresh:

``` html
<body>
  <h1>Page Moved</h1>
  <p>This page has moved to <a href="/new-location">our new location</a>. You will be redirected automatically.</p>
  <meta http-equiv="refresh" content="5; url=/new-location">
</body>
```

## Browser Support and Testing

Meta refresh works across modern browsers and mobile browsers. However:

- Some older accessibility tools may not trigger the redirect
- Instantaneous redirects (0 second delay) without visible feedback confuse users
- Test on actual devices—emulators can miss edge cases
- Use a reasonable delay (3–5 seconds) if showing a notice

Set `content="0"` only when you have no choice. A brief delay with clear messaging improves user experience and reduces support requests.
