---
title: "Persisting iptables Rules on CentOS 7"
date: 2018-03-24 11:53:59 +0000
modified: 2026-04-12 16:06:48 +0000
author: "Q A"
layout: post
categories: [programming-languages]
canonical: /how-to-make-iptables-ip6tables-configurations-permanent-across-reboot-on-centos-7-linux/
---

CentOS 7 uses FirewallD as the default firewall management tool. However, if you need direct control over iptables and ip6tables rules, you can disable FirewallD and use the `iptables-services` package to restore your rules at boot.

## Install and Configure iptables-services

Start by installing the iptables-services package:

``` bash
yum install iptables-services
```

Create the rule files if they don’t exist:

``` bash
touch /etc/sysconfig/iptables
touch /etc/sysconfig/ip6tables
```

## Disable FirewallD (if running)

If FirewallD is currently active, stop and disable it:

``` bash
systemctl disable firewalld.service
systemctl stop firewalld.service
```

Verify FirewallD is no longer running:

``` bash
systemctl status firewalld.service
```

## Start and Enable iptables Services

Start the iptables and ip6tables services:

``` bash
systemctl start iptables
systemctl start ip6tables
```

Enable them to start automatically on boot:

``` bash
systemctl enable iptables
systemctl enable ip6tables
```

Verify they’re active:

``` bash
systemctl status iptables
systemctl status ip6tables
```

## Configure Your Rules

Add your iptables rules using the standard `iptables` and `ip6tables` commands. For example:

``` bash
# Allow SSH traffic
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop everything else by default
iptables -P INPUT DROP
```

## Persist Rules Across Reboot

Before saving, back up your existing configuration:

``` bash
cp /etc/sysconfig/iptables /etc/sysconfig/iptables.backup.$(date +%s)
cp /etc/sysconfig/ip6tables /etc/sysconfig/ip6tables.backup.$(date +%s)
```

Save your current iptables and ip6tables rules:

``` bash
iptables-save > /etc/sysconfig/iptables
ip6tables-save > /etc/sysconfig/ip6tables
```

These rules will now be restored automatically when the `iptables` and `ip6tables` services start on boot.

## Verify Persistence

Reboot the system and verify your rules are loaded:

``` bash
reboot
```

After reboot, check that your rules are in place:

``` bash
iptables -L -n
ip6tables -L -n
```

## Important Considerations

**When to use iptables-services instead of FirewallD:** Direct iptables management is useful for specific use cases like complex rule sets, integration with custom scripts, or legacy systems. For most modern deployments, FirewallD provides a more manageable abstraction layer.

**Modifying rules:** Any changes you make with `iptables` or `ip6tables` commands won’t persist across reboots unless you run `iptables-save` and `ip6tables-save` again. Make this part of your workflow.

**Checking what’s loaded:** View your saved rules directly:

``` bash
cat /etc/sysconfig/iptables
cat /etc/sysconfig/ip6tables
```

**Restoring from backup:** If something goes wrong:

``` bash
cp /etc/sysconfig/iptables.backup.TIMESTAMP /etc/sysconfig/iptables
systemctl restart iptables
```

**IPv6 considerations:** Ensure you handle both IPv4 and IPv6 rules if you’re using IPv6 on your network. Missing ip6tables rules can lead to unexpected behavior.

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
