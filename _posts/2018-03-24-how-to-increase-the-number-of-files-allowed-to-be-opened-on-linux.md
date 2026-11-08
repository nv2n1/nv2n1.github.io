---
title: "Increase the Maximum Open Files Limit on Linux"
date: 2018-03-24 11:43:23 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-increase-the-number-of-files-allowed-to-be-opened-on-linux/
---

When you hit the open files limit on Linux, you’ll see errors like “Too many open files” — typically when running applications that create many temporary file handles. The default limit is often 1024, which isn’t enough for resource-heavy workloads.

Check your current limit:

``` bash
ulimit -n
```

## Understanding soft and hard limits

Linux maintains two types of file descriptor limits:

- **Soft limit**: The current limit a user can reach. Users can increase it up to the hard limit themselves.
- **Hard limit**: The absolute maximum. Only root can raise this.

The kernel also has a system-wide limit you can check:

``` bash
cat /proc/sys/fs/file-max
```

## Setting limits in /etc/security/limits.conf

The persistent way to change limits is through `/etc/security/limits.conf`. This file is read by PAM (Pluggable Authentication Modules) at login.

Edit the file:

``` bash
sudo nano /etc/security/limits.conf
```

Add these lines at the end (before any `@include` statements):

    *                soft   nofile           65536
    *                hard   nofile           65536

The `*` applies to all users. To set limits for a specific user:

    username       soft   nofile           65536
    username       hard   nofile           65536

Or for a group:

    @groupname     soft   nofile           65536
    @groupname     hard   nofile           65536

Changes take effect on next login. Test with a new shell session:

``` bash
ulimit -n
```

## Setting limits for specific services

For systemd services, use the `LimitNOFILE` directive in the service file or drop-in directory:

``` bash
sudo mkdir -p /etc/systemd/system/myservice.service.d
```

Create `/etc/systemd/system/myservice.service.d/limits.conf`:

``` ini
[Service]
LimitNOFILE=65536
```

Then reload and restart:

``` bash
sudo systemctl daemon-reload
sudo systemctl restart myservice
```

## Temporary limits (current session only)

To change the limit for your current shell only:

``` bash
ulimit -n 65536
```

This doesn’t persist after logout.

## Other commonly adjusted limits

While you’re configuring limits, you may need to adjust related settings:

    *                soft   nproc            4096
    *                hard   nproc            4096
    *                soft   memlock          unlimited
    *                hard   memlock          unlimited

- `nproc`: Maximum number of processes per user
- `memlock`: Maximum memory that can be locked (useful for databases)
- `nofile`: Maximum open file descriptors (what we’re focusing on)

## System-wide kernel limits

For high-traffic servers, you may also need to increase the kernel-level limit:

``` bash
sudo sysctl fs.file-max=2097152
```

To make this permanent, add it to `/etc/sysctl.conf`:

    fs.file-max=2097152

Then apply:

``` bash
sudo sysctl -p
```

## Choosing the right value

Common recommendations:

- **Development**: 65536 is usually sufficient
- **Production databases**: 65536 to 1048576
- **High-concurrency services**: 1048576 or higher

Monitor actual usage with:

``` bash
lsof -u username | wc -l
```

Or check system-wide:

``` bash
cat /proc/sys/fs/file-nr
```

This shows: `<used> <unused> <max>`. If used is consistently near max, increase the limit further.

## Verify limits are applied

After making changes, verify with a fresh login:

``` bash
ulimit -a
```

This shows all resource limits for your session.

## 2026 Best Practices and Advanced Techniques

For Increase the Maximum Open Files Limit on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
