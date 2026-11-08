---
title: "Hosting Multiple Websites on Apache with Virtual Hosts"
date: 2018-03-24 11:47:51 +0000
layout: post
canonical: https://www.systutorials.com/how-to-host-multiple-websites-on-a-apache-linux-web-server/
---

Virtual hosts allow you to serve multiple websites from a single Apache server and IP address. This is the standard approach for shared hosting and cost-effective server deployments.

## Basic Virtual Host Setup

The foundation of multi-site hosting on Apache is the VirtualHost directive. Each domain needs its own block that specifies where its files live and how Apache should handle requests for it.

Create a virtual hosts configuration file. Modern practice is to use separate files in `/etc/httpd/conf.d/` rather than editing the main httpd.conf:

``` bash
sudo nano /etc/httpd/conf.d/example1.com.conf
```

Add this for your first domain:

``` apache
<VirtualHost *:80>
    ServerName example1.com
    ServerAlias www.example1.com
    DocumentRoot /var/www/example1.com/public_html

    <Directory /var/www/example1.com/public_html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/example1.com_error.log
    CustomLog /var/log/httpd/example1.com_access.log combined
</VirtualHost>
```

Create a second configuration file for your second domain:

``` bash
sudo nano /etc/httpd/conf.d/example2.com.conf
```

``` apache
<VirtualHost *:80>
    ServerName example2.com
    ServerAlias www.example2.com
    DocumentRoot /var/www/example2.com/public_html

    <Directory /var/www/example2.com/public_html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/example2.com_error.log
    CustomLog /var/log/httpd/example2.com_access.log combined
</VirtualHost>
```

## Create Document Root Directories

Set up the actual directories where your website files will live:

``` bash
sudo mkdir -p /var/www/example1.com/public_html
sudo mkdir -p /var/www/example2.com/public_html
```

Create a test file to verify the configuration works:

``` bash
sudo bash -c 'echo "Example 1 Site" > /var/www/example1.com/public_html/index.html'
sudo bash -c 'echo "Example 2 Site" > /var/www/example2.com/public_html/index.html'
```

Set proper permissions (adjust user/group as needed for your setup):

``` bash
sudo chown -R apache:apache /var/www/example1.com
sudo chown -R apache:apache /var/www/example2.com
sudo chmod -R 755 /var/www
```

## Verify and Restart Apache

Test the Apache configuration for syntax errors before restarting:

``` bash
sudo apachectl configtest
```

You should see `Syntax OK`. If there are errors, fix them before proceeding.

Restart Apache to apply the new configuration:

``` bash
sudo systemctl restart httpd
```

Check that Apache started successfully:

``` bash
sudo systemctl status httpd
```

## Important Considerations

**Domain vs. www subdomain**: `example1.com` and `www.example1.com` are technically different domains. Use `ServerAlias` to handle both from a single VirtualHost block, as shown above. Without the alias, requests to the non-www version will fail.

**DNS Configuration**: Ensure both domain names point to your server’s IP address via A records in your DNS provider’s control panel.

**SSL/HTTPS**: If using HTTPS (which you should), you need separate virtual host blocks for port 443 with `SSLEngine on` and certificate paths. Let’s Encrypt with Certbot makes this straightforward:

``` bash
sudo certbot --apache -d example1.com -d www.example1.com
```

**Separate Log Files**: Keeping error and access logs separate per domain makes debugging and monitoring much easier.

**File Permissions**: Apache runs as the `apache` user on RHEL-based systems. Ensure it has read access to your document root directories.

## Scaling to Many Domains

For servers hosting dozens of domains, template-based approaches with configuration management tools (Ansible, Puppet) reduce manual work. Alternatively, use a control panel like cPanel or Plesk if you’re providing hosting services.

## Troubleshooting

If a domain isn’t working:

1.  Verify DNS points to the correct IP: `dig example1.com`
2.  Check the error log: `sudo tail -f /var/log/httpd/example1.com_error.log`
3.  Confirm the DocumentRoot directory exists and Apache can read it
4.  Verify no syntax errors with `apachectl configtest`

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Hosting Multiple Websites on Apache with Virtual Hosts with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Hosting Multiple Websites on Apache with Virtual Hosts. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
