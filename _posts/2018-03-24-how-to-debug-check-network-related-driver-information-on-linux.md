---
title: "Debugging Linux Network Drivers: Essential Tools and Techniques"
date: 2018-03-24 08:21:45 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-debug-check-network-related-driver-information-on-linux/
---

When network interfaces fail or behave unexpectedly, you need to inspect driver details, hardware state, and kernel messages. Here’s the practical toolkit for diagnosing network hardware and driver issues.

## Kernel Messages and Logs

Start by checking kernel logs where driver initialization and errors are recorded:

``` bash
dmesg | grep -i network
dmesg | grep -i driver
dmesg | tail -50
```

For persistent logs across reboots, use the systemd journal:

``` bash
journalctl -k | grep -i network
journalctl -k | grep -i eth
journalctl --since "1 hour ago" | grep -i driver
journalctl -u NetworkManager -n 50
```

On systems still using rsyslog, check traditional log files:

``` bash
grep -i network /var/log/messages
grep -i driver /var/log/syslog
```

## Hardware Detection and Driver Information

### PCI and USB Devices

`lspci` lists PCI devices including built-in network adapters:

``` bash
lspci | grep -i network
lspci -v | grep -i network  # verbose output
lspci -k | grep -A 2 -i network  # includes loaded kernel modules
```

`lsusb` lists USB devices including USB network adapters:

``` bash
lsusb
lsusb -v  # verbose output with all details
lsusb -d 0bda:8153  # search by vendor:device ID
lsusb -t  # tree view with hubs
```

`lshw` provides comprehensive hardware details with driver information:

``` bash
lshw -c network
lshw -c network -businfo
```

### Ethernet Driver Details

`ethtool` queries and modifies Ethernet device settings:

``` bash
ethtool eth0  # basic interface information
ethtool -i eth0  # driver and firmware information
ethtool -S eth0  # driver statistics
ethtool -k eth0  # show offloads (TSO, GSO, etc.)
ethtool -g eth0  # ring buffer settings
ethtool -c eth0  # coalescing settings
```

Example output from `ethtool -i eth0`:

    driver: e1000e
    version: 3.2.6-k
    firmware-version: 0.13-4
    bus-info: 0000:00:1f.6
    supports-statistics: yes
    supports-test: yes
    supports-eeprom-access: yes
    supports-register-dump: yes
    supports-priv-flags: no

## Wireless Device Management

For wireless interfaces, check hardware block state:

``` bash
rfkill list
rfkill unblock all  # unblock WiFi if hardware-blocked
rfkill unblock wifi
```

Modern systems use `iw` for wireless configuration:

``` bash
iw dev
iw dev wlan0 link  # connection status
iw list  # supported capabilities
iw wlan0 station dump  # connected station info
```

The legacy `iwconfig` still works on some systems but is deprecated:

``` bash
iwconfig
iwconfig wlan0
```

## Network Interface Configuration

View active interfaces and their state:

``` bash
ip link show
ip link show eth0
ip -s link show eth0  # statistics (RX/TX packets, errors, dropped)
```

Check IP configuration:

``` bash
ip addr show
ip route show
ip -6 route show  # IPv6 routes
```

For DNS and DHCP information:

``` bash
resolvectl status
resolvectl status eth0
nmcli device show eth0  # if using NetworkManager
```

## Finding Driver Module Information

Determine which kernel module drives a device:

``` bash
ethtool -i eth0 | grep driver
lsmod | grep driver_name
modinfo driver_name  # detailed module information
```

Check module parameters and current values:

``` bash
cat /sys/module/driver_name/parameters/*
cat /sys/module/e1000e/parameters/debug
```

To see what firmware files a driver is trying to load:

``` bash
journalctl -k | grep firmware
dmesg | grep -i "firmware\|fw_path"
```

## Detailed Hardware State

For USB network devices, check power management and descriptor information:

``` bash
lsusb -d 0bda:8153 -v
cat /sys/bus/usb/devices/*/power/control  # check autosuspend settings
```

To disable autosuspend on a USB network device (permanent):

``` bash
echo "0" | sudo tee /sys/bus/usb/devices/1-1/power/autosuspend_delay_ms
```

Check USB device tree:

``` bash
lsusb -t
cat /sys/bus/usb/devices/1-1/speed  # USB 2.0, 3.0, etc.
```

## Practical Debugging Workflow

When a network device isn’t recognized or behaves incorrectly:

1.  **Check kernel logs for hardware detection**

``` bash
dmesg | grep -E "eth|wlan|usb|Ethernet" | tail -30
journalctl -k --since "30 minutes ago"
```

2.  **Verify the device appears in hardware lists**

``` bash
lspci | grep -i network
lsusb | grep -i network
```

3.  **Confirm the driver module is loaded**

``` bash
lsmod | grep driver_name
ethtool -i eth0 | grep driver
```

4.  **If the driver isn’t loaded, load it manually**

``` bash
sudo modprobe driver_name
sudo modprobe -v driver_name  # verbose, shows what it's doing
```

5.  **Check for hardware blocks (wireless devices)**

``` bash
rfkill list
```

6.  **Inspect detailed device status**

``` bash
ethtool -i eth0
ip -s link show eth0
journalctl -k --grep="eth0" --all
```

7.  **For USB devices, check power state and firmware**

``` bash
lsusb -d vendor:product -v | grep -A 5 "MaxPower\|bMaxPower"
dmesg | grep -E "firmware|fw" | tail -10
```

## Common Issues and Solutions

**Driver not loading automatically:** Check if the module exists and isn’t blacklisted:

``` bash
find /lib/modules/$(uname -r) -name "*driver_name*"
grep -r "blacklist" /etc/modprobe.d/
```

**Driver loads but interface doesn’t appear:** Check kernel messages and driver initialization:

``` bash
sudo modprobe -r driver_name
sudo modprobe driver_name
dmesg | tail -20
```

**Interface shows as DOWN:** Check hardware block state and driver state:

``` bash
ip link show eth0
ethtool eth0 | grep -i "link detected"
rfkill list
```

**Poor network performance:** Check for driver issues, offloads, and ring buffers:

``` bash
ethtool -k eth0  # check if offloads are enabled
ethtool -g eth0  # verify ring buffer sizes
ethtool -S eth0 | grep -i drop  # check for dropped packets
```

Most modern distributions manage network interfaces through systemd-networkd or NetworkManager. Always verify their status alongside driver information for complete visibility.
