---
title: "Redirect RSS Feeds to follow.it with .htaccess"
date: 2020-06-20 03:35:41 +0000
author: "David Yang"
layout: post
categories: [programming-languages]
canonical: /how-to-redirect-feed-links-to-follow-it-using-htaccess/
---

Google shut down Feedburner’s management interface, leaving it in indefinite maintenance mode. While RSS remains a critical format for feed distribution across platforms like WordPress and other CMS software, you need an alternative service for feed management and subscriber tracking.

follow.it is a solid Feedburner replacement that handles RSS feeds, subscriptions, and analytics. This guide shows how to redirect your feed URLs to follow.it using .htaccess — a method that works regardless of your CMS or hosting setup.

## How the Redirect Works

The core strategy uses Apache’s `mod_rewrite` to detect the requesting client:

- **Requests from follow.it**: Pass through untouched so follow.it receives the original feed content from your server
- **Requests from browsers or readers**: Redirect to your follow.it feed URL so users subscribe there instead

This keeps follow.it subscribed to your authoritative feed while directing human visitors to the managed feed service.

## Implementation

Add this block to your `.htaccess` file in your site’s root directory (adjust the path if your feed lives elsewhere):

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_URI} ^/feed [NC]
    RewriteCond %{HTTP_USER_AGENT} !follow\.it [NC]
    RewriteRule ^feed/?.*$ https://follow.it/systut [L,R=302]
</IfModule>
```

Replace `https://follow.it/systut` with your actual follow.it feed URL. The `[NC]` flag makes pattern matching case-insensitive, and `[L,R=302]` tells Apache to stop processing and send a temporary redirect.

**Key points:**

- The `RewriteCond` for `HTTP_USER_AGENT` uses `!` to negate — meaning “if the User-Agent does NOT contain follow.it”
- The pattern `^feed/?.*$` matches `/feed`, `/feed/`, and any feed variants like `/feed/json`
- Use `R=302` (temporary redirect) rather than `R=301` (permanent) until you’re confident the redirect works correctly

## Testing Your Setup

Test with curl to verify follow.it can access the feed:

``` bash
curl -A "follow.it/1.0" https://yourdomain.com/feed
```

This should return your XML feed content without redirecting.

Then test as a regular browser:

``` bash
curl -A "Mozilla/5.0" https://yourdomain.com/feed -i
```

You should see a 302 response with a `Location` header pointing to follow.it.

## WordPress-Specific Considerations

WordPress creates multiple feed endpoints: `/feed`, `/feed/rss2`, `/feed/json`, and category/tag feeds like `/category/tech/feed`. Your regex should catch them all:

``` apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_URI} ^/feed [NC]
    RewriteCond %{REQUEST_URI} !^/wp-admin [NC]
    RewriteCond %{HTTP_USER_AGENT} !follow\.it [NC]
    RewriteRule ^.*feed/?.*$ https://follow.it/yourusername [L,R=302]
</IfModule>
```

The `!^/wp-admin` condition prevents redirecting dashboard requests.

## Switching Back Later

If you ever need to discontinue follow.it, simply comment out or remove the rewrite block. Your feed URLs revert to normal operation immediately since no permanent (301) redirects were issued.

## Troubleshooting

**Redirects not working:** Verify `mod_rewrite` is enabled with `apache2ctl -M | grep rewrite`. Some hosts disable it.

**Infinite loops:** This won’t happen with the User-Agent check, but if it does, your regex is probably matching something unexpected. Test patterns at regex101.com first.

**Follow.it can’t reach your feed:** Confirm your follow.it account is using the correct URL (usually your domain’s `/feed` path, not the follow.it URL itself).

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Redirect RSS Feeds to follow.it with .htaccess with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Redirect RSS Feeds to follow.it with .htaccess. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
