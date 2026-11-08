---
title: "Tuning Linux UDP Buffer Sizes to Prevent Packet Loss"
date: 2018-03-24 11:41:17 +0000
layout: post
canonical: https://www.systutorials.com/how-to-enlarge-linux-udp-buffer-size/
---

UDP packet loss on Linux commonly stems from undersized kernel buffers. When packets arrive faster than the application can process them, the kernel drops excess datagrams silently. Unlike TCP, UDP offers no retransmission, so these losses are permanent. Proper buffer tuning is essential for DNS servers, NTP, monitoring systems, video streaming, and any high-throughput UDP service.

## Why UDP Packets Get Lost

The kernel maintains separate receive and transmit buffers for each socket. When a UDP packet arrives and the receive buffer is full, the kernel discards it. This happens even when the application is running normally—the issue is purely a buffering mismatch between network arrival rate and application consumption rate.

## Checking Current Buffer Configuration

View your system’s current socket buffer limits:

``` bash
sysctl net.core.rmem_max net.core.rmem_default
sysctl net.core.wmem_max net.core.wmem_default
```

Default values on most modern distributions are modest (typically 128 KB to 256 KB). Check what a specific process is using with `/proc`:

``` bash
cat /proc/net/udp
```

The `RxQueue` column shows how full the receive buffer currently is. If you regularly see non-zero values, packets are being dropped.

To monitor in real-time with `ss`:

``` bash
ss -tnmu | head -20
```

## Increasing Buffer Sizes Temporarily

For immediate testing (persists until reboot):

``` bash
sudo sysctl -w net.core.rmem_max=26214400
sudo sysctl -w net.core.rmem_default=26214400
sudo sysctl -w net.core.wmem_max=26214400
sudo sysctl -w net.core.wmem_default=26214400
```

This sets both receive and transmit buffers to 25 MB. Changes take effect immediately.

## Permanent Configuration

Create or edit `/etc/sysctl.d/99-udp-buffers.conf`:

``` bash
sudo tee /etc/sysctl.d/99-udp-buffers.conf > /dev/null <<EOF
net.core.rmem_max=26214400
net.core.rmem_default=26214400
net.core.wmem_max=26214400
net.core.wmem_default=26214400
EOF
```

Apply the changes:

``` bash
sudo sysctl -p /etc/sysctl.d/99-udp-buffers.conf
```

Verify the new values:

``` bash
sysctl net.core.rmem_max
cat /proc/sys/net/core/rmem_max
```

## Application-Level Buffer Configuration

System limits set the maximum, but applications must explicitly request larger buffers. Most UDP applications have configuration options or allow socket buffer settings via `SO_RCVBUF` and `SO_SNDBUF` socket options.

In C:

``` c
int rcvbuf = 26214400;
setsockopt(sock, SOL_SOCKET, SO_RCVBUF, &rcvbuf, sizeof(rcvbuf));
```

In Python:

``` python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26214400)
```

The kernel enforces the system `rmem_max` as a hard cap—requesting a larger buffer than the system limit will be silently capped.

In Go:

``` go
import "net"
conn, _ := net.ListenUDP("udp", &net.UDPAddr{Port: 5353})
file, _ := conn.File()
defer file.Close()
syscall.SetsockoptInt(int(file.Fd()), syscall.SOL_SOCKET, syscall.SO_RCVBUF, 26214400)
```

## Right-Sizing Buffer Values

Buffer size recommendations depend on your workload:

- **DNS/NTP servers**: 1–4 MB (mostly small, bursty traffic)
- **High-frequency metrics/monitoring**: 8–16 MB
- **Syslog aggregation**: 16–32 MB
- **Video streaming/real-time media**: 32–64 MB or higher
- **General-purpose UDP services**: 16–32 MB

Choose conservatively based on observed packet loss, not theoretical maximum throughput. Oversizing wastes kernel memory.

## Impact on TCP Connections

These `rmem_max` and `wmem_max` settings also limit TCP socket buffers. Higher limits improve throughput on high-latency or high-bandwidth links. Use this formula to calculate optimal buffer size:

    buffer_size_bytes = bandwidth_Mbps × latency_ms / 8

For example, a 100 Mbps link with 50 ms latency needs at minimum: `(100 × 50) / 8 = 625 KB`. Setting buffers much higher than needed only increases kernel memory consumption.

## Monitoring and Verification

Monitor kernel memory usage to ensure buffer tuning doesn’t strain the system:

``` bash
free -h
cat /proc/meminfo | grep -E 'MemAvailable|Buffers|Cached|Slab'
```

Verify packet loss with `ethtool` (if your NIC driver supports it):

``` bash
sudo ethtool -S eth0 | grep -i drop
```

For application-specific verification, check application logs or use tcpdump to capture packets:

``` bash
sudo tcpdump -i any 'udp port 5353' -c 1000 -w /tmp/dns.pcap
```

Then analyze for gaps in sequence numbers or missing datagrams.

## Important Caveats

- **Buffer size doesn’t fix slow applications.** If your application processes data slowly, larger buffers only delay the inevitable packet loss. Profile and optimize the application first.
- **Kernel memory is finite.** On systems with many UDP sockets (load balancers, DNS resolvers), large buffers on each socket multiply quickly. Calculate total memory impact before deployment.
- **UDP loss isn’t always buffer-related.** Check for NIC drops, driver issues, or network congestion with `ip -s link` or netstat counters before assuming the kernel is the bottleneck.
