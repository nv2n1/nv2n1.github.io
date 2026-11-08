---
title: "Configure PHP\u2019s Maximum Execution Time and Memory Limits"
date: 2018-03-24 08:17:32 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-change-the-maximum-execution-time-and-memory-size-allowed-for-php/
---

You’re seeing fatal errors because PHP has hit its default resource constraints:

    PHP Fatal error:  Maximum execution time of 30 seconds exceeded
    PHP Fatal error:  Allowed memory size of 268435456 bytes exhausted

These limits exist to prevent runaway scripts from consuming server resources. Here’s how to increase them.

## Via php.ini (Global Configuration)

The most reliable method is editing your PHP configuration file directly. Locate it first:

``` bash
php -r 'phpinfo();' | grep "Loaded Configuration File"
```

On Linux systems this is typically `/etc/php.ini` or `/etc/php/8.x/fpm/php.ini` (for PHP-FPM). Edit the file and modify these directives:

``` ini
memory_limit = 512M
max_execution_time = 300
```

The `memory_limit` sets total memory per script in megabytes (or use `K` for kilobytes, `G` for gigabytes). The `max_execution_time` is in seconds; use `0` to disable the timeout entirely (not recommended for production).

After changes, restart PHP:

``` bash
# If using PHP-FPM
sudo systemctl restart php-fpm

# If using mod_php with Apache
sudo systemctl restart apache2
# or
sudo systemctl restart httpd
```

Verify the changes took effect:

``` bash
php -i | grep -E "memory_limit|max_execution_time"
```

## Via .htaccess (Per-Directory)

If you can’t modify php.ini or need directory-specific limits, use `.htaccess`:

``` apache
php_value memory_limit 512M
php_value max_execution_time 300
```

This only works if `AllowOverride` is enabled in your Apache configuration. Check with your hosting provider if you’re unsure.

## Via Code (Per-Script)

You can adjust limits within individual PHP scripts using `ini_set()`:

``` php
ini_set('memory_limit', '512M');
ini_set('max_execution_time', 300);
```

This must run before memory-intensive or long-running operations. Note that some hosts disable `ini_set()` for security reasons, and it won’t override hardcoded limits in php.ini prefixed with `hard_` in PHP-FPM.

## Application-Specific Settings

Some applications define their own memory handling:

**WordPress** — Add to `wp-config.php`:

``` php
define('WP_MEMORY_LIMIT', '256M');
define('WP_MEMORY_POST_LIMIT', '512M');  // For uploads
```

**Drupal** — Adjust in `settings.php`:

``` php
ini_set('memory_limit', '256M');
```

**Composer** — Increase memory for dependency resolution:

``` bash
COMPOSER_MEMORY_LIMIT=-1 composer install
```

## Practical Sizing Guidelines

Don’t blindly set high values. Size based on your workload:

- **Low traffic sites**: 128M memory, 30s timeout
- **Image processing**: 512M+ memory, 300+ seconds
- **API endpoints**: 256M memory, 60s timeout
- **Long batch jobs**: 1G+ memory, 0 (no limit)

Monitor actual usage:

``` bash
# Check current PHP process memory on Linux
ps aux | grep php-fpm | awk '{print $6}'
```

If a script regularly hits the memory limit, the issue is usually a leak or inefficient code, not insufficient resources. Increasing limits temporarily masks the real problem.

## Other Resource Limits to Consider

Beyond memory and execution time:

- `max_input_vars` — Number of POST/GET variables (default 1000)
- `post_max_size` — Request body size limit (must be larger than `upload_max_filesize`)
- `upload_max_filesize` — Single file upload limit
- `default_socket_timeout` — Database/network operation timeout

All are configured the same way: in php.ini, .htaccess, or via `ini_set()`.

## 2026 Best Practices and Advanced Techniques

For Configure PHP’s Maximum Execution Time and Memory Limits, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
