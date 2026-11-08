---
title: "Website Mirroring with Wget: A Practical Guide"
date: 2019-06-13 10:01:46 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-mirror-a-website-using-wget-on-linux/
---

Wget is a reliable command-line tool for downloading entire websites for offline viewing, archival, or testing. It preserves the full site structure—HTML, images, CSS, JavaScript—and maintains the original directory layout.

## Basic Mirroring Command

The core command to mirror a website:

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com
```

### Flag Breakdown

- `--mirror`: Enables recursive downloading with time-stamping to avoid re-downloading unchanged files
- `--convert-links`: Rewrites links in downloaded files to work locally instead of pointing to the live site
- `--adjust-extension`: Adds proper file extensions (.html, .css) based on content type, fixing issues where servers don’t return extensions
- `--page-requisites`: Downloads CSS, JavaScript, images, and other assets required to render pages
- `--no-parent`: Restricts downloading to the specified directory and subdirectories, preventing crawl-up attacks

## Practical Examples

### Download to Default Location

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com
```

Downloads to `./example.com/` by default. Check what was downloaded with:

``` bash
find ./example.com -type f | wc -l
du -sh ./example.com
```

### Specify Output Directory

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -P /var/www/archive https://example.com
```

The `-P` flag sets the base directory for output.

### Limit Bandwidth and Crawl Speed

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --wait=2 --random-wait --limit-rate=500k https://example.com
```

- `--wait=2`: Adds a 2-second delay between requests
- `--random-wait`: Varies wait time by 0–2 seconds (more respectful to servers)
- `--limit-rate=500k`: Caps bandwidth at 500 KB/s

Always check the site’s `robots.txt` and terms of service before mirroring. For sites you don’t own, request permission first.

### Exclude File Types

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --reject=pdf,mp4,zip,exe https://example.com
```

Useful for skipping large media files or formats you don’t need. You can also use reject patterns:

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --reject="*.pdf,*.mp4,*.zip" https://example.com
```

### Limit Crawl Depth

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -l 3 https://example.com
```

The `-l 3` flag limits recursion to 3 levels deep. Prevents runaway downloads on large sites:

- `-l 1`: Only the starting page
- `-l 2`: Starting page + one level of linked pages
- `-l 3`: Three levels deep (typical for most sites)

### Mirror a Specific Subdirectory

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites https://example.com/blog/
```

Omit `--no-parent` if you want to crawl up to parent directories (use with caution, as it can download unrelated content).

### Mirror with User-Agent and Custom Headers

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
  https://example.com
```

Some sites block the default wget user-agent. Spoofing a browser user-agent can help, but always respect the site’s intentions.

### Resume Interrupted Downloads

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  -c https://example.com
```

The `-c` flag continues a partial download instead of starting over.

## Handling Common Issues

### Links Still Broken After Mirroring

If `--convert-links` isn’t catching all links, the site likely uses JavaScript for navigation. Wget doesn’t execute JavaScript, so it can’t discover dynamically generated links.

**Solution**: Use tools designed for dynamic content:

- **ArchiveBox**: Modern archival with headless Chrome/Firefox backend
- **Playwright**: Automate browser-based crawling with link discovery
- **Puppeteer**: Node.js-based headless browser control

For a quick Playwright solution:

``` python
from playwright.async_api import async_playwright
import asyncio

async def mirror_dynamic_site():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')
        html = await page.content()
        with open('page.html', 'w') as f:
            f.write(html)
        await browser.close()

asyncio.run(mirror_dynamic_site())
```

### Out-of-Memory Errors on Large Sites

Wget loads entire pages into memory, which can cause issues with very large sites.

**Solutions**:

- Use depth limits (`-l 2` or `-l 3`) to download in chunks
- Split downloads by subdirectory over multiple runs
- Use `--delete-after` to discard files after link conversion (only useful if you’re filtering during the mirror)

### Robots.txt Blocking Your Mirror

If `robots.txt` prevents mirroring and you have permission:

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  -e robots=off https://example.com
```

Only use `-e robots=off` if you own the site or have explicit written permission. Ignoring robots.txt on third-party sites violates ethical standards and may violate legal terms.

### SSL/TLS Certificate Errors

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --no-check-certificate https://example.com
```

The `--no-check-certificate` flag skips SSL validation. Use this only for trusted sites you control or internal development servers. For production environments, fix the certificate instead.

### Timeout Issues on Slow Connections

``` bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent \
  --timeout=30 --tries=3 https://example.com
```

- `--timeout=30`: Waits up to 30 seconds per request
- `--tries=3`: Retries failed downloads up to 3 times

## Verification and Testing

### Test the Local Copy

After mirroring, serve it locally to verify everything works:

``` bash
cd ./example.com
python3 -m http.server 8000
```

Navigate to `http://localhost:8000` in your browser. Click through pages to verify links and assets load correctly.

### Check for Broken or Unmodified Links

``` bash
grep -r "https://example.com" ./example.com/ | head -20
```

If external URLs remain unmodified, `--convert-links` missed them. This sometimes happens with:

- Links in JavaScript strings
- Links in JSON data
- Dynamically constructed URLs

Fix manually with sed if needed:

``` bash
find ./example.com -type f -name "*.html" -o -name "*.js" | \
  xargs sed -i 's|https://example.com|.|g'
```

### Count Downloaded Files and Check Size

``` bash
find ./example.com -type f | wc -l
du -sh ./example.com
```

## Alternatives

**ArchiveBox** — Modern, self-hosted archival with search indexing, screenshots, and multiple backend support (wget, headless Chrome, etc.). Better for complex, dynamic sites. Requires more setup but worth it for serious archival work.

**HTTrack** — Graphical and CLI tool with built-in duplicate detection and project management. Easier learning curve than wget but less scriptable for automation.

**wpCli with Custom Scripts** — For WordPress sites specifically, wp-cli can export content more reliably than crawling.

**Headless Browser Crawlers** (Puppeteer, Playwright, Selenium) — Essential for modern JavaScript-heavy sites. More resource-intensive but handles SPAs and API-driven content.

Use wget for simplicity and scriptability on straightforward, static HTML sites. Reach for ArchiveBox or headless browser solutions when dealing with dynamic content, JavaScript rendering, or large-scale archival projects.
