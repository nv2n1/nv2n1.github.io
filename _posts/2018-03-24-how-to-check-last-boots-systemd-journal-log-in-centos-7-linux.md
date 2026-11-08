---
title: "Viewing the Previous Boot\u2019s systemd Journal on CentOS 7"
date: 2018-03-24 11:53:12 +0000
modified: 2026-04-12 16:30:37 +0000
author: "David Yang"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-check-last-boots-systemd-journal-log-in-centos-7-linux/
---

The command `journalctl -b -1` should show the previous boot’s journal, but on many systems it returns:

    Failed to look up boot -1: No such boot ID in journal

This happens because persistent journal storage isn’t enabled by default. Without it, journald only keeps logs in volatile memory (`/run/log/journal`), which gets cleared on shutdown.

## Enable Persistent Journal Storage

To fix this, enable persistent logging by creating the journal directory and restarting the service:

``` bash
mkdir -p /var/log/journal
systemd-tmpfiles --create --prefix /var/log/journal
systemctl restart systemd-journald
```

The `systemd-tmpfiles` command sets proper permissions and ownership. Verify the directory exists:

``` bash
ls -ld /var/log/journal
```

You should see output like:

    drwxr-sr-x+ 3 root systemd-journal 4096 Jan 15 10:42 /var/log/journal

## Configure journald for Persistence

Edit `/etc/systemd/journald.conf` to ensure persistence is configured:

``` bash
# Uncomment or add these lines
Storage=persistent
MaxRetentionSec=30day
```

Then restart journald:

``` bash
systemctl restart systemd-journald
```

## Viewing Boot Logs

Once persistent storage is enabled, you can view logs from previous boots:

``` bash
# Show all available boots
journalctl --list-boots

# View previous boot's logs
journalctl -b -1

# View second-to-last boot
journalctl -b -2

# View current boot
journalctl -b 0

# View logs from a specific boot ID
journalctl -b <boot-id>
```

The `--list-boots` output shows the boot offset, boot ID, and timestamp:

    -5 a1b2c3d4e5f6g7h8 Mon 2026-01-10 14:32:15 UTC—Mon 2026-01-10 16:45:22 UTC
    -4 f7g8h9i0j1k2l3m4 Mon 2026-01-11 08:10:05 UTC—Mon 2026-01-11 12:30:18 UTC
    -1 xyz789abc123def0 Sat 2026-01-15 09:15:42 UTC—Sat 2026-01-15 10:42:08 UTC
     0 m4n5o6p7q8r9s0t1 Sat 2026-01-15 10:42:15 UTC—Sat 2026-01-15 17:30:45 UTC

## Filter and Search Boot Logs

You can combine boot selection with filters:

``` bash
# View errors from previous boot
journalctl -b -1 -p err

# View a specific service's logs from last boot
journalctl -b -1 -u sshd

# View logs with timestamps in a specific time range
journalctl -b -1 --since "10:00:00" --until "11:00:00"

# Follow logs with priority filtering
journalctl -b -1 -p warning..err
```

Priority levels are: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`.

## Disk Space Considerations

Persistent journals can consume significant disk space over time. Control disk usage with these settings in `/etc/systemd/journald.conf`:

    # Limit journal to 1GB
    SystemMaxUse=1G

    # Keep minimum of 100MB free
    SystemKeepFree=100M

    # Maximum log file size
    SystemMaxFileSize=100M

    # Retention period (0 = unlimited)
    MaxRetentionSec=30day

Restart journald after changes:

``` bash
systemctl restart systemd-journald
```

Check current journal disk usage:

``` bash
journalctl --disk-usage
```

This command shows the actual disk consumption and the configured limits. On systems with limited disk space, adjust `SystemMaxUse` appropriately while balancing log retention needs.

## 2026 Best Practices and Advanced Techniques

For Viewing the Previous Boot’s systemd Journal on CentOS 7, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
