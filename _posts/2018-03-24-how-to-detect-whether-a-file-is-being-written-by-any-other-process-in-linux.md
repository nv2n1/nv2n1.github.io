---
title: "Detecting File Writes by Other Processes in Linux"
date: 2018-03-24 11:53:32 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-detect-whether-a-file-is-being-written-by-any-other-process-in-linux/
---

Several approaches exist to detect active file access in Linux, ranging from simple procfs inspection to sophisticated kernel-level tracking.

### Using lsof

The most straightforward method is `lsof` (list open files), which shows all files currently open by running processes:

``` bash
lsof /path/to/file
```

This returns process ID, user, file descriptor, and access mode. To check only write access:

``` bash
lsof -a /path/to/file -d cwd
```

For a specific file with cleaner output:

``` bash
lsof +D /path/to/directory | grep REG
```

The second column shows the process ID, and the access column (REG, CHR, DIR) indicates file type. Write mode appears as `w` in the access flags.

### Using fuser

`fuser` identifies processes accessing a file:

``` bash
fuser /path/to/file
```

Add verbosity for more details:

``` bash
fuser -v /path/to/file
```

This is lighter weight than `lsof` but provides less information.

### Checking /proc/locks

For more detailed lock information:

``` bash
cat /proc/locks | grep /path/to/file
```

This shows byte-range locks held on files. The format includes lock type (READ/WRITE), process ID, and lock range.

### Using flock and fcntl

For your own applications, use advisory locks to prevent concurrent writes:

``` bash
#!/bin/bash
LOCKFILE="/tmp/myfile.lock"
TARGETFILE="/tmp/data.txt"

(
  flock -n 9 || { echo "File is locked by another process"; exit 1; }
  # Perform write operations
  echo "data" >> "$TARGETFILE"
) 9>"$LOCKFILE"
```

In Python, the fcntl module provides the same capability:

``` python
import fcntl
import os

def write_with_lock(filepath):
    with open(filepath, 'a') as f:
        try:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            f.write("data\n")
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        except BlockingIOError:
            print("File is locked by another process")
            return False
    return True
```

### Inotify Monitoring

For real-time detection of file modifications:

``` bash
inotifywait -m -e modify,close_write /path/to/file
```

This watches for write operations and file closes. Useful for automation scripts that need to react to file changes.

``` python
import inotify_simple

inotify = inotify_simple.INotify()
watch_descriptor = inotify.add_watch('/path/to/file', inotify_simple.flags.MODIFY)

for event in inotify.read():
    print(f"File modified: {event}")
```

### eBPF-Based Monitoring

For kernel-level insights without high overhead, use eBPF tools. `opensnoop` and `writetracer` from the bcc toolkit track file access at the syscall level:

``` bash
opensnoop -f /path/to/file
writetracer /path/to/file
```

These capture system calls in real-time with minimal performance impact.

### Practical Considerations

**Advisory vs Mandatory Locks**: Linux primarily uses advisory locks—the kernel doesn’t enforce them unless all applications cooperate. Mandatory locks require mount-time configuration and are rarely used in modern systems.

**Race Conditions**: Between checking lock status and performing operations, another process might acquire the lock. Always use atomic locking mechanisms (fcntl, flock) rather than checking then writing.

**File Descriptors**: Check `/proc/[PID]/fd/` to see what files a specific process has open, useful for debugging:

``` bash
ls -l /proc/$(pidof targetprocess)/fd/
```

**Performance**: `lsof` can be slow on systems with thousands of open files. For monitoring, prefer `inotify` or eBPF tools.

Choose the method based on your use case: `lsof` for quick checks, fcntl/flock for application-level coordination, and inotify/eBPF for continuous monitoring.

## 2026 Best Practices and Advanced Techniques

For Detecting File Writes by Other Processes in Linux, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
