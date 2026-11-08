---
title: "Inspecting Linux Network Configuration"
date: 2013-07-12 16:32:14 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/finding-out-linux-network-configuration-information/
---

Linux provides multiple ways to query network configuration. While the underlying concepts remain consistent, modern tools have evolved from the older net-tools utilities.

## IP Address, MAC Address, and Netmask

The modern replacement for `ifconfig` is `ip addr`:

``` bash
$ ip addr show
```

This displays all network interfaces with their IPv4 and IPv6 addresses, MAC addresses, and subnet masks:

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:26:22:a1:25:0f brd ff:ff:ff:ff:ff:ff
        inet 143.89.135.175/24 brd 143.89.135.255 scope global eth0
           valid_lft forever preferred_lft forever
        inet6 fe80::226:22ff:fea1:250f/64 scope link
           valid_lft forever preferred_lft forever

To get information about a specific interface:

``` bash
$ ip addr show eth0
$ ip link show eth0
```

The CIDR notation (e.g., `/24`) replaces the old netmask format. If you need the netmask in dotted-decimal notation, use `ipcalc`:

``` bash
$ ipcalc 143.89.135.175/24
```

For quick reference, `hostname -I` shows all IP addresses on the system.

## DNS Configuration

Modern systems using systemd typically manage DNS through `systemd-resolved`. Query the current DNS configuration with:

``` bash
$ resolvectl status
```

This shows active DNS servers, search domains, and DNSSEC status.

Legacy `/etc/resolv.conf` may still exist but is often a symlink to systemd’s managed configuration:

``` bash
$ cat /etc/resolv.conf
```

If you need to configure DNS manually (for systems not using systemd or for overrides), edit `/etc/resolv.conf`:

    nameserver 8.8.8.8
    nameserver 8.8.4.4

For persistent DNS configuration on systems with NetworkManager:

``` bash
$ nmcli dev show
```

Or edit the NetworkManager connection profile directly:

``` bash
$ sudo nmcli connection modify "Connection Name" ipv4.dns "8.8.8.8 8.8.4.4"
$ sudo nmcli connection up "Connection Name"
```

## The Hosts File

The `/etc/hosts` file provides local hostname-to-IP mapping, bypassing DNS lookups. The loopback entries should remain unchanged:

    127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
    ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
    10.0.1.8    mysite.mydomain mysite

The system consults this file before DNS queries when configured properly in Name Service Switch.

## Name Service Switch Order

The `/etc/nsswitch.conf` file controls the order of hostname resolution:

    hosts: files mdns4_minimal [NOTFOUND=return] dns

This line means: check `/etc/hosts` first, then mDNS, then DNS. Modify the order based on your needs.

## Gateway and Routing

View the routing table with:

``` bash
$ ip route show
```

Output example:

    default via 143.89.135.254 dev eth0 proto static
    143.89.135.0/24 dev eth0 proto kernel scope link src 143.89.135.175

The `default via` line shows your gateway. To view routes for a specific interface:

``` bash
$ ip route show dev eth0
```

Add a static route:

``` bash
$ sudo ip route add 192.168.1.0/24 via 10.0.0.1 dev eth0
```

For persistence across reboots, use your distribution’s network configuration tool (NetworkManager, netplan, systemd-networkd) rather than manual route commands.

## Hostname Configuration

View the current hostname:

``` bash
$ hostname
```

Display the fully qualified domain name:

``` bash
$ hostname -f
```

Change the hostname temporarily (reverts on reboot):

``` bash
$ sudo hostname newhostname
```

For permanent changes, use `hostnamectl` on systemd systems:

``` bash
$ sudo hostnamectl set-hostname newhostname
```

This updates `/etc/hostname` and applies the change immediately.

Alternatively, edit `/etc/hostname` directly and reboot, or edit both `/etc/hostname` and `/etc/hosts` to ensure consistency.

## Complete Network Diagnostics

For comprehensive network information in one command, use:

``` bash
$ ip -a
```

This shows all addresses, routes, and interface statistics.

Test DNS resolution:

``` bash
$ nslookup example.com
$ dig example.com
$ getent hosts example.com
```

These tools verify both your DNS configuration and network connectivity.
