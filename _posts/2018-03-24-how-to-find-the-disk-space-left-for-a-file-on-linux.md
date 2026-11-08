---
title: "How to Check Available Disk Space on Linux"
date: 2018-03-24 08:19:16 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-find-the-disk-space-left-for-a-file-on-linux/
---

When a program appends data to a file, you need to know how much space remains on the partition containing that file. This determines whether the file can grow or if you’re about to hit a capacity limit.

### Quick answer

To find available space for a file, use `df`:

``` bash
df -B1 /mnt/logs/app-log.log | tail -1 | awk '{print $4}'
```

This outputs available space in bytes. Replace `/mnt/logs/app-log.log` with your target file.

### Understanding the output

The `df` command without the file argument shows all mounted filesystems:

``` bash
$ df -B1 /mnt/logs/app-log.log
Filesystem     1B-blocks        Used   Available Use% Mounted on
/dev/sda1    1099511627776 549755813888 549755813888  50% /mnt
```

Breaking down the output:

- **Filesystem**: The actual device or mount
- **1B-blocks**: Total capacity in bytes
- **Used**: Bytes consumed
- **Available**: Bytes remaining (what we care about)
- **Use%**: Percentage of capacity used
- **Mounted on**: The mount point

The `tail -1` grabs the last line (skipping headers), and `awk '{print $4}'` extracts the available space column.

### More practical approaches

**Human-readable format:**

``` bash
df -h /mnt/logs/app-log.log | tail -1 | awk '{print "Available:", $4}'
```

Output: `Available: 256G`

**Check if space is sufficient before writing:**

``` bash
required_bytes=10737418240  # 10GB in bytes
available=$(df -B1 /mnt/logs/app-log.log | tail -1 | awk '{print $4}')

if [ "$available" -lt "$required_bytes" ]; then
    echo "Insufficient space: need $required_bytes bytes, have $available"
    exit 1
fi
```

**Get both used and available space:**

``` bash
df -B1 /mnt/logs/app-log.log | tail -1 | awk '{printf "Used: %d bytes\nAvailable: %d bytes\n", $3, $4}'
```

### Using stat for file-specific info

While `df` shows partition space, `stat` displays the actual file’s properties:

``` bash
stat /mnt/logs/app-log.log | grep -E "Access|Modify|Change"
```

This shows file modification times, useful for understanding when files were last written.

### Monitoring disk usage over time

For files that grow continuously, use `watch` to monitor available space:

``` bash
watch -n 5 'df -h /mnt/logs/app-log.log | tail -1'
```

Updates every 5 seconds. Press `q` to exit.

### Common gotchas

**Reserved space**: Linux reserves 5% of filesystem capacity (typically) for the root user. Non-root users see less available space than the actual free space:

``` bash
df /mnt/logs/app-log.log  # Shows available to regular user
sudo df /mnt/logs/app-log.log  # Shows reserved space included
```

**Inode limits**: Disk space isn’t the only constraint. Systems can run out of inodes before bytes:

``` bash
df -i /mnt/logs/app-log.log
```

If “IUse%” approaches 100%, you’ll fail to create files despite available bytes.

**Mounted filesystems**: The file’s partition is determined by its mount point. Symbolic links report the target file’s partition:

``` bash
df /path/to/symlink  # Reports space for the target, not the symlink location
```

## 2026 Best Practices and Advanced Techniques

For How to Check Available Disk Space on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
