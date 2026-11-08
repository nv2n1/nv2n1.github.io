---
title: "Getting Millisecond-Precision Timestamps on Linux"
date: 2018-03-24 11:41:00 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-time-at-millisecond-level-on-linux-with-command-line/
---

If you need millisecond precision timestamps from the command line, there are several approaches depending on your use case and system requirements.

## Using date with %3N

The simplest and most reliable method on modern GNU coreutils (8.32+) is:

``` bash
date +%s%3N
```

This outputs seconds since epoch followed by exactly three digits of nanosecond precision (milliseconds). Example output: `1704067200123`

For UTC instead of local time:

``` bash
date -u +%s%3N
```

## Full nanosecond precision with %N

If you need higher precision, use `%N` for nanoseconds:

``` bash
date +%s.%N
```

Output: `1704067200.123456789`

Keep in mind that while the format provides nanosecond digits, actual system clock precision varies. Most modern systems deliver microsecond or better precision, but the least significant digits may not be meaningful. Check your hardware timer capabilities with:

``` bash
cat /proc/sys/kernel/clocksource
```

## ISO 8601 format with milliseconds

For logs that need both human-readable dates and millisecond precision:

``` bash
date -u '+%Y-%m-%dT%H:%M:%S.%3NZ'
```

Output: `2024-01-01T12:00:00.123Z`

For fractional seconds in other formats:

``` bash
date -u '+%Y-%m-%d %H:%M:%S.%3N' 
```

## Measuring elapsed time

To measure duration in milliseconds:

``` bash
start=$(date +%s%3N)
# ... do something ...
end=$(date +%s%3N)
echo "Elapsed: $((end - start)) ms"
```

## Using Python for programmatic access

In scripts where you need direct system time without shell parsing:

``` python
import time
print(int(time.time() * 1000))  # milliseconds since epoch
```

Or with datetime for formatted output:

``` python
from datetime import datetime, timezone
print(int(datetime.now(timezone.utc).timestamp() * 1000))
```

## Logging with millisecond timestamps

For application logs:

``` bash
echo "$(date -u '+%Y-%m-%d %H:%M:%S.%3N') - Event occurred" >> app.log
```

In structured logging (JSON):

``` bash
jq -n --arg timestamp "$(date -u '+%Y-%m-%dT%H:%M:%S.%3NZ')" \
  '{timestamp: $timestamp, event: "startup", level: "info"}'
```

## Performance considerations

If you’re executing timestamps in tight loops:

**Cache the timestamp outside the loop:**

``` bash
now=$(date +%s%3N)
for item in "${items[@]}"; do
    echo "$now: processing $item"
done
```

**Use a single date call with multiple format specifiers:**

``` bash
read -r epoch ms <<< "$(date +%s\ %3N)"
# $epoch = 1704067200, $ms = 123
```

**For high-frequency operations (\>1000/sec), move timing to the application layer.** Direct system calls from C, Python, or Go are significantly cheaper than spawning date processes.

## UTC vs local time

The epoch timestamp (`%s`) is always UTC internally. However, when formatting for display, explicitly specify UTC to avoid confusion across distributed systems:

``` bash
# Local time (confusing for logs)
date +%s%3N

# UTC (recommended for all logging)
date -u +%s%3N
```

This ensures consistent timestamps regardless of system timezone configuration.

## Checking system clock precision

To verify what precision your system actually supports:

``` bash
# See available clock sources
cat /proc/sys/kernel/clocksource

# Check NTP/chrony status (systemd systems)
timedatectl status
```

On most modern systems with NTP synchronization, you’ll get microsecond or better precision. Virtual machines may have coarser resolution depending on hypervisor configuration.

## 2026 Best Practices and Advanced Techniques

For Getting Millisecond-Precision Timestamps on Linux, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
