---
title: "Optimizing Virtual Machine Performance: A Tuning Guide"
date: 2018-03-24 11:54:16 +0000
author: "Weiwei Jia"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-tune-systems-to-achieve-high-performance-in-virtualization-circumstances/
---

Achieving high performance in virtualized environments requires careful tuning of kernel parameters, CPU idle states, and hypervisor settings. The goal is to reduce context switching overhead, minimize latency, and keep vCPUs busy rather than cycling through low-power states.

## Kernel Boot Parameters

Add these parameters to your kernel boot line in `/etc/default/grub`:

    intel_idle.max_cstate=0 processor.max_cstate=0 idle=poll intel_pstate=disable

After editing, regenerate your GRUB configuration:

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

Here’s what each parameter does:

- `intel_idle.max_cstate=0` — Disables C-state transitions in the intel_idle driver, preventing the CPU from entering deep sleep states
- `processor.max_cstate=0` — Disables C-state transitions via the acpi-cpufreq driver as a fallback
- `idle=poll` — Forces the CPU to busy-poll instead of entering sleep states when idle. This keeps the core hot and responsive but consumes more power
- `intel_pstate=disable` — Disables the intel_pstate driver in favor of the traditional acpi-cpufreq driver, which gives you better control over frequency scaling in virtualized workloads

The tradeoff is clear: lower latency and better performance for guest VMs at the cost of higher power consumption and CPU heat.

## Pause Loop Exiting (PLE)

PLE is a hypervisor optimization that detects when a vCPU is spinning in a busy loop (waiting for a lock) and yields the physical CPU to another task rather than burning cycles. In some workloads, disabling PLE can reduce latency.

### Disable PLE

``` bash
sudo rmmod kvm_intel
sudo modprobe kvm_intel ple_gap=0 ple_window=0
cat /sys/module/kvm_intel/parameters/ple*
```

The `ple_gap` and `ple_window` parameters control the PLE detection mechanism. Setting both to 0 disables it entirely.

### Re-enable PLE

``` bash
sudo rmmod kvm_intel
sudo modprobe kvm_intel
cat /sys/module/kvm_intel/parameters/ple*
```

This reloads the module with default parameters (PLE enabled).

## How idle=poll Affects PLE

When `idle=poll` is set, vCPUs execute NOP instructions in a spin-loop when idle instead of sleeping. If PLE is enabled, the hypervisor detects this spinning pattern and potentially yields the physical CPU — defeating the purpose of poll-based idling. For maximum latency-sensitive performance, you’ll typically want to disable PLE when using `idle=poll`.

## Checking Current Settings

View your active kernel parameters:

``` bash
cat /proc/cmdline
```

Check if PLE is enabled:

``` bash
cat /sys/module/kvm_intel/parameters/ple_gap
cat /sys/module/kvm_intel/parameters/ple_window
```

Monitor actual C-state usage:

``` bash
sudo apt install intel-pstate-turbo-num-freq-levels  # or equivalent on your distro
cat /sys/devices/system/cpu/cpu*/cpuidle/state*/time_in_state
```

## When to Apply These Tunings

This configuration is appropriate for:

- **Low-latency workloads** — trading power efficiency for predictable response times
- **Real-time applications** running in VMs
- **High-throughput, CPU-bound workloads** where guests have exclusive vCPU pinning
- **Database servers or in-memory caches** where context switching is expensive

It is **not** appropriate for:

- General-purpose shared hosting where multiple tenants’ VMs run on the same hardware
- Power-constrained environments (edge, battery-powered systems)
- Workloads that benefit from frequency scaling (most modern applications)

## AMD Systems

On AMD hypervisors with KVM, adjust the module parameters for `kvm_amd` instead:

``` bash
sudo rmmod kvm_amd
sudo modprobe kvm_amd pause_filter_count=0 pause_filter_thresh=0
```

AMD’s equivalent to PLE is the pause filter. Setting these to 0 disables pause filtering.

## Persistence Across Reboots

To make KVM module parameters persistent, create a configuration file:

``` bash
echo "options kvm_intel ple_gap=0 ple_window=0" | sudo tee /etc/modprobe.d/kvm-intel.conf
```

Then regenerate the initramfs:

``` bash
sudo update-initramfs -u
```

Verify after reboot:

``` bash
cat /sys/module/kvm_intel/parameters/ple_gap
```

## Measuring Impact

Use `perf` or `turbostat` to measure context switches and CPU time before and after tuning:

``` bash
sudo turbostat -i 1
```

Monitor guest performance with `vmstat` or `iostat` inside the VM to detect improvements in throughput and latency.
