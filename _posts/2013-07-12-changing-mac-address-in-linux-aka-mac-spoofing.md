---
title: "Spoofing MAC Addresses in Linux"
date: 2013-07-12 16:32:10 +0000
modified: 2026-04-12 05:27:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /changing-mac-address-in-linux-aka-mac-spoofing/
---

MAC stands for Media Access Control — a six-byte identifier (usually written as twelve hexadecimal digits) that uniquely identifies a network interface on a LAN. The Address Resolution Protocol (ARP) maps IP addresses to MAC addresses at layer 2.

You might need to change your MAC address to:

- Bypass network access controls tied to MAC filtering
- Avoid device tracking across networks
- Test network behavior with multiple “devices”
- Access networks with device-based licensing restrictions

## Using ip Command (Modern Approach)

The `ifconfig` command is deprecated. Use `ip` instead, which works on all modern distributions:

``` bash
# Bring down the interface
ip link set dev eth0 down

# Change the MAC address
ip link set dev eth0 address 00:00:00:00:00:01

# Bring it back up
ip link set dev eth0 up

# Verify the change
ip link show eth0
```

You should see output like:

    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
        link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff

## Using systemd-networkd or NetworkManager

For permanent MAC spoofing, configure it in your network management layer rather than relying on runtime commands.

**With systemd-networkd:**

Edit `/etc/systemd/network/99-eth0.link`:

``` ini
[Match]
MACAddress=<original_mac_address>

[Link]
MACAddress=00:00:00:00:00:01
```

Restart the service:

``` bash
systemctl restart systemd-networkd
```

**With NetworkManager:**

``` bash
nmcli connection modify eth0 802-3-ethernet.cloned-mac-address 00:00:00:00:00:01
nmcli connection up eth0
```

## Automated MAC Spoofing with macchanger

For frequent spoofing or random addresses, use `macchanger`:

``` bash
# Install
apt install macchanger  # Debian/Ubuntu
dnf install macchanger  # Fedora
pacman -S macchanger    # Arch

# View current MAC
macchanger -s eth0

# Change to specific address
macchanger -m 00:00:00:00:00:01 eth0

# Change to random address
macchanger -r eth0

# Keep vendor prefix, randomize device portion
macchanger -e eth0
```

## Important Caveats

**Persistence:** Runtime changes with `ip` are lost on reboot. Use systemd-networkd, NetworkManager, or udev rules for persistence.

**Virtualization:** In VMs, MAC changes may be restricted by the hypervisor. Check your VM settings.

**DHCP complications:** Some DHCP servers cache leases by MAC address. After spoofing, you may need to release and renew:

``` bash
dhclient -r eth0
dhclient eth0
```

**Interface naming:** Modern systemd uses predictable interface naming (eno1, enp3s0, etc.). Adjust commands accordingly. Use `ip link` to list all interfaces.

**Wireless interfaces:** MAC spoofing on WiFi requires the interface to be down and may be blocked by some drivers. Check `iw` capabilities:

``` bash
iw dev wlan0 link
```

**SELinux/AppArmor:** Confined systems may restrict `macchanger` or `ip link set address`. Check policy rules if commands fail.

## Checking Valid MAC Addresses

Real MAC addresses follow patterns — the first octet’s least significant bit indicates unicast (even) vs. multicast (odd), and the second-least significant bit indicates universally administered (0) vs. locally administered (1).

For testing, use locally administered unicast addresses (second hex digit is even and has bit 1 set):

- Valid: `02:xx:xx:xx:xx:xx`, `06:xx:xx:xx:xx:xx`, `0a:xx:xx:xx:xx:xx`
- Invalid for spoofing: `00:xx:xx:xx:xx:xx` (conflicts with real device MACs)

## Detection and Risks

Network administrators can detect spoofing through:

- DHCP server logs (hostname/vendor changes without MAC rotation)
- ARP inspection tools
- Passive observation of behavior patterns
- Active probing (DHCPv6 solicitations, mDNS queries)

Spoofing for legitimate network access is acceptable; using it to evade security controls or impersonate others is illegal in most jurisdictions.
