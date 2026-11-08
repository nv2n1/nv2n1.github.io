---
title: "MobileNet Configuration on Linux: HKUST Setup Guide"
date: 2013-07-12 16:31:39 +0000
modified: 2026-04-12 16:30:59 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /configure-smobilenet-of-hkust-on-linux/
---

To connect to HKUST’s sMobileNet wireless network via NetworkManager, you’ll need to configure WPA2 Enterprise authentication with PEAP. This guide covers the required settings.

## Network Settings

Configure the following parameters in NetworkManager:

**Basic Settings:**

- SSID: `sMobileNet`
- Wireless security: WPA & WPA2 Enterprise
- Authentication method: Protected EAP (PEAP)

**Authentication Details:**

- Anonymous identity: (leave empty)
- PEAP version: Automatic
- Inner authentication: MSCHAPv2
- Username: `username@ust.hk`
- Password: your HKUST password

**Certificate:**

- CA certificate: (None) — ignore any certificate warnings

## Configuring via GUI

1.  Open NetworkManager settings (system settings or `nmtui` in terminal)
2.  Select “Add” or “+” to create a new connection
3.  Choose “Wi-Fi” as the connection type
4.  Enter SSID: `sMobileNet`
5.  Under Security, select “WPA & WPA2 Enterprise”
6.  Configure the EAP method:
    - EAP method: PEAP
    - Anonymous identity: (leave blank)
    - CA certificate: (None)
    - PEAP version: Automatic
    - Inner authentication: MSCHAPv2
7.  Enter your HKUST credentials
8.  Save and connect

## Configuring via nmcli

You can also configure this from the command line using `nmcli`:

``` bash
nmcli connection add type wifi con-name sMobileNet ifname wlan0 ssid sMobileNet
nmcli connection modify sMobileNet wifi-sec.key-mgmt wpa-eap
nmcli connection modify sMobileNet 802-1x.eap peap
nmcli connection modify sMobileNet 802-1x.phase2-auth mschapv2
nmcli connection modify sMobileNet 802-1x.identity "username@ust.hk"
nmcli connection modify sMobileNet 802-1x.password "your-password"
nmcli connection up sMobileNet
```

Replace `username@ust.hk` with your actual HKUST username and `your-password` with your password.

## Manual Configuration via nmtui

If you prefer the terminal UI:

``` bash
nmtui
```

Navigate to “Edit a connection” → “Add” → “Wi-Fi”, then enter the settings listed above.

## Troubleshooting

**Connection fails with authentication error:**

- Verify your HKUST username format is correct (`username@ust.hk`, not just `username`)
- Confirm your password is current
- Check that PEAP is set to “Automatic” and inner auth is “MSCHAPv2”

**CA certificate warning:**
This is expected behavior with sMobileNet. The warning is safe to ignore — the connection will still function properly.

**No PEAP option available:**
Ensure you have the required packages installed:

``` bash
# Debian/Ubuntu
sudo apt install wpasupplicant network-manager

# RHEL/Fedora/CentOS
sudo dnf install wpa_supplicant NetworkManager

# Arch
sudo pacman -S wpa_supplicant networkmanager
```

**Connection drops or reconnects frequently:**
Check your system’s power management settings. Disable wireless power saving if needed:

``` bash
sudo iw wlan0 set power_save off
```

To make this persistent across reboots, add to `/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf`:

    [connection]
    wifi.powersave = 2

## Verification

After connecting, verify your connection:

``` bash
nmcli connection show sMobileNet
nmcli device wifi show
```

Check IP assignment:

``` bash
ip addr show wlan0
```

This configuration works on all major Linux distributions that use NetworkManager, including Fedora, RHEL, CentOS, Debian, Ubuntu, and Arch Linux.

## 2026 Best Practices and Advanced Techniques

For MobileNet Configuration on Linux: HKUST Setup Guide, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
