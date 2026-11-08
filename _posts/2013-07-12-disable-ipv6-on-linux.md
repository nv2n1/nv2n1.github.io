---
title: "Disabling IPv6 on Older Linux Kernels"
date: 2013-07-12 16:32:23 +0000
modified: 2026-04-12 16:08:53 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /disable-ipv6-on-linux/
---

IPv6 is enabled by default on most Linux distributions. While IPv6adoption has grown, many environments still rely primarily on IPv4, and disabling IPv6 can simplify networking configurations or resolve compatibility issues.

## Quick Method: Disable via modprobe

The most straightforward approach is to prevent the IPv6 kernel module from loading:

``` bash
echo "options ipv6 disable=1" >> /etc/modprobe.d/disable-ipv6.conf
```

This adds a configuration line telling the kernel not to load the IPv6 module at boot. After reboot, IPv6 will be disabled.

Verify the change took effect:

``` bash
cat /proc/sys/net/ipv6/conf/all/disable_ipv6
```

A value of `1` confirms IPv6 is disabled; `0` means it’s enabled.

## Disable IPv6 Without Reboot

If you need to disable IPv6 immediately without rebooting:

``` bash
sysctl -w net.ipv6.conf.all.disable_ipv6=1
sysctl -w net.ipv6.conf.default.disable_ipv6=1
```

Verify:

``` bash
ip a
```

IPv6 addresses (those starting with `fe80::` or `2001:`) should no longer appear.

To make these settings persistent across reboots, add them to `/etc/sysctl.conf` or create a file in `/etc/sysctl.d/`:

``` bash
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.d/99-disable-ipv6.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.d/99-disable-ipv6.conf
sudo sysctl -p /etc/sysctl.d/99-disable-ipv6.conf
```

## Disable IPv6 for Specific Interfaces

To disable IPv6 on a specific interface instead of system-wide:

``` bash
sysctl -w net.ipv6.conf.eth0.disable_ipv6=1
```

Replace `eth0` with your interface name. Make it persistent by adding to `/etc/sysctl.d/99-disable-ipv6.conf`:

``` bash
net.ipv6.conf.eth0.disable_ipv6 = 1
```

## Using netplan (Ubuntu/Debian with netplan)

On systems using netplan for network configuration, you can disable IPv6 in the YAML config:

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: false
      ipv6: false
```

Apply the configuration:

``` bash
sudo netplan apply
```

## Using NetworkManager

With NetworkManager, disable IPv6 via the `nmcli` command:

``` bash
nmcli con mod "Connection Name" ipv6.method ignore
nmcli con up "Connection Name"
```

Or edit the connection file directly at `/etc/NetworkManager/conf.d/` if needed.

## Verify IPv6 is Disabled

Check both kernel parameters and active connections:

``` bash
cat /proc/sys/net/ipv6/conf/all/disable_ipv6
ip -6 addr show
ss -tunap | grep '::'
```

All IPv6 listening sockets and addresses should be absent.

## Re-enabling IPv6

To reverse the changes:

``` bash
sysctl -w net.ipv6.conf.all.disable_ipv6=0
sysctl -w net.ipv6.conf.default.disable_ipv6=0
```

Or remove the configuration files and reboot:

``` bash
sudo rm /etc/modprobe.d/disable-ipv6.conf /etc/sysctl.d/99-disable-ipv6.conf
sudo reboot
```

## Important Considerations

Some services and applications expect IPv6 to be available, even if not actively used. Disabling IPv6 globally can cause:

- Increased DNS lookup times if the system tries IPv6 before falling back to IPv4
- Issues with services binding to `::1` (IPv6 localhost)
- Potential problems with containerized applications or systemd services

Test thoroughly in non-production environments before applying globally.

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
