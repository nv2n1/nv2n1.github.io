---
title: "Network Interface Bonding in Linux: Configuration Guide"
date: 2018-03-24 11:46:25 +0000
modified: 2026-04-12 16:34:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-interface-bonding-in-linux/
---

Network bonding aggregates multiple network interfaces into a single logical interface, providing redundancy, load balancing, or increased throughput. The method you use depends on your distribution and whether you’re managing a desktop, workstation, or server environment.

## NetworkManager (Desktop and Some Servers)

NetworkManager is the easiest approach for most distributions. Create a bond with a single command:

``` bash
sudo nmcli connection add type bond ifname bond0 mode active-backup con-name bond0
```

Add physical interfaces to the bond:

``` bash
sudo nmcli connection add type ethernet ifname eth0 master bond0 slave-type bond con-name bond0-eth0
sudo nmcli connection add type ethernet ifname eth1 master bond0 slave-type bond con-name bond0-eth1
```

Activate the bond:

``` bash
sudo nmcli connection up bond0
```

Verify the bond status:

``` bash
cat /proc/net/bonding/bond0
```

## Netplan (Ubuntu/Debian)

Edit `/etc/netplan/01-netcfg.yaml` (or similar):

``` yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
    eth1:
      dhcp4: no
  bonds:
    bond0:
      dhcp4: yes
      interfaces: [eth0, eth1]
      parameters:
        mode: active-backup
        mii-monitor-interval: 100
```

Apply the configuration:

``` bash
sudo netplan apply
```

## Network Scripts (RHEL/CentOS/Rocky)

Create `/etc/sysconfig/network-scripts/ifcfg-bond0`:

    TYPE=Bond
    BONDING_MASTER=yes
    NAME=bond0
    DEVICE=bond0
    BONDING_OPTS="mode=active-backup miimon=100"
    BOOTPROTO=dhcp
    ONBOOT=yes

Create `/etc/sysconfig/network-scripts/ifcfg-eth0`:

    TYPE=Ethernet
    BONDING_MASTER=no
    SLAVE=yes
    MASTER=bond0
    NAME=eth0
    DEVICE=eth0
    ONBOOT=yes

Repeat for `eth1`. Restart networking:

``` bash
sudo systemctl restart NetworkManager
# or
sudo systemctl restart network
```

## Bonding Modes Explained

- **mode=0 (balance-rr)**: Round-robin across all active interfaces. Requires switch-level port grouping.
- **mode=1 (active-backup)**: One interface is active; others stand by. No switch configuration needed. Best for redundancy.
- **mode=4 (802.3ad)**: Dynamic Link Aggregation Protocol (LACP). Requires switch support and properly configured trunk ports. Provides load balancing.
- **mode=6 (balance-alb)**: Adaptive load balancing. Works with any switch but not ideal for high-throughput scenarios.

## Monitoring and Troubleshooting

Check bond status:

``` bash
ip link show
cat /proc/net/bonding/bond0
ethtool -i bond0
```

Check if a slave interface is active:

``` bash
cat /sys/class/net/bond0/lower_eth0/flags
```

Monitor link changes:

``` bash
sudo ip monitor link
```

If an interface fails to bond, verify it’s not managed by conflicting services:

``` bash
nmcli device status
ip link set eth0 down  # manually bring down if needed
```

## Performance Considerations

For standard workloads, active-backup mode is reliable and requires no switch configuration. For production clusters needing maximum throughput, 802.3ad with proper switch LACP configuration delivers better performance.

If you’re building low-latency systems (HPC, financial services), consider RDMA over Converged Ethernet (RoCE) alongside bonding for specialized applications, though traditional bonding handles most use cases effectively.

## Persistent Configuration

Always verify your bond persists after reboot:

``` bash
sudo reboot
ip link show
cat /proc/net/bonding/bond0
```

If using NetworkManager and planning to transition to netplan or network scripts, export your configuration first to avoid conflicts:

``` bash
nmcli connection export bond0 > bond0-backup.conf
```

## 2026 Best Practices and Advanced Techniques

For Network Interface Bonding in Linux: Configuration Guide, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
