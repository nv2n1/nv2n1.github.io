---
title: "How to Check Wireless Network Speed on Linux"
date: 2018-03-24 11:47:03 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-a-wireless-network-adapters-speed-in-linux/
---

When troubleshooting wireless performance, you need to know both the negotiated link speed and actual throughput. `ethtool` won’t help here — it’s for wired interfaces. For wireless adapters, you’ll need different tools depending on what information you’re after.

## Using iwconfig for link speed

The `iwconfig` command shows the currently negotiated link rate between your adapter and access point:

``` bash
iwconfig wlp8s0
```

Output example:

    wlp8s0    IEEE 802.11bgn  ESSID:"Your AP"  
              Mode:Managed  Frequency:2.437 GHz  Access Point: 08:5B:0E:66:DF:27   
              Bit Rate=58.5 Mb/s   Tx-Power=16 dBm   
              Retry short limit:7   RTS thr:off   Fragment thr:off
              Encryption key:off
              Power Management:off
              Link Quality=65/70  Signal level=-45 dBm  
              Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
              Tx excessive retries:4  Invalid misc:1084   Missed beacon:0

The **Bit Rate** field shows the current link speed (58.5 Mb/s in this case). Keep in mind this is the negotiated rate with the access point — not necessarily the actual throughput you’ll see in practice.

## Using iw for detailed connection info

For newer systems, `iw` is the preferred replacement for `iwconfig`:

``` bash
iw dev wlp8s0 link
```

This shows:

    Connected to 08:5b:0e:66:df:27 (on wlp8s0)
        SSID: Your AP
        freq: 2437
        RX: 1234 bytes (9 packets)
        TX: 5678 bytes (12 packets)
        signal: -45 dBm
        tx bitrate: 58.5 MBit/s

The `tx bitrate` field indicates the current link speed. You can also check supported rates with:

``` bash
iw dev wlp8s0 rate
```

## Checking actual throughput

Link speed ≠ actual throughput. The speed you see is what the driver negotiated; real-world speeds are typically 50-70% of that due to protocol overhead, retransmissions, and interference.

Test actual throughput with `iperf3`:

``` bash
# On the receiving machine
iperf3 -s

# On the sending machine
iperf3 -c 192.168.1.100 -t 30
```

This gives you realistic numbers for your specific environment.

## Monitoring speed changes

Watch how link speed changes as you move around or run bandwidth-intensive tasks:

``` bash
watch -n 1 'iw dev wlp8s0 link | grep "tx bitrate"'
```

Higher interference, distance from the AP, or physical obstacles will cause the driver to negotiate lower speeds automatically.

## Checking capability vs. negotiated speed

See what speeds your adapter *supports*:

``` bash
iw list | grep -A 20 "Band 2GHz"
```

This shows available data rates. Your actual negotiated speed depends on what both your adapter and access point support, plus environmental conditions.

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
