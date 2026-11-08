---
title: "Getting File Modification Time on Linux"
date: 2018-03-24 11:53:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-mtime-of-a-file-on-linux/
---

The modification time (mtime) indicates when a file’s content was last changed. This is critical for scripting, backups, logging, and dependency tracking in builds.

## Using stat

The `stat` command is the most reliable tool for retrieving mtime programmatically:

``` bash
stat -c %Y filename
```

This outputs the Unix timestamp (seconds since epoch). For nanosecond precision:

``` bash
stat -c %Y.%Z filename
```

You can also view all timestamps in human-readable format:

``` bash
stat filename
```

This shows Access, Modify, and Change times. The Modify time is the mtime you need.

For batch operations, use `--printf` to parse multiple files:

``` bash
stat -c '%n: %Y' *.log
```

## Using ls

The `ls` command works but is less reliable for scripting:

``` bash
ls -l --time-style=full-iso filename
```

Output includes the full ISO timestamp. The `--time-style` option supports several formats:

- `full-iso`: Full ISO format
- `long-iso`: ISO date without seconds
- `+%s`: Unix timestamp (though `stat` is better for this)

For quick human-readable output:

``` bash
ls -lh filename
```

## Using date

You can convert mtime to a readable format with `date`:

``` bash
date -r filename '+%Y-%m-%d %H:%M:%S'
```

This is useful for reports or logging. Combine with other tools:

``` bash
find . -name "*.txt" -exec date -r {} '+%Y-%m-%d %H:%M:%S: {}' \;
```

## Finding Files by mtime

Common patterns for time-based searches:

``` bash
# Files modified in the last 24 hours
find . -mtime -1

# Files not modified in 30 days
find . -mtime +30

# Files modified between 1-7 days ago
find . -mtime -7 -mtime +1

# Files modified in the last hour (in minutes)
find . -mmin -60
```

## Filesystem Considerations

Modern Linux filesystems (ext4, XFS, Btrfs) all track mtime at the second granularity by default. For nanosecond-precision timestamps, ensure your filesystem supports it—most modern configurations do.

If you’re running high-performance systems with heavy I/O, mounting with `noatime` or `relatime` reduces unnecessary metadata writes:

``` bash
mount -o remount,relatime /
```

This still updates atime (access time) for `stat` calls but not for every read operation, balancing functionality with performance.

## Scripting Examples

Get mtime and compare files:

``` bash
#!/bin/bash
mtime1=$(stat -c %Y file1.txt)
mtime2=$(stat -c %Y file2.txt)

if [ "$mtime1" -gt "$mtime2" ]; then
  echo "file1.txt is newer"
else
  echo "file2.txt is newer"
fi
```

Check if a file was modified since a known timestamp:

``` bash
last_mtime=$(stat -c %Y /var/log/app.log)
threshold=$(($(date +%s) - 3600))

if [ "$last_mtime" -gt "$threshold" ]; then
  echo "Log file was modified in the last hour"
fi
```

For build systems and dependency tracking, storing mtimes in a state file is standard practice:

``` bash
stat -c '%n %Y' src/* > .build_state
# Later: compare new mtimes against stored values
```

Use `stat` for scripting and automation—it’s precise, portable, and doesn’t depend on locale settings like `ls` does.

## 2026 Best Practices and Advanced Techniques

For Getting File Modification Time on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
