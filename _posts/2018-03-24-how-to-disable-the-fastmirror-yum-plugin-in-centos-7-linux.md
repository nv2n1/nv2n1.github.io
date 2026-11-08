---
title: "Disable FastestMirror Plugin in CentOS 7"
date: 2018-03-24 11:54:09 +0000
modified: 2026-04-12 16:03:18 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-disable-the-fastmirror-yum-plugin-in-centos-7-linux/
---

The fastestmirror plugin automatically selects the fastest package mirror for your system. While useful, you might want to disable it if you’re experiencing slow mirror detection, prefer a specific mirror, or troubleshoot package manager issues.

The plugin is provided by `yum-plugin-fastestmirror` (on older EL7 systems) or as part of DNF’s core functionality (EL8+). Unlike older versions, modern systems don’t allow direct removal of this package due to dependency chains.

### Check your system

First, identify what package manager your system uses:

``` bash
cat /etc/os-release | grep VERSION_ID
```

- **EL7/CentOS 7**: Uses yum with plugin architecture
- **EL8+/CentOS Stream 8+/Rocky/Alma**: Uses DNF with modular plugin system
- **Fedora 38+**: Uses DNF5

### Disabling on EL7 (yum)

The fastestmirror plugin reads configuration from `/etc/yum/pluginconf.d/fastestmirror.conf`. View the current settings:

``` bash
cat /etc/yum/pluginconf.d/fastestmirror.conf
```

You’ll see output similar to:

``` ini
[main]
enabled=1
verbose=0
always_print_best_host=true
socket_timeout=3
hostfilepath=timedhosts.txt
maxhostfileage=10
maxthreads=15
```

To disable the plugin, change `enabled=1` to `enabled=0`:

``` bash
sudo sed -i 's/^enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf
```

Verify the change:

``` bash
grep "^enabled" /etc/yum/pluginconf.d/fastestmirror.conf
```

### Disabling on EL8+ (DNF)

Modern DNF versions handle mirror selection differently. If you want to disable fastest mirror detection, edit `/etc/dnf/dnf.conf`:

``` bash
sudo vi /etc/dnf/dnf.conf
```

Add or modify:

``` ini
fastestmirror=0
```

Alternatively, disable it temporarily for a single command:

``` bash
sudo dnf --setopt=fastestmirror=0 update
```

### Specifying a preferred mirror

If the issue is simply that fastestmirror picks a slow mirror, you can instead specify your preferred mirror directly. Edit your repo configuration:

``` bash
sudo vi /etc/yum/repos.d/CentOS-Linux-BaseOS.repo
```

Replace the `mirrorlist` line with a direct `baseurl`:

``` ini
# Comment out mirrorlist
# mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=baseos&infra=$infra

# Specify a direct mirror
baseurl=http://mirror.example.com/centos/$releasever/BaseOS/$basearch/os/
```

Use a geographically close or known-fast mirror from the <a href="https://www.centos.org/download/mirrors/" rel="nofollow noopener" target="_blank">CentOS mirror list</a>.

### Troubleshooting slow mirror detection

If fastestmirror itself is running slowly, check the age of the cached host file:

``` bash
ls -la /var/cache/yum/timedhosts.txt
```

Remove stale cache to force re-detection:

``` bash
sudo rm -f /var/cache/yum/timedhosts.txt
sudo yum clean all
```

For DNF:

``` bash
sudo dnf clean all
sudo dnf makecache
```

### Verify the plugin is disabled

Test that yum/dnf no longer uses mirror detection:

``` bash
sudo yum check-update
```

or

``` bash
sudo dnf check-update
```

You shouldn’t see messages about pinging or selecting mirrors. Run with verbose output to confirm:

``` bash
sudo yum -v check-update 2>&1 | grep -i mirror
```

No output indicates the plugin is successfully disabled.

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
