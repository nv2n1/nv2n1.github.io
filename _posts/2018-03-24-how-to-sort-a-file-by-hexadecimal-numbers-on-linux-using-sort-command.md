---
title: "Sorting Hexadecimal Values in Linux Text Files"
date: 2018-03-24 11:40:27 +0000
modified: 2026-04-12 16:59:25 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-sort-a-file-by-hexadecimal-numbers-on-linux-using-sort-command/
---

The `sort` command’s `-n` flag only handles decimal numbers. When you apply it to hexadecimal values, it falls back to lexicographic (alphabetical) sorting, which produces incorrect results since hex digits don’t follow numeric order alphabetically.

Given a file with hex addresses:

    400000000   __crt0
    400000039   __newr0
    400001B14   get_my_task_id
    200000020   reg1
    20400001000 status

Running `sort -n` will misorder these because “2” comes before “4” alphabetically, placing `200000020` after entries starting with “4”—the opposite of the correct numeric order.

## Solution: Convert Hex to Decimal Before Sorting

The most reliable approach converts hex values to decimal, sorts numerically, then removes the temporary decimal column:

``` bash
awk '{print strtonum("0x" $1), $0}' file.txt | sort -n | cut -d" " -f 2-
```

Breaking this down:

- `strtonum("0x" $1)` converts the first field from hex to decimal
- `sort -n` sorts by that decimal value
- `cut -d" " -f 2-` removes the temporary decimal column

Output:

    200000020   reg1
    200000028   reg2
    200000030   reg3
    200000038   reg4
    400000000   __crt0
    400000039   __newr0
    4000000DB   output_char
    40000018F   output_q

## Handling Different Column Positions

If hex values aren’t in the first column, adjust the field reference:

``` bash
# Hex in second column
awk '{print strtonum("0x" $2), $0}' file.txt | sort -n | cut -d" " -f 2-

# Hex in third column
awk '{print strtonum("0x" $3), $0}' file.txt | sort -n | cut -d" " -f 2-
```

## Alternative: Using Perl

If you prefer Perl or need different hex formats:

``` bash
perl -ane 'printf "%d %s\n", hex($F[0]), $_' file.txt | sort -n | cut -d" " -f 2-
```

The `-a` flag auto-splits fields, and `hex()` converts hex strings to decimal.

## Sorting Multiple Hex Columns

To sort by one hex column, then by another, chain the decimal conversions:

``` bash
awk '{print strtonum("0x" $1), strtonum("0x" $2), $0}' file.txt | \
  sort -n -k1,1 -k2,2 | \
  cut -d" " -f 3-
```

This sorts by the first hex value (`-k1,1`), then by the second hex value (`-k2,2`).

## Reverse Sort (Largest to Smallest)

Add the `-r` flag to `sort`:

``` bash
awk '{print strtonum("0x" $1), $0}' file.txt | sort -rn | cut -d" " -f 2-
```

## Performance Considerations

For files with 100K+ lines, `awk` is significantly faster than spawning multiple processes with Perl and paste. Test on your actual data if performance is critical:

``` bash
# Benchmark awk approach
time awk '{print strtonum("0x" $1), $0}' huge_file.txt | sort -n | cut -d" " -f 2-

# Benchmark perl approach (slower due to subprocess overhead)
time perl -ane 'printf "%d %s\n", hex($F[0]), $_' huge_file.txt | sort -n | cut -d" " -f 2-
```

## Edge Cases

**Leading zeros in hex values** — `strtonum()` and `hex()` both handle them correctly:

``` bash
awk '{print strtonum("0x" $1), $0}' file.txt
# 0x00FF converts to 255
# 0xFF also converts to 255
```

**Mixed case hex** (A-F vs a-f) — both work fine:

``` bash
# All valid
strtonum("0xABCD")   # 43981
strtonum("0xabcd")   # 43981
strtonum("0xAbCd")   # 43981
```

**Negative hex values** — if you need to sort signed hex, use `strtonum()` with explicit sign handling or convert differently depending on your bit-width interpretation.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Sorting Hexadecimal Values in Linux Text Files with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Sorting Hexadecimal Values in Linux Text Files. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
