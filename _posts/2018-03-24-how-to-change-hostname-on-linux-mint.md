---
title: "How to Change Your Hostname on Linux Mint"
date: 2018-03-24 11:41:58 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-change-hostname-on-linux-mint/
---

The hostname identifies your system on the network. On Linux Mint, you can change it through the GUI or command line depending on your preference and situation.

## Using the GUI (Easiest Method)

1.  Open **Settings** from the application menu
2.  Go to **Details** or **About**
3.  Click the hostname field (you may need to click a pencil icon or unlock the settings)
4.  Enter your new hostname
5.  Click **Rename** or press Enter
6.  Restart your system for the change to take full effect

This method updates both `/etc/hostname` and the transient hostname automatically.

## Using the Command Line

### Quick Method with `hostnamectl`

The modern approach on systemd-based systems (all current Linux Mint versions):

``` bash
sudo hostnamectl set-hostname mynewhost
```

Replace `mynewhost` with your desired hostname. This command automatically updates both the persistent hostname and the transient hostname.

Verify the change:

``` bash
hostnamectl
```

### Manual Method with `/etc/hostname`

If you prefer direct file editing:

``` bash
sudo nano /etc/hostname
```

Replace the entire contents with your new hostname (single line, no quotes):

    mynewhost

Save and exit (Ctrl+X, then Y, then Enter in nano).

You should also update `/etc/hosts` to avoid DNS resolution delays:

``` bash
sudo nano /etc/hosts
```

Find the line starting with `127.0.0.1` and replace the old hostname with the new one:

    127.0.0.1    localhost
    127.0.1.1    mynewhost

After manual edits, apply the transient hostname without rebooting:

``` bash
sudo hostname mynewhost
```

Then restart your system to ensure all services recognize the change:

``` bash
sudo reboot
```

## Hostname Naming Rules

- Use only lowercase letters, numbers, and hyphens
- Must be between 1 and 63 characters
- Cannot start or end with a hyphen
- Avoid special characters and spaces

## Verification

After changing and rebooting, verify your hostname with:

``` bash
hostname
```

Or check both persistent and transient settings:

``` bash
hostnamectl
```

Check that your system’s DNS resolves correctly:

``` bash
getent hosts $(hostname)
```

## Troubleshooting

**Changes didn’t persist after reboot?**

- Ensure you’re using `hostnamectl` or properly edited both `/etc/hostname` and `/etc/hosts`
- Check that the file was saved correctly (no extra spaces or lines)

**Network services still showing old hostname?**

- Restart the affected services: `sudo systemctl restart systemd-logind`
- Some applications cache the hostname; restart them individually
- For Docker containers or VMs, you may need to restart the daemon

**SSH connections report wrong hostname?**

- Clear your local SSH known_hosts if you changed hostname on a remote machine
- Update DNS records if using FQDN

The `hostnamectl` method is recommended for Linux Mint as it handles all necessary configuration automatically and works across systemd services consistently.

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
