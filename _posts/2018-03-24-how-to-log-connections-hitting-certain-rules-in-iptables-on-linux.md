---
title: "Log and Block Rate-Limited SSH Connections with iptables"
date: 2018-03-24 11:44:56 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-log-connections-hitting-certain-rules-in-iptables-on-linux/
---

Logging connections that hit rate-limit rules helps you identify brute force attempts and troubleshoot legitimate clients that are being blocked. The standard approach is to create a dedicated chain that logs packets before dropping them.

## Create a logging and drop chain

First, create a custom chain to handle logging and dropping:

``` bash
iptables -N LOGNDROP
iptables -A LOGNDROP -j LOG --log-level info --log-prefix "iptables-drop: "
iptables -A LOGNDROP -j DROP
```

The `--log-prefix` makes logs easier to grep and parse. Log level `info` (6) is appropriate for security events without flooding syslog.

## Complete SSH rate-limiting example

Here’s a practical firewall configuration that limits new SSH connections and logs those that exceed the threshold:

``` bash
for tables in iptables ip6tables; do
    # Clear existing rules
    $tables -F
    $tables -X LOGNDROP 2>/dev/null || true

    # Allow localhost
    $tables -A INPUT -i lo -j ACCEPT

    # Allow established and related connections
    $tables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

    # Create the logging/drop chain
    $tables -N LOGNDROP
    $tables -A LOGNDROP -j LOG --log-level info --log-prefix "iptables-drop: "
    $tables -A LOGNDROP -j DROP

    # SSH: allow max 6 new connections per 60 seconds per IP
    $tables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 6 --name SSH --rsource -j LOGNDROP
    $tables -A INPUT -p tcp --dport 22 -m recent --set --name SSH --rsource -j ACCEPT

    # Reject everything else
    $tables -A INPUT -j REJECT --reject-with icmp-host-unreachable
    $tables -A FORWARD -j REJECT --reject-with icmp-host-unreachable
done
```

Note: This example uses `conntrack` instead of the deprecated `state` module, which is more efficient and reliable.

## Viewing logs

Blocked connections appear in syslog with your prefix:

``` bash
tail -f /var/log/syslog | grep "iptables-drop"
```

On systemd systems:

``` bash
journalctl -f -g "iptables-drop"
```

Export logs to a separate file by adding this to `/etc/rsyslog.d/10-iptables.conf`:

    :msg,contains,"iptables-drop:" /var/log/iptables.log
    & stop

Then restart rsyslog:

``` bash
systemctl restart rsyslog
```

## Adjusting the rate limit

Increase the threshold to be less restrictive:

``` bash
# Allow 10 new SSH connections per 60 seconds
iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 10 --name SSH --rsource -j LOGNDROP
```

Increase the time window to track IPs across a longer period:

``` bash
# Allow 6 connections per 120 seconds
iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 120 --hitcount 6 --name SSH --rsource -j LOGNDROP
```

## Checking the recent list

View IPs currently being tracked by the SSH rate limiter:

``` bash
cat /proc/net/ipt_recent/SSH
```

To reset tracking for a specific IP:

``` bash
echo "-192.168.1.50" > /proc/net/ipt_recent/SSH
```

## Important considerations

- Use `nftables` for new deployments instead of iptables. It’s faster and more maintainable.
- If you’re running a service (like fail2ban), coordinate rate limiting to avoid conflicts.
- Consider IP whitelisting for trusted administrative access to avoid locking yourself out.
- Test rules in a non-production environment first, especially if managing remotely.
- On systems with many IPs hitting SSH, monitor `/proc/net/ipt_recent/SSH` size — it grows with each tracked IP and uses memory.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Log and Block Rate-Limited SSH Connections with iptables with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Log and Block Rate-Limited SSH Connections with iptables. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
