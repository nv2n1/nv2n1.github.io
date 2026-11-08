---
title: "iptables Configuration Guide for Linux Firewalls"
date: 2018-03-24 11:44:56 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /basic-iptables-configuration-for-linux/
---

iptables remains the standard firewall configuration tool on Linux systems, though many distributions now layer it with ufw or firewalld. Understanding the basics helps you troubleshoot, migrate, or work on systems without those abstractions.

## Understanding iptables Fundamentals

iptables operates on three main chains:

- **INPUT**: rules for incoming traffic
- **FORWARD**: rules for traffic passing through the system
- **OUTPUT**: rules for outgoing traffic

Each chain has a default policy (DROP, ACCEPT, or REJECT). Once a packet matches a rule, it’s acted upon immediately—no further rules in that chain are checked.

## Basic Firewall Setup

Here’s a practical starting configuration that allows SSH and outgoing traffic while blocking unexpected inbound connections:

``` bash
for tables in iptables ip6tables ; do
    # Flush existing rules
    $tables -F
    $tables -X

    # Default policies
    $tables -P INPUT DROP
    $tables -P FORWARD DROP
    $tables -P OUTPUT ACCEPT

    # Allow established and related connections
    $tables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

    # Allow loopback traffic
    $tables -A INPUT -i lo -j ACCEPT

    # Allow ICMP (ping)
    $tables -A INPUT -p icmp -j ACCEPT

    # Allow SSH
    $tables -A INPUT -p tcp --dport 22 -j ACCEPT

    # Log dropped packets (optional, useful for debugging)
    $tables -A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables DROP: "
done
```

Key changes from a basic config:

- **`-X` flush chains**: removes custom chains leftover from previous runs
- **FORWARD DROP**: explicitly blocks packet forwarding (change to ACCEPT only if the system routes traffic)
- **`--ctstate` instead of `--state`**: the conntrack module is more reliable for connection tracking
- **Log rule**: helps identify unexpected traffic during testing

## Saving and Persisting Rules

iptables rules exist only in memory. On reboot, you lose everything. Use a persistence method appropriate for your distribution:

**Ubuntu/Debian with iptables-persistent:**

``` bash
apt install iptables-persistent
iptables-save > /etc/iptables/rules.v4
ip6tables-save > /etc/iptables/rules.v6
```

**RHEL/CentOS/Fedora:**

``` bash
systemctl enable iptables
iptables-save > /etc/sysconfig/iptables
ip6tables-save > /etc/sysconfig/ip6tables
systemctl restart iptables
```

**Generic approach (all distributions):**

Save rules to a script and execute on boot via rc.local or a systemd service.

## Common Additions

**Allow specific HTTP/HTTPS traffic:**

``` bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

**Allow traffic from a specific subnet:**

``` bash
iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 3306 -j ACCEPT
```

**Rate-limit to prevent SYN floods:**

``` bash
iptables -A INPUT -p tcp --dport 22 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP
```

**Reject instead of drop (sends ICMP response):**

``` bash
iptables -P INPUT REJECT --reject-with icmp-host-unreachable
```

## Viewing Active Rules

``` bash
iptables -L -v -n
iptables -L INPUT -v -n
```

Use `-n` to show IP addresses instead of hostnames (faster). `-v` adds packet/byte counts.

To see rules in a format you can reuse:

``` bash
iptables-save
```

## Modern Alternatives

For new deployments, consider these instead of raw iptables:

- **ufw** (Ubuntu): simpler syntax, works on top of iptables
- **firewalld** (RHEL/Fedora): zone-based, dynamic rule reloading without dropping established connections
- **nftables** (newer systems): modern replacement for iptables with better performance and syntax

However, learning iptables remains essential for debugging, legacy systems, and understanding how these tools work underneath.
