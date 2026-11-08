---
title: "Remove Specific Lines from Text Files with sed"
date: 2018-03-24 11:45:21 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-delete-a-specific-line-from-a-text-file-in-command-line-on-linux/
---

The `sed` stream editor is the go-to tool for deleting lines from files in Linux. It’s fast, works on large files without loading everything into memory, and handles complex patterns easily.

## Delete a Single Line by Line Number

To delete the 4th line from a file:

``` bash
sed -i '4d' ./file
```

The `-i` flag edits the file in place. The `d` command deletes the matched pattern space. The number `4` specifies the exact line to remove.

Before:

    aaa
    bbb
    ccc
    ddd
    eee
    ffffff

After running the command:

    aaa
    bbb
    ccc
    eee
    ffffff

Without `-i`, `sed` prints the result to stdout instead of modifying the file — useful for previewing changes:

``` bash
sed '4d' ./file
```

For backups before editing, use the `-i` backup option:

``` bash
sed -i.bak '4d' ./file
```

This creates `file.bak` before making changes.

## Delete by Pattern Matching

Remove all lines matching a regular expression:

``` bash
sed -i '/pattern/d' ./file
```

For example, delete lines containing “oops”:

``` bash
sed -i '/oops/d' ./file
```

Case-insensitive matching:

``` bash
sed -i '/oops/Id' ./file
```

## Delete Line Ranges

Remove lines 7 through 9:

``` bash
sed -i '7,9d' ./file
```

Delete from line 5 to the end of the file:

``` bash
sed -i '5,$d' ./file
```

## Delete Empty Lines

Remove all blank lines:

``` bash
sed -i '/^$/d' ./file
```

Or using a character class:

``` bash
sed -i '/./!d' ./file
```

This keeps only lines containing at least one character.

To remove lines containing only whitespace (spaces, tabs):

``` bash
sed -i '/^[[:space:]]*$/d' ./file
```

## Delete the Last Line

``` bash
sed -i '$d' ./file
```

The `$` address refers to the last line.

## Multiple Deletions in One Command

Use semicolons or multiple `-e` flags to chain operations:

``` bash
sed -i -e '1d' -e '/^#/d' -e '/^$/d' ./file
```

This deletes the first line, all comment lines (starting with \#), and all empty lines.

Or more concisely:

``` bash
sed -i '1d;/^#/d;/^$/d' ./file
```

## Practical Examples

**Remove all lines except those matching a pattern** (inverse match):

``` bash
sed -i '/pattern/!d' ./file
```

**Delete lines between two patterns:**

``` bash
sed -i '/start/,/end/d' ./file
```

This removes the first occurrence of lines from “start” to “end” inclusive. Use `$` to match to end of file:

``` bash
sed -i '/start/,$d' ./file
```

**Delete a line only if it matches multiple conditions** (using regex):

``` bash
sed -i '/error.*critical/d' ./file
```

## Performance Notes

For very large files, `sed` is efficient since it processes line-by-line. If you need to delete many scattered lines or perform complex edits, consider:

- `awk` for more complex logic
- `perl` for powerful regex and in-place editing
- Standard text editors like `vim` with `:g` commands for interactive work

`sed` remains the fastest and most portable choice for simple line deletions across Unix-like systems.

## 2026 Best Practices and Advanced Techniques

For Remove Specific Lines from Text Files with sed, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
