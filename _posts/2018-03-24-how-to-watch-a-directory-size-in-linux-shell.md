---
title: "Monitor Directory Size Growth in Linux"
date: 2018-03-24 11:49:14 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-watch-a-directory-size-in-linux-shell/
---

Monitoring directory growth is essential for tracking logs, temporary files, and catching runaway disk usage before it becomes a problem. Linux offers several approaches depending on whether you need simple periodic checks, interactive exploration, or event-driven monitoring.

## Simple periodic monitoring

The `watch` command repeatedly runs a command at set intervals:

``` bash
watch -n 1 du -sh /path/to/dir
```

This updates every 1 second (`-n 1`) and shows the total size in human-readable format. Press `q` to exit. The `du` command can be resource-intensive on large directories, so if you’re monitoring frequently, increase the interval:

``` bash
watch -n 5 du -sh /var/log /tmp /home
```

This checks multiple directories every 5 seconds.

## Interactive exploration with ncdu

For deeper analysis, `ncdu` (NCurses Disk Usage) is far superior to navigating with `du` manually. It builds an interactive tree view and lets you identify which subdirectories consume the most space:

``` bash
ncdu /path/to/dir
```

Navigate with arrow keys, press `d` to delete files directly, and `q` to quit. The initial scan takes longer on large directories, but subsequent navigation is instant. Use `-o` to export results:

``` bash
ncdu -o /tmp/scan.json /var/log
ncdu -f /tmp/scan.json
```

This lets you compare scans over time.

## Event-driven monitoring

For production systems, trigger actions when files are added or removed:

``` bash
inotifywait -m -e create,delete -r /var/log | while read path action file; do
    size=$(du -sh /var/log | cut -f1)
    echo "$(date): $action on $file, total: $size" >> /var/log/monitor.log
done
```

The `-m` flag keeps `inotifywait` running continuously, `-e` specifies events, and `-r` watches recursively. This is useful for alerting when log directories grow unexpectedly.

## Filesystem-wide monitoring

To see overall usage across mounted filesystems:

``` bash
df -h
```

For a sorted view of which filesystems are filling up fastest:

``` bash
df -h | sort -k5 -rn
```

This sorts by percentage used (column 5) in reverse numeric order.

## Monitoring with alerts

Combine `du` with a cron job to alert when a directory exceeds a threshold:

``` bash
#!/bin/bash
dir="/var/log"
limit=$((10 * 1024 * 1024))  # 10GB in bytes
size=$(du -sb "$dir" | cut -f1)

if [ $size -gt $limit ]; then
    echo "Warning: $dir is $(( size / 1024 / 1024 ))MB" | mail -s "Disk alert" admin@example.com
fi
```

Run this via cron:

``` bash
0 * * * * /usr/local/bin/check-disk-usage.sh
```

This checks hourly and emails alerts when thresholds are exceeded.

## Performance considerations

For very large directories (millions of files), `du` becomes slow. Use `ncdu` for interactive analysis or consider hardware-backed solutions like quotas. On production systems, avoid running `du -s` too frequently—cache results or increase `watch` intervals to every 30 seconds or more.

## 2026 Best Practices and Advanced Techniques

For Monitor Directory Size Growth in Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
