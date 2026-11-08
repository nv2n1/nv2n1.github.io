---
title: "How to Clear Cookies for a Specific Site in Chrome"
date: 2018-03-24 08:18:16 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-remove-cookies-for-a-certain-site-in-chrome/
---

You can delete cookies from individual sites without clearing your entire browser cache. Here’s how:

### Via Settings UI

1.  Open `chrome://settings/privacy` in the address bar (or go to Settings \> Privacy and security)
2.  Click **Cookies and other site data**
3.  Click **All cookies and site data**
4.  Use the search box to find the domain you want to clear
5.  Click the trash icon next to the site to delete its cookies, or click the site name to view and selectively delete specific cookies

### Via DevTools (faster for active debugging)

If you’re testing a site you’re currently viewing:

1.  Press **F12** to open DevTools
2.  Go to the **Application** tab (or **Storage** in Firefox)
3.  Expand **Cookies** in the left sidebar
4.  Click the domain you want to clear
5.  Select all cookies (Ctrl+A) and delete them, or right-click individual cookies to remove them

DevTools also lets you inspect cookie values, expiration dates, and security flags before deleting.

### Clear cookies programmatically

If you’re automating testing or need to clear cookies via command line, use the Chrome debugging protocol:

``` bash
google-chrome --user-data-dir=/tmp/chrome-test https://example.com
```

For headless automation with Python/Playwright:

``` python
import asyncio
from playwright.async_api import async_playwright

async def clear_cookies():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        await context.clear_cookies()
        await browser.close()

asyncio.run(clear_cookies())
```

Or with Selenium:

``` python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
driver.delete_cookie("cookie_name")  # Delete specific cookie
# or
driver.delete_all_cookies()  # Clear all cookies for the domain
```

### Bulk management with extensions

For frequent cookie management, consider:

- **Cookie Editor** — Visual cookie manager with import/export
- **uBlock Origin** — Blocks cookies by default with granular control
- **Privacy Badger** — Automatically handles tracking cookies

### Browser-level cookie settings

You can also prevent specific sites from storing cookies:

1.  Go to `chrome://settings/privacy`
2.  Click **Cookies and other site data**
3.  Scroll to **Sites that can always use cookies** or **Sites that cannot use cookies**
4.  Add domains to block or allow lists

This approach stops sites from creating new cookies rather than deleting existing ones.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
