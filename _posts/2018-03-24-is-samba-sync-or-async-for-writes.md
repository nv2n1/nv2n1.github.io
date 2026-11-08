---
title: "Understanding Samba\u2019s Write Behavior: Sync vs Async"
date: 2018-03-24 11:53:16 +0000
modified: 2026-04-12 16:46:31 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /is-samba-sync-or-async-for-writes/
---

Samba defaults to asynchronous writes for performance reasons, but the behavior is fully configurable. Understanding these options is critical when data integrity matters more than speed.

### Default Async Behavior

By default, Samba writes are asynchronous. When `smbd` receives a write request, it:

1.  Copies data to a memory buffer
2.  Returns success to the client immediately
3.  Flushes the buffer to disk later via the kernel

This approach maximizes throughput but risks data loss if the system crashes between buffer write and disk flush.

### Configurable Synchronous Writes

Windows clients can request synchronous writes via the `FILE_FLAG_WRITE_THROUGH` flag in the CreateFile API. Samba honors this flag through two configuration options:

**strict sync** (default: no)\
: When set to `yes`, Samba respects the `FILE_FLAG_WRITE_THROUGH` flag from clients. Writes are flushed to disk before returning to the caller. This is slow but provides per-request control.

**sync always** (default: no)\
: When set to `yes`, all writes execute synchronously regardless of client flags. This guarantees data hits disk before acknowledgment but severely impacts performance. Requires `strict sync = yes` to function.

### Configuration Matrix

| strict sync | sync always | Client flag | Actual sync      |
|-------------|-------------|-------------|------------------|
| no          | no          | no          | Async            |
| no          | no          | yes         | Async            |
| yes         | no          | no          | Async            |
| yes         | no          | yes         | Sync (slow)      |
| yes         | yes         | no          | Sync (very slow) |
| yes         | yes         | yes         | Sync (very slow) |

### Practical Considerations

**For general file sharing:** Leave both options at defaults. The kernel’s dirty page writeback (typically every 5-30 seconds) provides reasonable safety without sacrificing performance.

**For databases or critical data:** Use `strict sync = yes` with `sync always = no`. This allows clients to opt-in to synchronous writes via the `FILE_FLAG_WRITE_THROUGH` flag when they need guarantees. Most database applications set this flag automatically.

**For maximum data safety:** Use `strict sync = yes` and `sync always = yes`. Accept the performance penalty. This is rarely necessary outside highly regulated environments.

### Relevant Samba Configuration Example

``` ini
[global]
    strict sync = yes
    sync always = no

[critical_share]
    path = /var/data/critical
    read only = no
    strict sync = yes
    sync always = yes
```

### Monitoring Sync Impact

Check your actual disk write patterns with `iostat`:

``` bash
iostat -x 1
```

Look for high `await` times when sync is enabled. Compare with async baselines to quantify the performance cost in your environment.

### Kernel-Level Considerations

Modern Linux uses `noatime` and `relatime` mount options to reduce metadata writes. Verify your Samba share’s underlying filesystem mount options:

``` bash
mount | grep samba_mount
```

Consider `nodiratime` as well to prevent directory timestamp updates on reads.

Also be aware that `sync always = yes` forces synchronous writes at the system call level, bypassing kernel optimizations. This is much slower than relying on the kernel’s intelligent writeback strategy.

## 2026 Best Practices and Advanced Techniques

For Understanding Samba’s Write Behavior: Sync vs Async, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
