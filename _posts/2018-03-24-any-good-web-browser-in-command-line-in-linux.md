---
title: "Terminal Web Browsers: Lynx, w3m, and ELinks Compared"
date: 2018-03-24 11:46:19 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /any-good-web-browser-in-command-line-in-linux/
---

When you need to browse the web over SSH or in a headless environment, graphical browsers aren’t an option. Several terminal-based browsers exist that actually handle modern websites reasonably well, though with limitations around JavaScript and CSS.

## Lynx

Lynx is the oldest and most established terminal browser, first released in 1992. It’s still actively maintained and available in most Linux distributions.

Install it:

``` bash
sudo apt install lynx          # Debian/Ubuntu
sudo dnf install lynx          # Fedora/RHEL
sudo pacman -S lynx            # Arch
```

Basic usage:

``` bash
lynx https://example.com
```

Navigate with arrow keys, press `Enter` to follow links, `d` to download, `g` to go to a new URL, and `q` to quit. Lynx renders HTML cleanly and handles basic tables and forms. It doesn’t execute JavaScript, so many modern sites will be degraded but still readable.

View the full keybindings with `?` while in Lynx.

## w3m

w3m is more modern than Lynx and handles inline images in terminals that support it (using sixel or other protocols). It’s generally faster and has better CSS support.

``` bash
sudo apt install w3m
```

Usage:

``` bash
w3m https://example.com
```

Navigate with arrow keys, press `Enter` for links, `B` to go back, `Shift+U` for a new URL, `q` to quit. If your terminal supports image rendering, w3m will display them inline — useful for news sites and image-heavy content.

## elinks

elinks is a fork of links2 with more features, including tabbed browsing, cookie support, and better table rendering.

``` bash
sudo apt install elinks
```

Usage:

``` bash
elinks https://example.com
```

Press `?` for help. elinks supports tabs (`t` for new tab), bookmarks, and history. It’s a good middle ground between Lynx’s simplicity and feature-rich browsers.

## Comparing the three

| Feature       | Lynx       | w3m               | elinks   |
|---------------|------------|-------------------|----------|
| Installation  | Ubiquitous | Common            | Common   |
| Speed         | Fast       | Fast              | Moderate |
| Image support | No         | Yes (sixel/xterm) | No       |
| Tabs          | No         | No                | Yes      |
| Cookies       | Limited    | Yes               | Yes      |
| JavaScript    | No         | No                | No       |
| CSS support   | Basic      | Better            | Good     |

## Practical tips

**Dump page content to stdout** instead of opening interactively:

``` bash
lynx -dump https://example.com
w3m -dump https://example.com
elinks -dump https://example.com
```

This is useful in scripts. To extract just text without formatting:

``` bash
lynx -dump -nolist https://example.com | head -20
```

**Set a custom user agent** if a site blocks terminal browsers:

``` bash
lynx -useragent="Mozilla/5.0" https://example.com
```

**View source HTML**:

``` bash
lynx -source https://example.com | less
```

**For heavy scripting**, consider `curl` with `html2text` or similar instead of a browser:

``` bash
curl -s https://example.com | html2text
```

## When to use what

- **Lynx**: Most stable, works everywhere, best for simple HTML and text content
- **w3m**: When you need image support or better rendering
- **elinks**: When you want tabs and more modern browser features in a terminal

None of these handle modern JavaScript-heavy sites well. For those, you’d need a headless browser like Chromium in headless mode or Selenium, but that’s outside the scope of terminal browsing.

Install a couple and try them against your use case — terminal browsers have different strengths depending on the sites you visit.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Terminal Web Browsers: Lynx, w3m, and ELinks Compared with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Terminal Web Browsers: Lynx, w3m, and ELinks Compared. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
