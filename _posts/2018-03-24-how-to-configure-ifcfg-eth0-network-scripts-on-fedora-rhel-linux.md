---
title: "Configuring Network Interfaces with ifcfg Files on RHEL"
date: 2018-03-24 11:49:09 +0000
modified: 2026-04-12 16:03:29 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-ifcfg-eth0-network-scripts-on-fedora-rhel-linux/
---

The `/etc/sysconfig/network-scripts/` directory contains network configuration files on RHEL and Fedora systems. While newer systems increasingly use NetworkManager and systemd-networkd, understanding ifcfg files remains essential for legacy systems and certain enterprise environments.

## Basic Static IP Configuration

Here’s a typical `ifcfg-eth0` file for a static IP setup:

    DEVICE=eth0
    TYPE=Ethernet
    BOOTPROTO=none
    ONBOOT=yes
    IPADDR=192.168.1.151
    NETMASK=255.255.0.0
    GATEWAY=192.168.1.10
    USERCTL=no

The key parameters:

- `DEVICE`: Interface name (eth0, ens3, etc.)
- `TYPE`: Interface type (Ethernet, Bridge, etc.)
- `BOOTPROTO`: Protocol for IP assignment (`none` for static, `dhcp` for dynamic)
- `ONBOOT`: Start interface at boot (`yes` or `no`)
- `IPADDR`: Static IP address
- `NETMASK`: Network mask (or use PREFIX for CIDR notation)
- `GATEWAY`: Default gateway
- `USERCTL`: Allow non-root users to control this interface

## Modern Syntax with CIDR Notation

Prefer CIDR notation over separate NETMASK parameters:

    DEVICE=ens3
    TYPE=Ethernet
    BOOTPROTO=none
    ONBOOT=yes
    IPADDR=192.168.1.151
    PREFIX=16
    GATEWAY=192.168.1.10
    USERCTL=no

## DHCP Configuration

For dynamic IP assignment:

    DEVICE=ens3
    TYPE=Ethernet
    BOOTPROTO=dhcp
    ONBOOT=yes
    USERCTL=yes

## Multiple IPs on One Interface

Add secondary IPs with alias files (`ifcfg-eth0:1`):

    DEVICE=eth0:1
    TYPE=Ethernet
    BOOTPROTO=none
    ONBOOT=yes
    IPADDR=192.168.1.152
    PREFIX=24

Or use the modern `IPADDR0`, `PREFIX0`, `IPADDR1`, `PREFIX1` syntax in a single file:

    DEVICE=ens3
    TYPE=Ethernet
    BOOTPROTO=none
    ONBOOT=yes
    IPADDR0=192.168.1.151
    PREFIX0=24
    IPADDR1=192.168.1.152
    PREFIX1=24
    GATEWAY=192.168.1.10

## DNS Configuration

Specify DNS servers in the ifcfg file or in `/etc/resolv.conf`. In ifcfg files:

    DNS1=8.8.8.8
    DNS2=8.8.4.4

Or use `/etc/NetworkManager/conf.d/` for NetworkManager-managed systems.

## Applying Changes

After editing ifcfg files, restart networking:

``` bash
sudo systemctl restart network
```

Or for NetworkManager (modern default):

``` bash
sudo nmcli connection reload
sudo nmcli connection up ens3
```

Verify changes:

``` bash
ip addr show
ip route show
```

## Additional Useful Parameters

- `MTU`: Maximum Transmission Unit size
- `BONDING_MASTER`: Enable bonding on this interface
- `SLAVE`: Designate as bonded slave
- `BRIDGE`: Assign to a bridge interface
- `DEFROUTE`: Use as default route (`yes` or `no`)
- `IPV6INIT`: Enable IPv6 (`yes` or `no`)
- `IPV6ADDR`: IPv6 address with prefix (e.g., `2001:db8::1/64`)

## When to Use ifcfg Files

Modern RHEL 9+ and recent Fedora versions default to NetworkManager. However, ifcfg files are still:

- Required on minimal/headless systems without NetworkManager
- Used in certain enterprise deployments with strict configuration management
- Necessary for complex bonding or bridging setups in some environments

For new deployments, prefer NetworkManager’s nmcli or YAML-based netplan configurations, but understanding ifcfg files remains important for system administration across RHEL/Fedora infrastructure.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
