---
title: "Clearing Linux Filesystem Caches: Methods and Best Practices"
date: 2013-07-12 16:32:30 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /linux-flushing-file-system-caches/
---

Dropping file system caches reclaims memory for applications. Linux kernels 2.6.16+ provide a `/proc/sys/vm/drop_caches` interface to trigger cache eviction. This is safe — the kernel only frees clean cache pages and unreferenced inodes/dentries. Dirty data stays in memory until explicitly synced to disk.

## Two-Step Cache Drop Process

### Step 1: Sync Dirty Data to Disk

Before dropping caches, flush any pending writes to storage:

``` bash
sync
```

This ensures dirty buffers and metadata reach the disk. Omitting this step means those pages won’t be freed by `drop_caches` — they’ll remain in memory until later writes occur.

### Step 2: Drop the Caches

Echo a value to `/proc/sys/vm/drop_caches` to signal the kernel to drop specific cache types:

``` bash
echo 3 > /proc/sys/vm/drop_caches
```

The value determines what gets freed:

- **1**: Page cache only
- **2**: Inode and dentry caches only
- **3**: Page cache, inode, and dentry caches (all three)

Typical practice is to use `3` for maximum reclamation, though you can be selective if needed. For example, drop only the page cache on a system with many directory listings in use:

``` bash
echo 1 > /proc/sys/vm/drop_caches
```

## Practical Considerations

**Why sync first?** The kernel won’t evict dirty pages. If you skip `sync`, unwritten filesystem buffers remain cached and count against your free memory.

**Requires root.** You must have write access to `/proc/sys/vm/drop_caches`. Use `sudo` if necessary:

``` bash
sudo sh -c 'sync && echo 3 > /proc/sys/vm/drop_caches'
```

**Not destructive to data.** Cache drops never cause data loss. Unflushed writes stay in memory; the operation only removes clean pages that can be re-read from disk.

**Checking cache usage.** Examine current memory state before and after:

``` bash
free -h
```

Or inspect detailed cache breakdown:

``` bash
cat /proc/meminfo | grep -E "^Buffers|^Cached"
```

## When to Drop Caches

Common scenarios include:

- Benchmarking disk I/O (start with known cache state)
- Freeing memory after large file operations
- Troubleshooting memory pressure on systems with minimal swap
- Testing application behavior under low-cache conditions

**Avoid routine use in production.** Dropping caches degrades performance for a period afterward since frequently accessed data must be re-cached. On systems with adequate memory, the kernel naturally manages caches efficiently.

## Automated Cache Dropping

Some workloads benefit from periodic cache clearing. A systemd timer can drop caches on schedule:

**File:** `/etc/systemd/system/drop-caches.service`

``` ini
[Unit]
Description=Drop filesystem caches
After=network.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'sync && echo 3 > /proc/sys/vm/drop_caches'
```

**File:** `/etc/systemd/system/drop-caches.timer`

``` ini
[Unit]
Description=Run drop-caches service hourly

[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable --now drop-caches.timer
```

Check timer status:

``` bash
sudo systemctl list-timers drop-caches.timer
```

## Alternative: Disable Page Cache Temporarily

For specific workloads, you can reduce caching pressure without full eviction. The `O_DIRECT` flag on file opens bypasses page cache entirely (used by databases and high-performance storage applications). This is more surgical than system-wide cache drops.

## 2026 Best Practices and Advanced Techniques

For Clearing Linux Filesystem Caches: Methods and Best Practices, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
