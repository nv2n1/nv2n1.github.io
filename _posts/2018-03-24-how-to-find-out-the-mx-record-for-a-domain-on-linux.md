---
title: "Querying MX Records on Linux with dig and host"
date: 2018-03-24 11:47:56 +0000
modified: 2026-04-12 16:59:39 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-out-the-mx-record-for-a-domain-on-linux/
---

When troubleshooting email delivery or verifying mail server configuration, you need to look up the MX (Mail Exchange) records for a domain. On Linux, two tools handle this: `host` and `dig`. Both are reliable, though `dig` is generally preferred for its flexibility and cleaner output format.

## Using dig to query MX records

The `dig` command is part of the bind-utils package and offers more detailed control over DNS queries:

``` bash
dig gmail.com MX
```

This returns output like:

    ; <<>> DiG 9.18.x <<>> gmail.com MX
    ;; QUESTION SECTION:
    ;gmail.com.         IN  MX

    ;; ANSWER SECTION:
    gmail.com.      3600    IN  MX  5 gmail-smtp-in.l.google.com.
    gmail.com.      3600    IN  MX  10 alt1.gmail-smtp-in.l.google.com.
    gmail.com.      3600    IN  MX  20 alt2.gmail-smtp-in.l.google.com.
    gmail.com.      3600    IN  MX  30 alt3.gmail-smtp-in.l.google.com.
    gmail.com.      3600    IN  MX  40 alt4.gmail-smtp-in.l.google.com.

The number before each hostname is the priority (lower values are preferred). The TTL (3600 in this case) indicates how long DNS resolvers cache the record.

For cleaner output without the verbose headers, use the `+short` flag:

``` bash
dig +short gmail.com MX
```

## Using host to query MX records

The `host` command provides simpler output and is often installed by default:

``` bash
host -t MX gmail.com
```

Output:

    gmail.com mail is handled by 5 gmail-smtp-in.l.google.com.
    gmail.com mail is handled by 10 alt1.gmail-smtp-in.l.google.com.
    gmail.com mail is handled by 20 alt2.gmail-smtp-in.l.google.com.
    gmail.com mail is handled by 30 alt3.gmail-smtp-in.l.google.com.
    gmail.com mail is handled by 40 alt4.gmail-smtp-in.l.google.com.

The `-t` flag specifies the record type. Common types include MX, A, AAAA, CNAME, NS, SOA, and TXT.

## Querying a specific DNS server

Both tools allow you to query a particular nameserver. This is useful for debugging DNS propagation issues or testing authoritative nameserver responses.

With `dig`:

``` bash
dig @8.8.8.8 gmail.com MX
```

With `host`:

``` bash
host -t MX gmail.com 8.8.8.8
```

The `@` syntax in `dig` is more intuitive than appending the server address to `host`.

## Practical troubleshooting examples

To verify mail server responsiveness after querying the MX record, combine the lookup with a connection test:

``` bash
mx_host=$(dig +short gmail.com MX | head -1 | awk '{print $NF}' | sed 's/\.$//')
telnet $mx_host 25
```

This retrieves the highest-priority MX record and attempts an SMTP connection on port 25.

To check all DNS records for a domain at once:

``` bash
dig gmail.com ANY
```

Or query specific record types:

``` bash
dig gmail.com A              # IPv4 address
dig gmail.com AAAA           # IPv6 address
dig gmail.com TXT            # Text records (SPF, DKIM, DMARC)
dig gmail.com NS             # Authoritative nameservers
```

## Performance and caching considerations

DNS queries are cached by your system resolver. If you’re testing changes to MX records, flush the local DNS cache first:

``` bash
sudo systemctl restart systemd-resolved
```

Or on systems using nscd:

``` bash
sudo systemctl restart nscd
```

For recursive lookups across multiple nameserver hops, `dig` provides the `+trace` option:

``` bash
dig +trace gmail.com MX
```

This shows the delegation chain from root nameservers down to the authoritative server, useful for understanding DNS resolution paths.

## Summary

Use `dig` for flexibility and detailed DNS diagnostics. Use `host` for quick, straightforward lookups. Both tools are essential for email administration, postfix/exim configuration, and general DNS troubleshooting on Linux systems.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Querying MX Records on Linux with dig and host with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Querying MX Records on Linux with dig and host. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
