---
title: "Optimizing MTU Size for WiFi Performance on Linux"
date: 2013-07-12 16:32:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /smaller-mtu-faster-wifi-linux/
---

If your Linux machine is getting noticeably slower WiFi speeds than other devices on the same network, MTU (Maximum Transmission Unit) misconfiguration can be a culprit. While MTU tuning won’t be the answer in every case, it’s worth investigating if you’re seeing symptoms like high latency, dropped packets, or intermittent connection issues.

## Understanding MTU

MTU is the largest packet size that can be transmitted over your network interface in a single frame. The standard Ethernet MTU is 1500 bytes, but WiFi networks sometimes need smaller values depending on:

- Your wireless driver implementation
- The access point’s configuration
- The WiFi standard (802.11a/b/g/n/ac/ax)
- Interference or marginal signal conditions

When packets exceed the MTU, they must be fragmented, which adds overhead and latency. If fragmentation is happening excessively or your hardware doesn’t handle it well, you’ll see poor performance.

## Checking Current MTU

View your current MTU setting:

``` bash
ip link show
```

Look for the `mtu` value on your WiFi interface (usually `wlan0`):

    3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
        link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff

You can also check a specific interface:

``` bash
ip link show wlan0 | grep mtu
```

## Changing MTU Temporarily

To test a different MTU value:

``` bash
sudo ip link set dev wlan0 mtu 1400
```

Verify the change:

``` bash
ip link show wlan0 | grep mtu
```

Now test your connection. Use `ping` to check latency:

``` bash
ping -c 10 8.8.8.8
```

Try different values between 1200 and 1500. Some common tested values are 1400, 1350, 1300, and 1200. Run bandwidth tests with `iperf3` to see if throughput improves:

``` bash
# On server machine
iperf3 -s

# On client (your Linux box)
iperf3 -c <server_ip>
```

## Making MTU Changes Persistent

The `ip link` command only affects the current session. To persist MTU changes across reboots:

### Using NetworkManager (most modern distributions)

Edit the connection configuration:

``` bash
sudo nmcli connection edit <connection_name>
```

Add or modify the `ethernet` section:

    [ethernet]
    mtu = 1400

Save and exit (Ctrl+D). Reactivate the connection:

``` bash
sudo nmcli connection up <connection_name>
```

Or use the GUI if NetworkManager is available on your desktop.

### Using systemd-networkd

Edit `/etc/systemd/network/99-wireless.network` (create if needed):

``` ini
[Match]
Name=wlan0

[Link]
MTUBytes=1400
```

Restart the network service:

``` bash
sudo systemctl restart systemd-networkd
```

### Using ifupdown (Debian/Ubuntu with /etc/network/interfaces)

Edit `/etc/network/interfaces`:

``` bash
auto wlan0
iface wlan0 inet dhcp
    mtu 1400
```

Restart networking:

``` bash
sudo systemctl restart networking
```

### Using Netplan (Ubuntu 18.04+)

Edit `/etc/netplan/01-netcfg.yaml`:

``` yaml
network:
  version: 2
  wifis:
    wlan0:
      dhcp4: true
      mtu: 1400
```

Apply the changes:

``` bash
sudo netplan apply
```

## Why This Works (and When It Doesn’t)

MTU problems typically arise when:

- Your WiFi driver fragments packets inefficiently
- Your access point uses non-standard MTU settings
- There’s encapsulation overhead (VPN, tunneling, VLAN tagging)
- Signal quality is marginal, making small packets more reliable

However, MTU tuning alone won’t fix:

- Poor signal strength (move closer to the AP)
- Interference from other devices (change channels)
- Outdated or buggy drivers (update your kernel/firmware)
- Network congestion

## Troubleshooting

If changing MTU causes connectivity issues, revert immediately:

``` bash
sudo ip link set dev wlan0 mtu 1500
```

If you can’t connect after making persistent changes, boot into recovery mode or connect via Ethernet to undo the configuration.

Always test gradually. Start at 1400, then try 1350 or 1300 if needed. Values below 1280 may cause issues with some services.

## Checking for Fragmentation

To see if fragmentation is occurring, check interface statistics:

``` bash
ip -s link show wlan0
```

Look for `RX` and `TX` error counts. High fragmentation isn’t directly visible, but persistent connection drops or latency spikes suggest it’s happening.

MTU tuning is a low-risk troubleshooting step when experiencing WiFi slowness. It rarely solves the root problem alone, but combined with checking signal strength, updating drivers, and ensuring your access point is properly configured, it can make a real difference.
