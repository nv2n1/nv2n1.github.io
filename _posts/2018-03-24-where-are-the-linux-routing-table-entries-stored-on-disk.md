---
title: "Where Linux Stores Routing Table Entries on Disk"
date: 2018-03-24 08:16:39 +0000
layout: post
canonical: https://www.systutorials.com/where-are-the-linux-routing-table-entries-stored-on-disk/
---

Linux routing tables exist in kernel memory during runtime. To persist routes across reboots, you need to store them on disk and have them reloaded during system startup. The mechanism varies depending on your network management setup.

## systemd-networkd and netplan (modern systems)

On contemporary distributions using `systemd-networkd` or `netplan`, define routes in YAML configuration files.

With **netplan**, create or edit `/etc/netplan/01-netcfg.yaml`:

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      routes:
        - to: 10.1.1.0/24
          via: 192.168.1.1
          metric: 100
        - to: 10.2.0.0/16
          via: 192.168.1.254
```

Apply with:

``` bash
sudo netplan apply
```

With **systemd-networkd**, place `.network` files in `/etc/systemd/network/`:

``` ini
[Match]
Name=eth0

[Network]
DHCP=yes

[Route]
Destination=10.1.1.0/24
Gateway=192.168.1.1
Metric=100

[Route]
Destination=10.2.0.0/16
Gateway=192.168.1.254
```

Reload with:

``` bash
sudo systemctl restart systemd-networkd
```

## NetworkManager

NetworkManager stores configuration in `/etc/NetworkManager/system-connections/` as `.nmconnection` files. Edit these directly or use the GUI:

``` bash
nmtui
```

Or configure routes via nmcli:

``` bash
nmcli connection modify "connection-name" +ipv4.routes "10.1.1.0/24 192.168.1.1"
nmcli connection up "connection-name"
```

## Legacy: /etc/sysconfig/static-routes (RHEL/CentOS 7 and earlier)

On older RHEL/CentOS systems using traditional init scripts, static routes go in `/etc/sysconfig/static-routes`:

    any host 10.1.1.8 gw 8.9.10.11
    any net 10.2.0.0 netmask 255.255.255.0 gw 192.168.1.1

The format is `any [net|host] destination [netmask mask] gw gateway`. The network script parses lines starting with `any` and passes them to `route add`.

## Per-interface routes (legacy)

On systems with ifcfg scripts, routes can also be defined in `/etc/sysconfig/network-scripts/route-eth0`:

    10.1.1.0/24 via 192.168.1.1
    10.2.0.0/16 via 192.168.1.254 metric 100

## Verifying persistent routes

After configuration, verify routes are loaded:

``` bash
ip route show
```

Check route configuration is correct:

``` bash
ip route show table all
```

To view all route tables:

``` bash
cat /etc/iproute2/rt_tables
```

## Adding runtime-only routes

For temporary routes that don’t survive reboot, use `ip route`:

``` bash
sudo ip route add 10.1.1.0/24 via 192.168.1.1
sudo ip route del 10.1.1.0/24
```

These disappear after reboot unless persisted through the appropriate configuration method above.

## Key differences from iptables

Unlike firewall rules (iptables/nftables), routing table entries aren’t typically stored in a single dedicated dump file like `/etc/sysconfig/iptables`. Instead, they’re defined as part of network interface configuration, allowing routes to be associated with specific connections and applied conditionally based on network state.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Where Linux Stores Routing Table Entries on Disk with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Where Linux Stores Routing Table Entries on Disk. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
