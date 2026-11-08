---
title: "Setting Date and Time from the Linux Command Line"
date: 2018-03-24 11:54:34 +0000
modified: 2026-04-12 16:04:00 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-linux-date-and-time-in-commands/
---

Accurate system time is critical for log timestamps, security operations, certificate validation, and coordinating across distributed systems. Modern Linux distributions handle time synchronization automatically, but you’ll occasionally need to set the time manually.

## Using timedatectl

The standard tool for time management on systemd systems is `timedatectl`. Check your current time and synchronization status:

``` bash
timedatectl status
```

This shows the local time, UTC time, timezone, and whether NTP synchronization is active.

### Set Time Manually

To set both date and time:

``` bash
sudo timedatectl set-time "2026-04-07 10:55:00"
```

Set only the date:

``` bash
sudo timedatectl set-time "2026-04-07"
```

Set only the time:

``` bash
sudo timedatectl set-time "10:55:00"
```

After manual changes, you can re-enable NTP sync:

``` bash
sudo timedatectl set-ntp true
```

## Setting Timezone

List available timezones:

``` bash
timedatectl list-timezones
```

Set your timezone:

``` bash
sudo timedatectl set-timezone America/New_York
```

## Alternative: date Command

For scripts or quick checks, the `date` command still works for displaying time:

``` bash
date
date +"%Y-%m-%d %H:%M:%S"
date --utc
```

However, `date -s` for setting time is deprecated and may not persist across reboots. Use `timedatectl` instead.

## NTP and Time Synchronization

Most production systems use automatic NTP synchronization. The default systemd-timesyncd service handles this on most modern distributions:

``` bash
systemctl status systemd-timesyncd
```

For more advanced NTP requirements, `chrony` is the preferred tool:

``` bash
sudo systemctl status chrony
chronyc tracking
```

Chrony handles clock synchronization better on systems with intermittent network connectivity or when precise time is critical.

## Time in Containers and VMs

Container and VM clocks inherit the host’s system time. Setting time inside a container won’t persist and will reset when the container restarts. Always set time on the host:

``` bash
# On the host machine
sudo timedatectl set-time "2026-04-07 10:55:00"
```

For Kubernetes clusters, ensure all nodes are synchronized:

``` bash
kubectl get nodes -o wide
# Verify time sync across nodes
ssh node1 date && ssh node2 date
```

## Verifying Time Synchronization

Check if NTP is active and synchronized:

``` bash
timedatectl status | grep "System clock synchronized"
```

For Chrony users, verify peer connectivity:

``` bash
chronyc sources
chronyc makestep
```

## Isolated Networks

In air-gapped or isolated environments where external NTP is unavailable, designate one machine as the time source and configure other systems to sync from it. Use `chrony` with a local stratum server configuration for reliable internal time synchronization.

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
