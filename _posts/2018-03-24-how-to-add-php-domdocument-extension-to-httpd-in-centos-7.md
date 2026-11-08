---
title: "How to Enable PHP DOM Extension in Apache on CentOS 7"
date: 2018-03-24 11:53:59 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-add-php-domdocument-extension-to-httpd-in-centos-7/
---

If you’re seeing PHP errors like `Class 'DOMDocument' not found`, your PHP installation is missing the XML extension. This is common after migrating sites or fresh installations where the base PHP package doesn’t include DOM support out of the box.

## Install php-xml

The solution is straightforward — install the `php-xml` package:

``` bash
sudo dnf install php-xml
```

On RHEL 9 and Rocky Linux 9+, `dnf` is the preferred package manager (yum is now an alias to dnf anyway, but dnf is more explicit).

## Restart Apache/httpd

After installation, reload Apache to apply the changes:

``` bash
sudo systemctl restart httpd
```

Or use the older syntax if you prefer:

``` bash
sudo apachectl restart
```

`systemctl` is more modern and consistent with current Linux practices, but both work.

## What gets installed

The `php-xml` package includes several XML-related modules:

``` bash
$ rpm -ql php-xml
/etc/php.d/dom.ini
/etc/php.d/wddx.ini
/etc/php.d/xmlreader.ini
/etc/php.d/xmlwriter.ini
/etc/php.d/xsl.ini
/usr/lib64/php/modules/dom.so
/usr/lib64/php/modules/wddx.so
/usr/lib64/php/modules/xmlreader.so
/usr/lib64/php/modules/xmlwriter.so
/usr/lib64/php/modules/xsl.so
```

The `.ini` files in `/etc/php.d/` are loaded automatically by PHP at startup, so no manual configuration is needed. The `.so` files are the actual compiled extensions.

## Verify the installation

Check that the extension is loaded:

``` bash
php -m | grep -i dom
```

You should see `dom` in the output. You can also check with a PHP script:

``` php
<?php
if (extension_loaded('dom')) {
    echo "DOM extension is installed\n";
} else {
    echo "DOM extension is NOT installed\n";
}
?>
```

Or test DOMDocument directly:

``` php
<?php
try {
    $doc = new DOMDocument();
    echo "DOMDocument is available\n";
} catch (Error $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```

## Related XML extensions

If your application uses other XML processing functions, you might also need:

- **php-xsl** (included in php-xml) — for XSLT transformations
- **php-simplexml** — usually included in base PHP, provides SimpleXML functions
- **php-xmlrpc** — if you’re doing XML-RPC calls (less common in modern stacks)

Check what’s already installed:

``` bash
php -m | grep -i xml
```

## Common issues

**Extension still not loading after restart:** Verify Apache is actually using the PHP module:

``` bash
httpd -M | grep php
```

You should see `php_module` in the output. If not, check `/etc/httpd/conf.modules.d/` for PHP configuration files.

**Wrong PHP version:** If you have multiple PHP versions installed (e.g., via Remi repository), ensure you’re installing php-xml for the same version as your httpd PHP module. Check:

``` bash
php -v
```

Then install the matching extension explicitly, like `php81-php-xml` if you’re using PHP 8.1.

**SELinux blocking:** On systems with SELinux enforcing, module loading can be blocked. Check logs:

``` bash
sudo tail -f /var/log/audit/audit.log | grep -i denied
```

## 2026 Best Practices and Advanced Techniques

For How to Enable PHP DOM Extension in Apache on CentOS 7, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
