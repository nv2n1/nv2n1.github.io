---
title: "How glibc Implements strstr with the Two-Way Algorithm"
date: 2018-03-24 11:46:57 +0000
modified: 2026-04-12 16:42:13 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /implementation-of-strstr-in-glibc/
---

The glibc implementation of `strstr()` is a practical case study in algorithm selection. Rather than a naive O(n\*m) search, it uses the Two-Way string matching algorithm for better performance on both short and long needles.

## The Basic Approach

The `strstr()` function in glibc (found in `string/strstr.c`) starts with a quick check: it scans forward comparing the haystack and needle character by character. If they match completely on the first pass, the search is done immediately. If the needle is longer than the available haystack, it returns `NULL` early.

``` c
while (*haystack && *needle)
  ok &= *haystack++ == *needle++;
if (*needle)
  return NULL;  /* Needle longer than haystack */
if (ok)
  return (char *) haystack_start;  /* Match at position 0 */
```

This simple check handles the common case where the needle matches at the start, avoiding unnecessary algorithm overhead.

## Optimization with strchr()

Once a match at position 0 is ruled out, glibc uses `strchr()` to find the next occurrence of the first character of the needle in the haystack. This is faster than scanning every position because `strchr()` is highly optimized (often using SIMD operations).

``` c
needle_len = needle - needle_start;
haystack = strchr(haystack_start + 1, *needle_start);
if (!haystack || needle_len == 1)
  return (char *) haystack;
```

If the needle is only one character, `strchr()` has already solved the problem. Otherwise, the search continues from the first matching character position.

## The Two-Way Algorithm

For longer needles, glibc switches to the Two-Way algorithm, which has O(n + m) time complexity and O(1) space complexity. The algorithm doesn’t require preprocessing like KMP or Boyer-Moore, making it ideal for general-purpose string searching.

The implementation splits into two variants based on needle length:

- **Short needles** (`< LONG_NEEDLE_THRESHOLD`): Use `two_way_short_needle()`
- **Long needles**: Use `two_way_long_needle()`

Both are implemented in `string/str-two-way.h` and use the same underlying Two-Way principle: decomposing the needle into two overlapping parts and finding either the left or right part in the haystack, guaranteeing either a match or safe skipping of positions.

## When to Care About This

Understanding glibc’s approach matters when:

- **Profiling shows `strstr()` is slow**: The Two-Way algorithm is good but not optimal for all patterns. Algorithms like Boyer-Moore-Horspool can be faster on specific workloads (long needles with low match probability).
- **You need predictable performance**: Two-Way has consistent O(n + m) behavior, unlike naive algorithms that degrade to O(n\*m) on worst-case patterns.
- **Porting string search to embedded systems**: glibc’s approach is memory-efficient and doesn’t require preprocessing tables.

For most Linux sysadmin and application tasks, glibc’s `strstr()` is sufficient and well-tuned. Only optimize if profiling identifies it as a bottleneck.

## 2026 Best Practices and Advanced Techniques

For How glibc Implements strstr with the Two-Way Algorithm, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
