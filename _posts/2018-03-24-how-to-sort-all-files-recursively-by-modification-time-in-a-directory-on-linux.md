---
title: "Sort Files Recursively by Modification Time in Linux"
date: 2018-03-24 11:46:44 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-sort-all-files-recursively-by-modification-time-in-a-directory-on-linux/
---

Finding and sorting files by modification time across directories is a common task for log rotation, cleanup scripts, and audit purposes. Here are the most practical approaches.

## Using find with printf (simplest method)

The `find` command with `-printf` is the fastest and most portable approach:

``` bash
find . -type f -printf '%T@ %p\n' | sort -rn | sed 's/^[^ ]* //'
```

Break this down:

- `find . -type f` — find all regular files recursively from current directory
- `-printf '%T@ %p\n'` — print modification time as Unix timestamp (`%T@`) and path (`%p`)
- `sort -rn` — sort numerically in reverse order (newest first); use `-n` for oldest first
- `sed 's/^[^ ]* //'` — remove the timestamp, leaving just the path

Example output:

    ./logs/app.log
    ./cache/temp.txt
    ./data/old_backup.tar.gz

## Using find with -stat (if printf isn’t available)

On some BSD systems or when `-printf` isn’t supported:

``` bash
find . -type f -exec stat --printf="%Y %n\n" {} \; | sort -rn | sed 's/^[^ ]* //'
```

This is slower because it spawns `stat` for each file, but works universally.

## Using find with ls (legacy approach)

``` bash
find . -type f -exec ls -lt {} + | awk '{print $NF}'
```

This is less efficient but works when other tools fail.

## Using a more readable alternative with awk

If you want human-readable timestamps alongside the files:

``` bash
find . -type f -printf '%T+ %p\n' | sort -r | awk '{$1=""; print $0}' | sed 's/^ //'
```

Or to include the timestamp:

``` bash
find . -type f -printf '%T@ %Tc %p\n' | sort -rn | cut -d' ' -f1-6 --complement
```

## Limiting depth and file type

For more control, add these options to `find`:

``` bash
# Only search 2 levels deep
find . -maxdepth 2 -type f -printf '%T@ %p\n' | sort -rn

# Only find files matching a pattern
find . -type f -name "*.log" -printf '%T@ %p\n' | sort -rn

# Exclude certain directories
find . -type f -not -path "*/node_modules/*" -printf '%T@ %p\n' | sort -rn
```

## Practical examples

Show 10 most recently modified files:

``` bash
find . -type f -printf '%T@ %p\n' | sort -rn | head -10 | sed 's/^[^ ]* //'
```

Find files modified more than 30 days ago and sort them:

``` bash
find . -type f -mtime +30 -printf '%T@ %p\n' | sort -rn | sed 's/^[^ ]* //'
```

Format output with human-readable dates:

``` bash
find . -type f -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort -r
```

## Performance notes

- `-printf` is faster than `-exec stat` because it doesn’t fork a process per file
- For very large directory trees, pipe to `head -n X` immediately after `find` to avoid sorting thousands of files unnecessarily
- On NFS mounts or slow storage, `find` itself may be the bottleneck; consider using `locate` with a recent database if available

## 2026 Best Practices and Advanced Techniques

For Sort Files Recursively by Modification Time in Linux, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
