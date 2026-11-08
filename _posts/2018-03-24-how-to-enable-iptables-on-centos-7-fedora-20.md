---
title: "Migrating from firewalld to iptables on CentOS 7 and Fedora"
date: 2018-03-24 08:21:31 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-enable-iptables-on-centos-7-fedora-20/
---

If you need direct control over your firewall rules, you can disable firewalld and use iptables instead. This guide covers the setup process and best practices for maintaining persistent rules.

## Stop and disable firewalld

If firewalld is currently running, stop it and prevent it from starting on boot:

``` bash
sudo systemctl stop firewalld
sudo systemctl disable firewalld
```

Both firewalld and iptables-services manage the kernel’s netfilter subsystem, so running them simultaneously causes conflicts. You must choose one or the other.

## Install iptables-services

Install the package that provides systemd unit files and infrastructure for managing iptables:

``` bash
sudo yum install iptables-services
```

This installs init scripts for both `iptables` and `ip6tables` services.

## Initialize rule files

Create empty rule files before starting the service:

``` bash
sudo touch /etc/sysconfig/iptables
sudo touch /etc/sysconfig/ip6tables
```

These files persist your firewall rules across reboots. Without them, the service may fail to start or rules won’t be saved properly.

## Start and enable the services

Start both IPv4 and IPv6 firewall services:

``` bash
sudo systemctl start iptables
sudo systemctl start ip6tables
```

Enable them to start automatically on boot:

``` bash
sudo systemctl enable iptables
sudo systemctl enable ip6tables
```

Verify both services are running:

``` bash
sudo systemctl status iptables
sudo systemctl status ip6tables
```

## View current rules

List all rules with numeric output and verbose details:

``` bash
sudo iptables -L -n -v
sudo ip6tables -L -n -v
```

Add `-t` to view specific tables (e.g., `sudo iptables -L -n -v -t nat` for NAT rules).

## Add firewall rules

Use standard iptables commands to add rules. For example, allow SSH and established connections:

``` bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -j DROP
```

Do the same for IPv6:

``` bash
sudo ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo ip6tables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo ip6tables -A INPUT -j DROP
```

## Save rules persistently

After adding rules, save them to the configuration files:

``` bash
sudo iptables-save > /etc/sysconfig/iptables
sudo ip6tables-save > /etc/sysconfig/ip6tables
```

These rules will automatically load when the service starts.

## Common rule examples

**Allow specific ports:**

``` bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

**Allow traffic from a specific IP:**

``` bash
sudo iptables -A INPUT -s 192.168.1.100 -j ACCEPT
```

**Allow loopback traffic:**

``` bash
sudo iptables -A INPUT -i lo -j ACCEPT
```

**Delete a rule:**

``` bash
sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT
```

**Flush all rules:**

``` bash
sudo iptables -F
sudo iptables -X
```

Remember to save again after any changes.

## Troubleshooting

If the iptables service fails to start, check systemd logs:

``` bash
sudo journalctl -u iptables -n 20
```

Common issues include:

- **Invalid rule syntax** in `/etc/sysconfig/iptables` — verify with `sudo iptables-restore < /etc/sysconfig/iptables`
- **Permission problems** — ensure root can read the rule files: `sudo chmod 600 /etc/sysconfig/iptables*`
- **Service conflicts** — confirm firewalld is disabled: `sudo systemctl is-active firewalld` should return `inactive`

## Important notes for modern systems

On CentOS 8+ and Fedora 30+, nftables replaced iptables as the default firewall tool. However, iptables still works through legacy wrapper binaries. If you’re on these systems and want native nftables instead, refer to nftables documentation. For older workloads requiring iptables, the compatibility layer continues to function.
