---
title: "MySQL and MariaDB Default Data Directories on CentOS 7"
date: 2018-03-24 11:53:59 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/where-is-mysql-mariadb-storage-location-by-default-on-centos-7/
---

The default data directory for MySQL and MariaDB installed from official repositories on modern distributions is:

    /var/lib/mysql

This applies to CentOS 7, Rocky Linux 9, Fedora, and most RHEL-based systems.

## Finding the Data Directory Programmatically

If you’ve customized your installation or need to verify the exact location, there are several reliable methods.

### Query MariaDB/MySQL Configuration

The most straightforward approach is to ask the database server directly:

``` bash
mysql -u root -p -e "SELECT @@datadir;"
```

Or if you have `mysqladmin` available:

``` bash
mysqladmin -u root -p variables | grep datadir
```

Both commands return the configured data directory without needing root access to the system.

### Check Configuration Files

MariaDB and MySQL read configuration from multiple sources. Check these files in order of precedence:

``` bash
cat /etc/mysql/my.cnf
cat /etc/mysql/mariadb.conf.d/*.cnf
cat /etc/my.cnf
cat /etc/my.cnf.d/*.cnf
```

Look for the `datadir` parameter in the `[mysqld]` section:

``` ini
[mysqld]
datadir=/var/lib/mysql
socket=/var/run/mysqld/mysqld.sock
```

### Inspect Open Files via /proc

If the database is running but you can’t query it, you can examine the mysqld process’s open file descriptors:

``` bash
ps aux | grep mysqld
```

This returns output like:

    mysql    25403  1.0 17.2 1322220 174948 ?  Ssl  Aug31 178:10 /usr/sbin/mysqld

Note the process ID (25403 in this example), then inspect its open files:

``` bash
ls -lha /proc/25403/fd | grep mysql
```

Example output:

    lrwx------. 1 mysql mysql 64 Sep 12 11:43 83 -> /var/lib/mysql/my_wp2/wp_links.MYI
    lrwx------. 1 mysql mysql 64 Sep 12 11:43 84 -> /var/lib/mysql/my_wp2/wp_links.MYD

The symlinks reveal the actual storage location.

## Custom Data Directories

If you’ve moved the data directory to a different location (common for performance tuning or when `/var` space is limited), verify the change was properly applied:

``` bash
systemctl status mariadb
grep -r "datadir" /etc/mysql/ /etc/my.cnf.d/
```

Ensure the directory is owned by the mysql user and has proper permissions:

``` bash
ls -ld /path/to/datadir
chown -R mysql:mysql /path/to/datadir
chmod 750 /path/to/datadir
```

After changing the data directory, restart the service and verify the symlinks in `/proc` reflect the new location.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For MySQL and MariaDB Default Data Directories on CentOS 7, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
