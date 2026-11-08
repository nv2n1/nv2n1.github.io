---
title: "Troubleshooting High TCP Retransmission Rates in VMs"
date: 2018-03-24 08:16:59 +0000
layout: post
canonical: https://www.systutorials.com/too-many-tcp-segments-retransmited-in-a-virtual-machine/
---

If you’re seeing elevated TCP segment retransmission counts on Xen VMs, this typically signals network congestion, packet loss, or CPU contention. Here’s how to identify the root cause and fix it.

### Check Your Current Retransmission Rate

Start by gathering baseline metrics:

``` bash
ss -s
```

Look for the retransmit counters:

    TCP:   established 45 tw 3 alloc 48
    segments: 537559 received 558908 sent out
    retransmitted 3533 bad 2677

Calculate your retransmission percentage: `(retransmitted / sent out) * 100`. Rates above 1-2% typically indicate a problem. In the example above, that’s roughly 0.63%, which is acceptable, but if you’re seeing 5-10%+, investigate immediately.

For continuous monitoring, use `netstat` alternatives that are more reliable on modern systems:

``` bash
# Monitor retransmits in real-time
watch -n 1 'ss -s | grep -A2 "^TCP:"'

# Or use sar for historical data
sar -n TCP 1 5
```

### Identify the Bottleneck

High retransmission rates usually stem from three sources:

**1. CPU Saturation**

With multiple VMs on a single host with limited cores, the hypervisor struggles to schedule network processing. Check host CPU usage:

``` bash
top -bn1 | head -15
vmstat 1 5
```

Watch for high `sy` (system) and `wa` (iowait) columns. If the host is CPU-bound, VMs can’t process incoming packets quickly enough, causing the network stack to drop segments.

**2. Memory Pressure and Network Buffer Exhaustion**

Check socket buffer usage on the VM:

``` bash
ss -tumen | head -20
```

Look at the `Send-Q` and `Recv-Q` columns. Persistent backlog indicates buffers are filling faster than they’re being drained. Increase TCP buffer sizes:

``` bash
# Temporary (until reboot)
sysctl -w net.ipv4.tcp_rmem="4096 87380 134217728"
sysctl -w net.ipv4.tcp_wmem="4096 65536 134217728"

# Persistent (add to /etc/sysctl.d/99-tcp.conf)
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
sysctl -p
```

**3. Network Driver or Physical Link Issues**

Check for dropped packets at the hypervisor level:

``` bash
ethtool -S vif-name
ethtool -S physical-nic
```

Look for `rx_dropped`, `tx_dropped`, and `rx_errors`. High counts point to physical network problems or driver issues.

### Solutions

**Reduce VM Density**

The most straightforward fix: don’t oversubscribe. A 4-core host should comfortably run 2-3 VMs if they’re network-intensive. The original finding—dropping from 4 VMs to 3—likely worked because it reduced CPU contention on the hypervisor’s network processing path.

**Tune VM vCPU Assignment**

Pin vCPUs to avoid migration overhead:

``` bash
virsh vcpupin domain-name 0 0
virsh vcpupin domain-name 1 1
virsh vcpupin domain-name 2 2
```

**Enable TCP Window Scaling and SACK**

Ensure these are enabled on the VM:

``` bash
sysctl net.ipv4.tcp_window_scaling
sysctl net.ipv4.tcp_sack
```

Both should return `1`. If not, enable them:

``` bash
sysctl -w net.ipv4.tcp_window_scaling=1
sysctl -w net.ipv4.tcp_sack=1
```

**Adjust RTO (Retransmission Timeout)**

On older systems or high-latency environments, increase the RTO:

``` bash
sysctl -w net.ipv4.tcp_retries2=15
```

**Monitor Long-Term with netlink**

For sustained monitoring across reboots, use `nstat`:

``` bash
nstat -a
# Run again 10 minutes later to see deltas
nstat -a
```

### The Real Issue

In most cases with VMs, high retransmission is CPU starvation at the hypervisor level. The network stack on each VM is waiting for CPU cycles to process ACKs and retransmit logic. Reducing VM density solves this immediately. If reducing VM count doesn’t help, the problem likely lives in your physical network or driver, not the VMs themselves.
