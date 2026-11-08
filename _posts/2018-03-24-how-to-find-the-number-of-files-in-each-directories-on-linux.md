---
title: "Count Files in Each Linux Subdirectory"
date: 2018-03-24 11:44:39 +0000
modified: 2026-04-12 16:45:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-the-number-of-files-in-each-directories-on-linux/
---

When you need to audit disk usage or understand directory structure, counting files in each subdirectory is a common task. This is especially useful when dealing with large directory trees where you need a quick overview of distribution.

## The Basic Approach

The simplest method uses a loop with `find` and `wc`:

``` bash
for i in */; do
  echo "$i: $(find "$i" -type f | wc -l)"
done
```

This iterates through each subdirectory and counts regular files. The `*/` glob pattern is safer than `ls -1` because it handles whitespace and special characters in filenames correctly.

## More Robust Solutions

**Using `find` alone without a loop:**

``` bash
find . -maxdepth 2 -type f -printf '%h\n' | sort | uniq -c
```

This finds all files up to 2 levels deep, prints their parent directory, sorts, and counts occurrences. It’s faster for large trees since it doesn’t spawn multiple `find` processes.

**For deeper recursion with better readability:**

``` bash
find . -type f -printf '%h\n' | sed 's|^\./||' | sort | uniq -c | sort -rn
```

The `sed` removes leading `./` for cleaner output, and the final `sort -rn` orders results by count descending.

**Using `du` for a different perspective:**

``` bash
du -s */ | sort -rn
```

While `du` counts disk usage rather than file count, it’s useful when you care about space consumption. For actual file counts, `find` is more direct.

## Handling Edge Cases

If your subdirectories contain spaces or special characters, quote variables properly:

``` bash
for dir in */; do
  count=$(find "$dir" -type f -print0 | tr -cd '\0' | wc -c)
  printf '%s: %d\n' "$dir" "$count"
done
```

This uses null-delimited output to avoid counting issues with unusual filenames.

## Performance with Large Directories

For massive directory trees, parallel processing speeds things up:

``` bash
find . -maxdepth 1 -type d -print0 | \
  xargs -0 -P 4 -I {} bash -c 'echo "{}: $(find "{}" -type f | wc -l)"'
```

The `-P 4` flag runs 4 parallel processes. Adjust based on your system’s cores and I/O capabilities.

## Sorting Output

To see which directories contain the most files:

``` bash
find . -maxdepth 2 -type f -printf '%h\n' | \
  sed 's|^\./||' | sort | uniq -c | sort -rn
```

This provides a ranked list, helpful for identifying storage hotspots.

## One-Liner with `tree`

If you have `tree` installed:

``` bash
tree -L 1 -d -h --du
```

This shows a visual tree with file counts and disk usage in one command, though it’s less suitable for scripting.

The key is choosing the right tool for your context: simple loops work for ad-hoc checks, `find` patterns scale better for automation, and parallel approaches handle massive trees efficiently.

## 2026 Best Practices and Advanced Techniques

For Count Files in Each Linux Subdirectory, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
