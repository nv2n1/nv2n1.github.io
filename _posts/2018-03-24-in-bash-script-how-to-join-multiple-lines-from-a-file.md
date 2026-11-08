---
title: "Joining Multiple Lines in Bash Scripts"
date: 2018-03-24 11:51:24 +0000
modified: 2026-04-12 16:58:28 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /in-bash-script-how-to-join-multiple-lines-from-a-file/
---

The most common need is collapsing multi-line records into single lines. Here are the practical approaches:

### Using tr to remove newlines

The simplest method removes all newlines:

``` bash
tr -d '\n' < input.txt > output.txt
```

This works well for data without embedded line breaks you want to preserve. For CSV or structured data where you need spaces between joined lines:

``` bash
tr '\n' ' ' < input.txt > output.txt
```

### Using paste to merge adjacent lines

If you need to join every N lines, `paste` is efficient:

``` bash
paste -d' ' - - - < input.txt
```

This joins every 3 lines with spaces. Adjust the number of `-` arguments for different groupings.

### Using sed for conditional joining

Join lines that match a pattern or end with a continuation character:

``` bash
sed -e ':a' -e '$!N' -e '$!ba' -e 's/\n/ /g' input.txt
```

This reads all lines into the pattern space, then replaces newlines with spaces. More readable with comments in a script:

``` bash
sed -e ':a'              # label 'a'
    -e '$!N'            # if not last line, append next line
    -e '$!ba'           # if not last line, branch to 'a'
    -e 's/\n/ /g'       # replace all newlines with space
```

### Using awk for field-based joining

For structured data, `awk` provides more control:

``` bash
awk 'BEGIN{RS=""} {gsub(/\n/, " "); print}' input.txt
```

This treats blank lines as record separators (useful for multi-line records):

``` bash
awk 'BEGIN{RS=""; OFS=" "} {$1=$1; print}' input.txt
```

The `$1=$1` trick forces field re-evaluation with the new OFS.

### Joining lines ending with backslash

For continuation lines (common in config files):

``` bash
sed -e ':a' -e '/\\$/{N; s/\\\n//; ba' -e '}' input.txt
```

### Real-world example: processing log entries

If you have multi-line log entries separated by blank lines:

``` bash
awk 'BEGIN{RS=""; OFS=" | "} {gsub(/\n/, " | "); print NR, $0}' logfile.txt
```

### Bash parameter expansion approach

For small files entirely in memory:

``` bash
mapfile -t lines < input.txt
result=$(printf '%s ' "${lines[@]}")
echo "${result% }"  # remove trailing space
```

### Performance considerations

- `tr` is fastest for simple newline removal
- `paste` excels at joining fixed numbers of lines
- `sed` works well in pipelines without intermediate files
- `awk` best for conditional logic or field manipulation
- Bash loops are slowest but most readable for complex logic

For files over 1GB, avoid loading entirely into memory. Use streaming tools (`sed`, `awk`, `tr`) or process in chunks with `split`.

### Common pitfalls

**Preserving intentional spacing**: If your file has meaningful blank lines or specific spacing, be explicit:

``` bash
awk 'NF {printf "%s ", $0} END {print ""}' input.txt
```

This joins non-empty lines while skipping blanks.

**Handling special characters**: When joining, ensure delimiters work with your data:

``` bash
paste -d'|' - - < input.txt  # Use pipe instead of space
```

**Line ending issues**: On mixed-line-ending files (CRLF and LF), preprocess first:

``` bash
dos2unix input.txt
tr -d '\n' < input.txt > output.txt
```

Use the right tool for your specific use case—simple removal calls for `tr`, structured data favors `awk`, and complex logic benefits from `sed` patterns or pure Bash when performance isn’t critical.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Joining Multiple Lines in Bash Scripts with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Joining Multiple Lines in Bash Scripts. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
