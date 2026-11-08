---
title: "Configuring a Static IP Address on Fedora, RHEL, and CentOS"
date: 2016-01-30 03:14:33 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-set-the-static-ip-address-using-cli-in-fedoracentos-linux/
---

NetworkManager is the default network management tool on modern Fedora, RHEL, and CentOS systems. You can configure static IPs either through the CLI or by editing configuration files directly. This guide covers both approaches for Fedora 41+ and RHEL 9+.

## Identify your network interface

Start by listing all available network interfaces:

``` bash
ip link show
```

or the more verbose:

``` bash
ip addr show
```

Look for your interface name—typically `eth0`, `enp2s0`, or similar depending on your hardware and naming convention. You’ll use this name in all subsequent commands.

## Configure static IP with nmcli (recommended)

The `nmcli` command-line tool is the modern way to manage NetworkManager connections. This approach is cleaner and doesn’t require manual file editing.

Get the current connection name:

``` bash
nmcli connection show
```

Note the connection name (often something like “System eth0” or “Wired connection 1”).

Modify the connection to use a static IP. Replace `enp2s0` with your interface name and adjust the IP settings as needed:

``` bash
sudo nmcli connection modify "System enp2s0" ipv4.method manual
sudo nmcli connection modify "System enp2s0" ipv4.addresses "192.168.1.100/24"
sudo nmcli connection modify "System enp2s0" ipv4.gateway "192.168.1.1"
sudo nmcli connection modify "System enp2s0" ipv4.dns "8.8.8.8 1.1.1.1"
```

Apply the changes by bringing the connection down and back up:

``` bash
sudo nmcli connection down "System enp2s0"
sudo nmcli connection up "System enp2s0"
```

Verify the configuration took effect:

``` bash
ip addr show enp2s0
ip route show
```

## Configure static IP by editing connection files

If you prefer editing files directly, NetworkManager stores connection profiles in `/etc/NetworkManager/system-connections/`. Each connection has its own `.nmconnection` file.

List your connections:

``` bash
ls /etc/NetworkManager/system-connections/
```

Edit the appropriate file (requires root):

``` bash
sudo nano /etc/NetworkManager/system-connections/System\ enp2s0.nmconnection
```

A basic static IP configuration looks like:

``` ini
[connection]
id=System enp2s0
uuid=550e8400-e29b-41d4-a716-446655440000
type=802-3-ethernet
interface-name=enp2s0
autoconnect=true

[ipv4]
method=manual
addresses=192.168.1.100/24
gateway=192.168.1.1
dns=8.8.8.8;1.1.1.1;
dns-search=

[ipv6]
method=auto

[802-3-ethernet]
```

Save the file and reload NetworkManager:

``` bash
sudo nmcli connection reload
sudo nmcli connection up "System enp2s0"
```

## Using the old ifcfg format (legacy, not recommended)

Older NetworkManager versions used `/etc/sysconfig/network-scripts/ifcfg-*` files. This format is deprecated but may still work on some systems:

``` bash
sudo nano /etc/sysconfig/network-scripts/ifcfg-enp2s0
```

Example configuration:

    TYPE=Ethernet
    BOOTPROTO=none
    NAME=enp2s0
    DEVICE=enp2s0
    ONBOOT=yes
    IPADDR=192.168.1.100
    PREFIX=24
    GATEWAY=192.168.1.1
    DNS1=8.8.8.8
    DNS2=1.1.1.1
    NM_CONTROLLED=yes

Then restart NetworkManager:

``` bash
sudo systemctl restart NetworkManager
```

## Verify your configuration

After applying changes, confirm the static IP is active:

``` bash
ip addr show enp2s0
ip route show
cat /etc/resolv.conf
```

Check that NetworkManager recognizes the connection:

``` bash
nmcli device show enp2s0
```

## Troubleshooting

If the IP doesn’t persist after reboot, ensure the connection has `autoconnect=true` set. Check NetworkManager logs for errors:

``` bash
sudo journalctl -u NetworkManager -n 50
```

If you’re still seeing DHCP behavior, verify the connection method is set to `manual`:

``` bash
nmcli connection show "System enp2s0" | grep ipv4.method
```

On systems where NetworkManager conflicts with other tools, you can fall back to configuring the interface directly without NetworkManager by using `/etc/sysconfig/network-scripts/` and disabling NetworkManager, though this is generally not recommended on modern Fedora/RHEL systems.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Configuring a Static IP Address on Fedora, RHEL, and CentOS with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Configuring a Static IP Address on Fedora, RHEL, and CentOS. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
