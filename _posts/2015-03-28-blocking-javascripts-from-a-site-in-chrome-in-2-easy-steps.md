---
title: "Block JavaScript on Specific Sites in Chrome"
date: 2015-03-28 14:32:19 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/blocking-javascripts-from-a-site-in-chrome-in-2-easy-steps/
---

Blocking JavaScript per-site in Chrome lets you stop intrusive scripts, malicious content, or resource-heavy trackers without disabling JavaScript globally. This gives you surgical control—some sites work fine without JS, while others need it.

## Access the JavaScript exceptions page

Open Chrome and navigate to this URL in the address bar:

    chrome://settings/contentExceptions#javascript

Alternatively, go through the menu: **Settings \> Privacy and security \> Site Settings \> JavaScript**.

## Add a domain pattern and select Block

In the “Hostname pattern” field, enter the domain you want to block. Chrome accepts these formats:

- `example.com` — blocks JavaScript only on that exact domain (not subdomains)
- `[*.]example.com` — blocks JavaScript on example.com and all subdomains (www.example.com, api.example.com, mail.example.com, etc.)
- `https://example.com` — blocks JavaScript specifically on HTTPS; HTTP version still gets JS
- `cdn.example.com` — blocks only that specific subdomain

Select **Block** from the “Behavior” dropdown and click **Add**.

## Practical examples

**Block all scripts from a tracking domain:**

- Pattern: `[*.]analytics-provider.com`
- Behavior: Block

**Block scripts only on a CDN subdomain:**

- Pattern: `cdn.example.com`
- Behavior: Block

**Block a specific HTTPS variant:**

- Pattern: `https://ads.example.com`
- Behavior: Block

## Verify the block is working

Visit the blocked site and open DevTools with **F12** or **Ctrl+Shift+I**. Check the **Console** tab—you’ll see CSP (Content Security Policy) violations or blocked script errors confirming the browser blocked those resources.

Open the **Network** tab to see which scripts were blocked—they’ll appear with a red X or blocked status.

## Remove or modify a blocked domain

Go back to `chrome://settings/contentExceptions#javascript`, find the entry in the list, and click the trash icon to delete it.

To change a rule from “Block” to “Allow”, click the three dots next to the entry and select **Edit**, then change the behavior dropdown.

## Limitations and alternatives

Chrome’s per-site JavaScript blocking doesn’t work on:

- Inline scripts embedded directly in the HTML `<script>` tags
- Scripts loaded from the same domain

It only blocks external scripts and scripts from other domains.

For more granular control—including inline script blocking, regex patterns, and element filtering—use content blocking extensions:

- **uBlock Origin** — blocks scripts, ads, and trackers with regex support
- **NoScript** — whitelist-based JavaScript control with fine-grained permissions
- **Ghostery** — tracker blocking with detailed reports

These extensions also block resource-intensive third-party content beyond just JavaScript, improving page load times on bloated sites.

## Other per-site content controls

Chrome’s Site Settings menu lets you manage other content per-domain:

- **Cookies** — allow, block, or auto-clear after session
- **Images** — block images from specific domains
- **Popups** — prevent popup windows
- **Plugins** — control Flash and other legacy plugins
- **Autoplay** — silence video and audio autoplay
- **Third-party cookies** — block tracking cookies from external sources

If you frequently block content on the same sites, extensions are faster than repeatedly modifying Chrome’s exceptions list.

## 2026 Best Practices and Advanced Techniques

For Block JavaScript on Specific Sites in Chrome, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
