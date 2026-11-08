---
title: "Fetching Webpages as a Mobile Browser Using curl"
date: 2018-03-24 11:40:17 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-fetch-a-webpage-as-a-mobile-browser-with-curl-on-linux/
---

You can fetch a webpage as if you’re requesting from a mobile device by setting curl’s User-Agent header to match a mobile browser. Remote servers use the User-Agent header to decide whether to serve mobile or desktop versions of pages.

## Basic syntax

Use the `-A` (or `--user-agent`) flag to specify a mobile User-Agent string:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1" https://example.com/
```

## Current mobile User-Agent strings

Different devices and browsers require different User-Agent strings. These are current as of 2026:

**iPhone (Safari)**

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1" https://example.com/
```

**Android Chrome**

``` bash
curl -A "Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36" https://example.com/
```

**Android Firefox**

``` bash
curl -A "Mozilla/5.0 (Android 15; Mobile; rv:135.0) Gecko/135.0 Firefox/135.0" https://example.com/
```

**Samsung Galaxy (Chrome)**

``` bash
curl -A "Mozilla/5.0 (Linux; Android 15; SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36" https://example.com/
```

When in doubt, the Android Chrome string works for most sites that differentiate mobile content.

## Building realistic mobile requests

Combine the User-Agent with other headers to mimic real mobile browser behavior:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Accept-Encoding: gzip, deflate, br" \
  -H "Viewport-Width: 390" \
  -H "Sec-CH-UA-Mobile: ?1" \
  -L \
  https://example.com/
```

**Flag reference:**

- `-A` — Sets the User-Agent string
- `-H` — Add custom headers to match browser behavior
- `-L` — Follow redirects (many sites redirect mobile traffic differently)
- `-i` — Include response headers in output
- `-v` — Verbose mode (shows headers, SSL handshake, timing)
- `-o <file>` — Save output to file
- `-D <file>` — Save cookies to file (for stateful requests)

## Verify what the server received

Test endpoints confirm the User-Agent the server sees:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X)" https://httpbin.org/user-agent
```

Returns JSON with the User-Agent string the server recorded. Useful for debugging if mobile content isn’t being served.

## Save mobile pages to disk

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15" \
  https://example.com/ -o mobile-page.html
```

Include response headers:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X)" \
  -i https://example.com/ > mobile-response.txt
```

## Handling cookies and sessions

Some sites require cookies for proper mobile detection:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X)" \
  -c cookies.txt \
  -b cookies.txt \
  https://example.com/
```

The `-c` flag saves cookies; `-b` loads them for subsequent requests.

## Common issues and solutions

**User-Agent strings change frequently**

Mobile OS versions and browser versions update multiple times per year. If a particular User-Agent stops working, check current strings at <a href="https://www.whatismybrowser.com/" rel="nofollow noopener" target="_blank">whatismybrowser.com</a> or capture one from a real device using browser DevTools.

**Servers validate beyond User-Agent**

Some sites check additional mobile headers like `Sec-CH-UA-Mobile`, viewport dimensions, or connection type. Try adding:

``` bash
curl -A "Mozilla/5.0 (Linux; Android 15)" \
  -H "Sec-CH-UA-Mobile: ?1" \
  -H "Sec-Fetch-Dest: document" \
  -H "Sec-Fetch-Mode: navigate" \
  https://example.com/
```

**JavaScript-rendered content**

curl only fetches raw HTML. If a site renders mobile content via JavaScript, curl won’t see the rendered output. Use headless browsers instead:

``` bash
# Using Playwright (Node.js)
npx playwright codegen --device "iPhone 12" https://example.com/

# Using Selenium (Python)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(390, 844)  # iPhone viewport
driver.get("https://example.com/")
```

**Rate limiting and blocking**

Aggressive scraping triggers rate limits and IP bans regardless of User-Agent. Respect `robots.txt`, add delays between requests, and rotate IPs if necessary:

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X)" \
  --max-time 10 \
  --retry 2 \
  --retry-delay 5 \
  https://example.com/
```

**Certificate issues with old systems**

On systems with outdated CA certificates, add `--cacert` or disable verification (for testing only):

``` bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X)" \
  --cacert /etc/ssl/certs/ca-certificates.crt \
  https://example.com/
```

Never disable SSL verification (`-k`) in production.
