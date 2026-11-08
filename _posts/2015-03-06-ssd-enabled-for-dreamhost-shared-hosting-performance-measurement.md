---
title: "Benchmarking SSD Performance on Shared Hosting Without Root"
date: 2015-03-06 11:02:22 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/ssd-enabled-for-dreamhost-shared-hosting-performance-measurement/
---

SSD storage is standard across modern hosting providers. DreamHost and competitors have shifted entirely to SSD-backed shared hosting. The marketing claim of “200% faster page loads” deserves skepticism, but SSD-backed hosting does deliver measurable I/O improvements for realistic workloads.

This post covers practical performance measurement techniques on a shared hosting account where you lack root access — the actual constraint most shared hosting users face.

## Testing Constraints on Shared Hosting

Testing I/O on shared hosting differs fundamentally from testing on dedicated hardware or a VPS. You cannot:

- Flush kernel buffers or drop caches
- Isolate your workload from concurrent user activity
- Control system load or I/O contention
- Run privileged monitoring tools

These tests should be treated as baseline measurements, not definitive performance claims. Shared hosting servers run dozens or hundreds of sites simultaneously, and I/O contention varies throughout the day. Morning performance differs from evening performance.

## Testing Small File I/O Performance

Moving files between disk and RAM (`/dev/shm/`) isolates sequential read/write performance:

``` bash
$ ls -lha 49MBfile.pdf
-rwxr-xr-x 1 test pg000000 49M Mar  5 23:23 49MBfile.pdf

$ time mv ./49MBfile.pdf /dev/shm/
real    0m0.602s
user    0m0.012s
sys     0m0.176s

$ time mv /dev/shm/49MBfile.pdf ./
real    0m0.307s
user    0m0.008s
sys     0m0.216s

$ time mv ./49MBfile.pdf /dev/shm/
real    0m0.291s
user    0m0.016s
sys     0m0.172s

$ time mv /dev/shm/49MBfile.pdf ./
real    0m0.225s
user    0m0.000s
sys     0m0.208s

$ time mv ./49MBfile.pdf /dev/shm/
real    0m0.331s
user    0m0.000s
sys     0m0.188s

$ time mv /dev/shm/49MBfile.pdf ./
real    0m0.262s
user    0m0.000s
sys     0m0.216s
```

The initial move (0.602s) yields approximately 81.4 MB/s. Subsequent runs stabilize around 250-300ms, indicating kernel cache warmth improves performance. The `sys` time dominates because `mv` on the same filesystem is a metadata operation, not a full data copy.

## Sequential Write Throughput with Direct I/O

Using `dd` with the `oflag=direct` flag bypasses the page cache and measures actual disk write speed:

``` bash
$ dd if=/dev/zero of=./testfile bs=512M count=1 oflag=direct
1+0 records in
1+0 records out
536870912 bytes (537 MB) copied, 9.26255 s, 58.0 MB/s

$ time mv testfile /dev/shm/
real    0m4.802s
user    0m0.052s
sys     0m2.148s
```

This produces:

- **Write throughput**: 58.0 MB/s (via `dd` with `oflag=direct`)
- **Read throughput**: 111.8 MB/s (537 MB ÷ 4.802s)

The `oflag=direct` flag forces unbuffered I/O, so 58 MB/s represents actual SSD write speed under contention on a shared system. The higher read speed reflects cached performance — the kernel buffers recently written data in memory.

## Testing Random I/O Performance

Database workloads depend more on random I/O than sequential throughput. Test random read latency without requiring root:

``` bash
$ dd if=./testfile of=/dev/null bs=4K skip=$((RANDOM % 131072)) count=1000 iflag=direct
1000+0 records in
1000+0 records out
4096000 bytes (4.1 MB) copied, 0.087234 s, 46.9 MB/s
```

For smaller random reads:

``` bash
$ time for i in {1..100}; do dd if=./testfile of=/dev/null bs=4K count=1 iflag=direct 2>/dev/null; done
real    0m0.543s
```

This suggests ~5.4ms average latency per random 4KB read — acceptable for shared hosting but much slower than NVMe-backed systems (\< 0.5ms).

## Interpreting the Numbers

For shared hosting workloads (WordPress, static sites, small applications):

- **58 MB/s sustained writes**: Adequate for log rotation, backup operations, and user uploads
- **100+ MB/s cached reads**: Covers typical PHP/Python application code and asset serving
- **Millisecond-scale operation times**: Indicates responsive disk I/O for typical requests

Comparison points:

- HDD-based shared hosting: 10–20 MB/s
- SSD shared hosting: 50–100 MB/s (what you’re testing)
- NVMe VPS: 500+ MB/s (different price tier)
- Local SSD laptop: 400–600 MB/s

## What These Results Mean for Your Application

SSD-backed shared hosting performs well for:

- **Database query caching**: MySQL and PostgreSQL benefit significantly from faster random I/O and lower latency
- **Static asset serving**: Images, CSS, and JavaScript load measurably faster
- **Application code loading**: PHP opcode caches and Python bytecode compilation work better with responsive disk I/O
- **Log aggregation**: Web server and application logs flush to disk faster

Where you’ll still hit limits:

- **Bulk file operations**: Migrations and backups still require time proportional to data size
- **High concurrency**: Thousands of simultaneous requests will saturate I/O regardless of SSD speed
- **Heavy database workloads**: Optimization queries and indexes matter more than raw I/O speed

## Practical Testing Recommendations

Run tests at different times of day — shared hosting I/O performance varies with overall server load. Early morning typically shows higher throughput than peak hours.

Test your own application under realistic load instead of relying on synthetic benchmarks. Profile your actual PHP/Node.js/Python application with tools like `strace`, `py-spy`, or `perf` (if available) to identify actual bottlenecks.

For most shared hosting users, SSD adoption eliminated the obvious storage performance problem. If your site is still slow, look at database query optimization, inefficient application code, and excessive third-party API calls before blaming disk I/O.
