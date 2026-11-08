---
title: "Force HTTPS Redirects with .htaccess"
date: 2018-03-24 11:45:52 +0000
modified: 2026-04-13 00:02:33 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-force-a-website-to-use-https-by-htaccess-settings/
---

Forcing HTTPS on your website protects visitor data and improves SEO. The most common method is using `.htaccess` with Apache’s `mod_rewrite` module to redirect all HTTP requests to HTTPS.

## Basic HTTPS redirect

Add this to your `.htaccess` file in the document root:

``` apache
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

This performs a permanent 301 redirect from HTTP to HTTPS. The conditions and rules work as follows:

- `RewriteEngine On` — enables the rewrite module
- `RewriteCond %{HTTPS} !=on` — matches requests where HTTPS is not already on
- `RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]` — rewrites the request URL to use HTTPS, preserves the domain and request URI, and sends a 301 permanent redirect

The `[L,R=301]` flags mean:

- `L` — last rule (stops processing further rules)
- `R=301` — external redirect with 301 status code

## Alternative: redirect specific domains

If your site uses multiple domains or subdomains, you can be more selective:

``` apache
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteCond %{HTTP_HOST} ^(www\.)?example\.com$ [NC]
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

The `[NC]` flag makes the domain match case-insensitive.

## Forcing HTTPS with www prefix

To ensure visitors always use `www.example.com` over HTTPS:

``` apache
RewriteEngine On
RewriteCond %{HTTPS} !=on [OR]
RewriteCond %{HTTP_HOST} !^www\.example\.com$ [NC]
RewriteRule ^ https://www.example.com%{REQUEST_URI} [L,R=301]
```

This handles three cases: HTTP without www, HTTPS without www, and HTTP with www — all redirect to `https://www.example.com`.

## Removing www while forcing HTTPS

To enforce `https://example.com` (no www):

``` apache
RewriteEngine On
RewriteCond %{HTTPS} !=on [OR]
RewriteCond %{HTTP_HOST} ^www\. [NC]
RewriteRule ^ https://example.com%{REQUEST_URI} [L,R=301]
```

## Prerequisites and testing

Before deploying this in `.htaccess`:

1.  **Verify `mod_rewrite` is enabled** — check with your hosting provider or run `apache2ctl -M | grep rewrite` on your server
2.  **Ensure your SSL certificate is installed** — test at <a href="https://yoursite.com" rel="nofollow noopener" target="_blank">https://yoursite.com</a> to confirm the certificate loads without errors
3.  **Test the redirect** — use `curl -I http://yoursite.com` to verify it returns a 301 response
4.  **Check for mixed content** — after enabling HTTPS, audit your site for resources (images, scripts, stylesheets) still loading via HTTP

## Why 301 redirects matter

A 301 redirect signals to browsers and search engines that the move to HTTPS is permanent. Search engines will update their index and transfer SEO ranking from HTTP to HTTPS. Temporary redirects (302) will not achieve this and may confuse caching layers.

## HSTS headers for added security

After HTTPS is working, consider adding HSTS (HTTP Strict Transport Security) to your `.htaccess`:

``` apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
```

This tells browsers to always use HTTPS for your domain, even on the first visit. The `max-age` value is in seconds (31536000 = 1 year).

## Common issues

**Infinite redirect loop** — ensure your SSL certificate is valid and installed. An invalid cert can cause the server to reject HTTPS, creating a loop.

**Not working at all** — `mod_rewrite` may be disabled, or `.htaccess` files may not be processed (check `AllowOverride All` in your Apache configuration).

**Slow redirects** — 301 redirects are cached aggressively by browsers. If you need to test multiple times, use incognito/private mode or clear your browser cache.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Force HTTPS Redirects with .htaccess with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Force HTTPS Redirects with .htaccess. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.

## 2026 Comprehensive Guide for Systemd

This article extends “Force HTTPS Redirects with .htaccess” with advanced techniques and best practices for 2026. Following modern guidelines ensures reliable, maintainable, and secure systems.

### Advanced Implementation Strategies

For complex deployments involving systemd, consider Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment.

### Security and Hardening

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data, and follow the principle of least privilege for access controls.

### Performance Optimization

- Monitor system resources continuously with htop, vmstat, iotop
- Use caching strategies to optimize performance
- Profile application performance before and after optimizations
- Optimize database queries with proper indexing

### Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce issues, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found.

### Best Practices

- Write clean, self-documenting code with clear comments
- Use version control effectively with meaningful commit messages
- Implement proper testing before deployment
- Monitor production systems and set up alerts

### Resources and Further Reading

For more information on systemd, consult official documentation and community resources. Stay updated with the latest tools and frameworks.
