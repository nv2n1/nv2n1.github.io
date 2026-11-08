---
title: "Monitoring System Interrupts in Real Time"
date: 2018-03-24 11:54:21 +0000
modified: 2026-04-11 17:47:01 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /how-to-check-interrupts-lively-in-your-systems/
---

Interrupts are fundamental to how your Linux system handles hardware and software events. Monitoring them in real-time helps identify performance bottlenecks, device driver issues, and CPU load imbalances. Here’s how to check interrupts effectively.

## Quick Live Monitoring with `/proc/interrupts`

The simplest approach is reading `/proc/interrupts` directly:

``` bash
cat /proc/interrupts
```

This shows a snapshot of interrupt counts per CPU. For example:

               CPU0       CPU1       CPU2       CPU3
      0:       8934          0          0          0   IO-APIC   2-edge      timer
      1:         12          0          0          0   IO-APIC   1-edge      i8042
      8:          1          0          0          0   IO-APIC   8-edge      rtc0
      9:          0          0          0          0   IO-APIC   9-fasteoi   acpi
     24:     120480      98764      87234      92104   PCI-MSI 512000-edge  eth0

The first column is the interrupt number (IRQ), followed by counts per CPU, then the interrupt type and handler.

## Real-Time Monitoring with `watch`

To watch interrupts update in real-time:

``` bash
watch -n 1 'cat /proc/interrupts | head -20'
```

This refreshes every second and shows the top 20 interrupts. For a specific device like a network interface:

``` bash
watch -n 0.5 'grep eth0 /proc/interrupts'
```

## Using `sar` for Historical Data

The `sysstat` package provides `sar` for collecting and reporting interrupt statistics:

``` bash
# Install sysstat
sudo apt install sysstat

# Show interrupts for the last hour
sar -n INT 1 10

# Continuous monitoring (every 2 seconds for 5 iterations)
sar -n INT 2 5
```

Output includes CPU, INTR/s (interrupts per second), and per-IRQ breakdowns.

## eBPF-Based Approach with `bpftrace`

For modern kernel observability (5.8+), `bpftrace` provides zero-copy tracing:

``` bash
sudo bpftrace -e 'tracepoint:irq:irq_handler_entry { @[comm] = count(); }'
```

This counts IRQ handlers by process name with minimal overhead. For interrupt latency:

``` bash
sudo bpftrace -e 'tracepoint:irq:irq_handler_entry { @start[args.irq] = nsecs; }
tracepoint:irq:irq_handler_exit { if (@start[args.irq]) { @latency[args.irq] = hist(nsecs - @start[args.irq]); delete(@start[args.irq]); } }'
```

## Checking Interrupt Affinity

CPUs should ideally balance interrupts. Check CPU affinity for an IRQ:

``` bash
# View affinity mask for IRQ 24 (1 = use that CPU)
cat /proc/irq/24/smp_affinity

# Set IRQ 24 to use only CPU 0 and 1 (binary: 0011)
echo 3 | sudo tee /proc/irq/24/smp_affinity

# Or use irqbalance for automatic balancing
sudo systemctl enable irqbalance
```

The mask is hexadecimal. For a 4-CPU system, `0xf` means all CPUs, `0x1` means CPU0 only.

## Identifying Problem IRQs

High interrupt rates on a single CPU can cause:

- **CPU starvation** — threads don’t get scheduled
- **Cache thrashing** — context switching overhead
- **Latency spikes** — time-sensitive applications suffer

Compare before and after snapshots:

``` bash
cat /proc/interrupts > /tmp/interrupts_before
sleep 60
cat /proc/interrupts > /tmp/interrupts_after
diff /tmp/interrupts_before /tmp/interrupts_after
```

Look for IRQs with rapidly increasing counts or unbalanced distribution across CPUs.

## Tools for Deep Analysis

- **`irqstat`** — Part of `sysstat`, shows interrupt rates per second
- **`perf`** — Record interrupt samples: `sudo perf record -e irq:* -ag sleep 5`
- **`systemtap`** — Write custom probes for interrupt behavior (deprecated on newer kernels; prefer bpftrace)

## Practical Troubleshooting

**High timer interrupts** often indicate CPU frequency scaling issues. Check:

``` bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

**Network interrupts concentrated on one CPU** suggest misconfigured driver settings or missing `irqbalance`. Restart it:

``` bash
sudo systemctl restart irqbalance
```

**Spurious interrupts** (IRQ handler runs but no real event) appear in `/proc/interrupts` as unusually high counts for the IRQ type. Enable debug logging:

``` bash
sudo sysctl kernel.debug=1
dmesg | grep spurious
```

Real-time interrupt monitoring is essential for diagnosing performance issues. Start with `/proc/interrupts` and `sar`, then move to eBPF tools when you need sub-microsecond precision or kernel-space tracing.
