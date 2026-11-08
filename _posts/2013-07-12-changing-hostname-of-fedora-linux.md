---
title: "Changing Your Hostname on Fedora Linux"
date: 2013-07-12 16:32:28 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/changing-hostname-of-fedora-linux/
---

Fedora has evolved its hostname management over the years. Modern versions use systemd and the `/etc/hostname` file, while older releases relied on `/etc/sysconfig/network`. Here’s how to handle both scenarios.

## Using hostnamectl (Recommended)

The most straightforward method on current Fedora is using `hostnamectl`, which handles hostname changes through systemd:

``` bash
sudo hostnamectl set-hostname newname.example.com
```

For a hostname without a domain component:

``` bash
sudo hostnamectl set-hostname myhostname
```

Verify the change immediately:

``` bash
hostnamectl
```

This will display both the static hostname and the current hostname. The change takes effect immediately without requiring a restart.

## Direct File Editing (Fedora 41+)

If you prefer editing directly, the `/etc/hostname` file contains a single line with your hostname:

``` bash
sudo nano /etc/hostname
```

Replace the existing content with your desired hostname:

    myhostname.example.com

Save and exit. To apply the change:

``` bash
sudo systemctl restart systemd-hostnamed
```

Verify with:

``` bash
hostname
hostnamectl
```

## Persistent DNS Configuration

Changing the hostname alone doesn’t update your system’s DNS configuration. For a fully functional setup, also update `/etc/hosts`:

``` bash
sudo nano /etc/hosts
```

Modify the entry for localhost and add your new hostname:

    127.0.0.1   localhost
    ::1         localhost
    127.0.0.1   myhostname.example.com myhostname
    ::1         myhostname.example.com myhostname

This ensures local resolution works correctly and prevents potential issues with applications that reference the hostname.

## For Older Fedora Releases (Before Fedora 41)

Older releases used the `/etc/sysconfig/network` file:

``` bash
sudo nano /etc/sysconfig/network
```

Locate or create the `HOSTNAME` line:

    HOSTNAME=myhostname.example.com

Restart the network service:

``` bash
sudo systemctl restart network
```

## Verifying Your Changes

Always confirm the hostname has been set correctly:

``` bash
hostname
hostname -f
hostnamectl status
```

- `hostname` shows the short hostname
- `hostname -f` shows the fully qualified domain name
- `hostnamectl status` displays detailed information from systemd

## Checking Hostname Propagation

If you’ve set a fully qualified domain name, verify DNS resolution:

``` bash
nslookup myhostname.example.com
dig myhostname.example.com
```

This confirms the hostname resolves properly through your DNS infrastructure, which is essential if other systems need to reach this machine by name.

## Temporary Hostname Changes

To change the hostname only for the current session (reverts on reboot):

``` bash
sudo hostname temporaryname
```

This is useful for testing before making permanent changes.

## Common Pitfalls

Avoid spaces and special characters in hostnames — use only lowercase letters, numbers, and hyphens. Keep hostnames under 253 characters and individual labels under 63 characters per DNS standards. If you’re managing multiple systems, ensure hostnames are unique within your network to prevent connectivity and identification issues.

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
