---
title: "How to Monitor Process I/O Utilization"
date: 2018-03-24 11:54:03 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /how-to-get-processes-i-o-utilization-percentage/
---

Getting accurate I/O metrics per process is critical for troubleshooting performance issues, identifying storage bottlenecks, and capacity planning. Linux provides several tools for this task, each with different trade-offs between accuracy and overhead.

## Using `/proc/[pid]/io`

The simplest approach is reading directly from the proc filesystem. Each process has an `io` file containing I/O statistics:

``` bash
cat /proc/1234/io
```

Output looks like:

    rchar: 1234567
    wchar: 7654321
    syscr: 456
    syscw: 789
    read_bytes: 2097152
    write_bytes: 5242880
    cancelled_write_bytes: 0

The relevant fields are:

- `read_bytes`: Physical bytes read from storage
- `write_bytes`: Physical bytes written to storage
- `rchar` and `wchar`: Characters read/written (includes page cache)

To get current I/O rate, sample these values twice with a time interval:

``` bash
#!/bin/bash
pid=$1
interval=${2:-1}

read_bytes_start=$(grep "^read_bytes" /proc/$pid/io | awk '{print $2}')
write_bytes_start=$(grep "^write_bytes" /proc/$pid/io | awk '{print $2}')
timestamp_start=$(date +%s%N)

sleep $interval

read_bytes_end=$(grep "^read_bytes" /proc/$pid/io | awk '{print $2}')
write_bytes_end=$(grep "^write_bytes" /proc/$pid/io | awk '{print $2}')
timestamp_end=$(date +%s%N)

elapsed=$(echo "scale=3; ($timestamp_end - $timestamp_start) / 1000000000" | bc)
read_rate=$(echo "scale=2; ($read_bytes_end - $read_bytes_start) / $elapsed / 1024 / 1024" | bc)
write_rate=$(echo "scale=2; ($write_bytes_end - $write_bytes_start) / $elapsed / 1024 / 1024" | bc)

echo "Read: ${read_rate} MB/s"
echo "Write: ${write_rate} MB/s"
```

**Limitations**: This approach doesn’t give you percentage utilization relative to disk capacity. It only shows throughput.

## Using `iotop`

`iotop` is purpose-built for this task and shows actual disk I/O per process:

``` bash
sudo iotop -o -b -n 1
```

Flags:

- `-o`: Show only processes doing I/O
- `-b`: Batch mode (non-interactive)
- `-n 1`: Exit after one iteration

Output includes `DISK READ`, `DISK WRITE`, and `IO%` columns. The `IO%` represents the percentage of time the disk was busy servicing that process’s I/O requests.

For continuous monitoring:

``` bash
sudo iotop -d 2 -o
```

This refreshes every 2 seconds showing only active processes.

## Using `pidstat`

The `pidstat` tool from sysstat package provides flexible I/O reporting:

``` bash
sudo pidstat -d -p 1234 1 10
```

This shows I/O stats for PID 1234, sampling every 1 second for 10 iterations. Output columns include:

- `kB_rd/s`: KB read per second
- `kB_wr/s`: KB written per second
- `kB_ccwr/s`: Cancelled write KB/s (important for understanding actual vs attempted I/O)

For all processes with significant I/O:

``` bash
sudo pidstat -d -u 1
```

## eBPF-Based Approaches

For production environments requiring minimal overhead and kernel-level insights, eBPF tools are superior. These use in-kernel filtering to avoid expensive context switches:

``` bash
sudo apt install bpftrace
```

A simple tracing script:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_read,
                   tracepoint:syscalls:sys_enter_write {
  @[comm] = count();
}'
```

This counts read/write syscalls by process name without overhead of context switching back to userspace.

For production-grade monitoring, tools like **Cilium Hubble** and **Datadog** provide eBPF-based I/O telemetry that’s far more efficient than traditional tools.

## Practical Considerations

- `/proc/[pid]/io` is always available but requires root on some systems
- `iotop` gives the clearest picture but uses some CPU sampling overhead
- `pidstat` is best for scripting and integration into monitoring systems
- eBPF tools scale to thousands of processes without performance degradation

For containerized workloads, use `cgroup` v2 I/O limits and monitoring which integrate directly with container runtimes:

``` bash
cat /sys/fs/cgroup/system.slice/docker-*.scope/io.stat
```

Choose your tool based on whether you need real-time interactivity (`iotop`), scriptable metrics (`pidstat`), or production-scale observability (eBPF platforms).
