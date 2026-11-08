---
title: "Getting Unix Timestamps in Bash"
date: 2018-03-24 11:52:13 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-epoch-timestamp-in-bash/
---

The `date` command is your primary tool for retrieving Unix epoch timestamps. It’s available on virtually all Unix-like systems and integrates seamlessly into scripts and command pipelines.

## Basic Epoch Timestamp

``` bash
date +%s
```

This returns the number of seconds since January 1, 1970 UTC. Output looks like `1735689600`.

## Higher Precision with Nanoseconds

For microsecond or nanosecond precision, use:

``` bash
date +%s%N
```

This appends nanoseconds to the seconds value. For example: `1735689600123456789`. If you need just microseconds, pipe it through `awk`:

``` bash
date +%s%N | awk '{print substr($1, 1, 16)}'
```

This takes the first 16 digits (seconds + first 6 digits of nanoseconds).

## Calculating Script Execution Time

A common use case is measuring how long a script takes:

``` bash
start=$(date +%s)
# ... your work here ...
end=$(date +%s)
duration=$((end - start))
echo "Script took $duration seconds"
```

For sub-second precision:

``` bash
start=$(date +%s%N)
# ... your work here ...
end=$(date +%s%N)
duration=$(( (end - start) / 1000000 ))
echo "Script took $duration milliseconds"
```

## Generating Unique Filenames

Epoch timestamps are reliable for creating unique filenames without collisions:

``` bash
backup_file="/backups/data_$(date +%s).tar.gz"
tar czf "$backup_file" /var/data
```

Or with nanosecond precision for rapid iterations:

``` bash
log_file="/var/log/process_$(date +%s%N).log"
```

## Converting Epoch to Readable Date

To reverse the process and convert an epoch timestamp back to human-readable format:

``` bash
date -d @1735689600
# Output: Fri Jan 03 12:00:00 UTC 2025
```

On BSD/macOS systems, use lowercase `-f`:

``` bash
date -f %s 1735689600
```

## Epoch in Different Time Zones

By default, `date +%s` always returns UTC epoch (regardless of your local timezone). If you need the epoch for a specific timezone, set `TZ` first:

``` bash
TZ=America/New_York date +%s
```

This doesn’t change what epoch represents — it’s always UTC — but it affects how you interpret local time conversions.

## Performance Considerations

Calling `date` repeatedly in tight loops adds overhead. Cache the result when possible:

``` bash
now=$(date +%s)
for i in {1..1000}; do
    # Use $now instead of calling date each iteration
    echo "$now: Processing item $i"
done
```

For high-frequency timestamp collection in performance-critical code, consider using Bash 5.2+ with the `$EPOCHSECONDS` and `$EPOCHREALTIME` variables (if available in your shell build):

``` bash
echo $EPOCHSECONDS
echo $EPOCHREALTIME
```

These are built-in variables that avoid spawning a subprocess, making them significantly faster than calling `date`.

## Practical Example: Cache Expiration Check

``` bash
cache_file="/tmp/data.cache"
cache_max_age=$((60 * 60 * 24))  # 24 hours in seconds
current_time=$(date +%s)

if [[ -f "$cache_file" ]]; then
    cache_time=$(stat -c %Y "$cache_file")
    cache_age=$((current_time - cache_time))

    if [[ $cache_age -gt $cache_max_age ]]; then
        echo "Cache expired, refreshing..."
        # refresh logic here
    fi
fi
```

The epoch timestamp remains the most reliable and portable way to handle time operations in shell scripts across different systems and environments.

## 2026 Best Practices and Advanced Techniques

For Getting Unix Timestamps in Bash, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
