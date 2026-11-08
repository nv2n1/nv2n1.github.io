---
title: "Redirect Output to Multiple Files with tee and Monitoring"
date: 2018-03-24 11:47:46 +0000
layout: post
canonical: https://www.systutorials.com/how-to-redirect-anything-written-on-a-file-to-another-file-in-linux/
---

When you need writes to one or more files to automatically go to another file, you have several options depending on your exact use case. The most common scenario is capturing output from commands, monitoring file changes, or duplicating writes across multiple destinations.

## Using tee for Command Output Duplication

The `tee` command duplicates standard input to both stdout and one or more files simultaneously. This is useful when you want output from a command to go to multiple places:

``` bash
echo "hello" | tee a.txt b.txt c.txt
```

This writes “hello” to all three files. If files exist and you want to append instead of overwrite:

``` bash
echo "hello" | tee -a a.txt b.txt c.txt
```

You can also combine `tee` with command pipelines to redirect output and process it further:

``` bash
cat data.txt | tee output.txt | grep "pattern"
```

This writes the full content to `output.txt` while simultaneously piping it through `grep`.

## Monitoring File Changes with inotifywait

If your actual requirement is to monitor when files a.txt or b.txt are written to and automatically copy those changes to c.txt, use `inotifywait`:

``` bash
#!/bin/bash
inotifywait -m -e modify a.txt b.txt |
while read path action file; do
    cat a.txt b.txt >> c.txt
done
```

This watches both files for modifications and appends their combined contents to c.txt whenever either changes. The `-m` flag keeps monitoring continuously; `-e modify` specifies the event type.

For a more selective approach that only captures new writes:

``` bash
#!/bin/bash
tail -f a.txt b.txt | tee -a c.txt
```

This tails both files and writes everything to c.txt. This works well if a.txt and b.txt are actively being written to (like log files).

## Using strace to Intercept File Operations

For advanced cases where you need to intercept all writes to specific files at the system level:

``` bash
strace -e write -o /tmp/trace.log -p <pid>
```

This traces all write operations from a process and logs them. Extract the data programmatically afterward.

## Practical Example: Logging Multiple Sources

A common real-world scenario is combining logs from multiple applications:

``` bash
#!/bin/bash
while true; do
    {
        cat a.txt
        cat b.txt
    } | sort | uniq >> c.txt
    sleep 5
done
```

Or using named pipes for real-time aggregation:

``` bash
mkfifo fifo_a fifo_b
cat a.txt > fifo_a &
cat b.txt > fifo_b &
paste fifo_a fifo_b | tee c.txt
rm fifo_a fifo_b
```

## Key Differences Between Approaches

- **tee**: Best for command output; simple and immediate
- **inotifywait**: Best for monitoring file changes in real-time
- **tail -f**: Best for log aggregation
- **strace**: Only when you need system-level interception

Choose based on whether you’re redirecting command output, monitoring file changes, or aggregating logs. For most cases, `tee` with multiple file arguments or piping through `tee -a` provides the simplest solution.

## 2026 Best Practices and Advanced Techniques

For Redirect Output to Multiple Files with tee and Monitoring, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
