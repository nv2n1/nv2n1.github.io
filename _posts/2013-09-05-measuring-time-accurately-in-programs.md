---
title: "Choosing the Right Timer: clock_gettime vs TSC in Linux"
date: 2013-09-05 12:19:15 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /measuring-time-accurately-in-programs/
---

Measuring time accurately matters for performance profiling, benchmarking, and latency-sensitive applications. Linux provides several APIs with different tradeoffs in resolution, overhead, and reliability. Understanding which to use prevents subtle bugs in production code.

## POSIX Time APIs: gettimeofday and clock_gettime

`gettimeofday()` and `clock_gettime()` are the standard POSIX calls for reading system time. `gettimeofday()` returns seconds and microseconds but lacks resolution metadata. `clock_gettime()` is more flexible—you specify a clock type and get nanosecond precision, plus you can query resolution with `clock_getres()`.

Both functions are implemented via VDSO (Virtual Dynamic Shared Object) on modern Linux, avoiding kernel context switches. Typical overhead on x86-64:

- `gettimeofday()`: ~30 nanoseconds
- `clock_gettime(CLOCK_REALTIME)`: ~26 nanoseconds
- `clock_gettime(CLOCK_REALTIME_COARSE)`: ~8 nanoseconds
- `clock_gettime(CLOCK_MONOTONIC)`: ~26 nanoseconds
- `clock_gettime(CLOCK_MONOTONIC_COARSE)`: ~9 nanoseconds
- `clock_gettime(CLOCK_PROCESS_CPUTIME_ID)`: ~170 nanoseconds
- `clock_gettime(CLOCK_THREAD_CPUTIME_ID)`: ~154 nanoseconds

For elapsed time measurement, always use `CLOCK_MONOTONIC`. It’s unaffected by system clock adjustments via `adjtime()`, NTP, or `timedatectl set-time`. Using `CLOCK_REALTIME` can produce negative deltas or backward time jumps if the system time is adjusted during measurement.

For CPU time spent in a single-threaded process, use `CLOCK_PROCESS_CPUTIME_ID`. For multi-threaded code, measure individual thread time with `CLOCK_THREAD_CPUTIME_ID`.

### Example: Basic Elapsed Time Measurement

``` c
#include <time.h>
#include <stdio.h>

int main() {
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    // Code to measure here
    some_expensive_function();
    clock_gettime(CLOCK_MONOTONIC, &end);

    long elapsed_ns = (end.tv_sec - start.tv_sec) * 1000000000L 
                      + (end.tv_nsec - start.tv_nsec);
    printf("Elapsed: %ld ns\n", elapsed_ns);

    return 0;
}
```

The `_COARSE` variants (`CLOCK_MONOTONIC_COARSE`, `CLOCK_REALTIME_COARSE`) trade nanosecond precision for lower overhead. They update at the kernel’s jiffy interval (typically 4ms on modern systems). Use them when you’re measuring operations in the millisecond range and the function call overhead matters.

### Example: Measuring with Lower Overhead

``` c
#include <time.h>
#include <stdio.h>

int main() {
    struct timespec start, end;

    // Use _COARSE for high-frequency measurements where ns precision isn't needed
    clock_gettime(CLOCK_MONOTONIC_COARSE, &start);
    for (int i = 0; i < 1000000; i++) {
        lightweight_operation();
    }
    clock_gettime(CLOCK_MONOTONIC_COARSE, &end);

    long elapsed_ms = (end.tv_sec - start.tv_sec) * 1000L 
                      + (end.tv_nsec - start.tv_nsec) / 1000000L;
    printf("Total: %ld ms\n", elapsed_ms);

    return 0;
}
```

## TSC and RDTSC: Cycle-Level Precision on x86

For applications requiring cycle-accurate measurement on x86-64, the TSC (Time Stamp Counter) increments every CPU cycle. The `rdtsc` instruction reads this 64-bit counter directly with minimal overhead (~5ns).

### Basic RDTSC Usage

Inline assembly in C:

``` c
static inline unsigned long long rdtsc_tsc(void) {
    unsigned int lo, hi;
    asm volatile ("rdtsc" : "=a" (lo), "=d" (hi));
    return ((unsigned long long)hi << 32) | lo;
}
```

Or using `rdtscp`, which provides built-in serialization:

``` c
static inline unsigned long long rdtscp(void) {
    unsigned int lo, hi;
    asm volatile ("rdtscp" : "=a" (lo), "=d" (hi) : : "rcx");
    return ((unsigned long long)hi << 32) | lo;
}
```

### The Serialization Problem

Modern CPUs execute instructions out of order. An `rdtsc` instruction may execute before earlier instructions complete, corrupting your measurement. This is the most common pitfall.

**Problematic code:**

``` c
rdtsc              // might execute early
mov time, eax
fdiv               // slow floating-point operation
rdtsc              // might execute before fdiv completes!
sub eax, time
```

**Solution 1: Use cpuid for serialization before and after the timed section:**

``` c
cpuid();           // serializes all prior instructions
unsigned long long start = rdtsc();
some_operation();
cpuid();           // serialize before reading
unsigned long long end = rdtsc();
unsigned long long cycles = end - start;
```

**Solution 2: Use rdtscp, which serializes automatically:**

``` c
static inline void serialize_rdtsc(void) {
    asm volatile ("cpuid" : : : "%rax", "%rbx", "%rcx", "%rdx");
}

serialize_rdtsc();
unsigned long long start = rdtscp();
some_operation();
unsigned long long end = rdtscp();
unsigned long long cycles = end - start;
```

Check CPU support for `rdtscp` via CPUID leaf 0x80000001, EDX bit 27. Most modern x86-64 processors support it, but some embedded or older systems don’t.

### Multi-Core and Frequency Scaling Issues

TSC values are not guaranteed synchronized across CPU cores. When a thread migrates between cores, TSC values may jump unpredictably or even go backward.

Modern CPUs include “invariant TSC” (independent of frequency scaling), but older systems are affected by frequency changes from Intel Turbo Boost or AMD Turbo Core. Check for invariant TSC support via CPUID leaf 0x80000007, EDX bit 8.

For multi-core benchmarks, pin threads to specific cores using `sched_setaffinity()`:

``` c
#include <sched.h>

cpu_set_t set;
CPU_ZERO(&set);
CPU_SET(0, &set);  // pin to core 0
sched_setaffinity(0, sizeof(set), &set);
```

### Example: Cycle Profiling with Serialization

``` c
#include <stdio.h>
#include <string.h>

static inline unsigned long long rdtscp_serialized(void) {
    unsigned int lo, hi;
    asm volatile ("cpuid; rdtsc" : "=a" (lo), "=d" (hi) : : "rcx", "rbx");
    return ((unsigned long long)hi << 32) | lo;
}

int main() {
    unsigned long long start = rdtscp_serialized();

    // Timed operation
    char buffer[1024];
    for (int i = 0; i < 1000; i++) {
        memset(buffer, 0, sizeof(buffer));
    }

    unsigned long long end = rdtscp_serialized();
    printf("Total cycles: %llu\n", end - start);

    return 0;
}
```

### Lack of Portability

TSC is x86/x86-64 specific. ARM, RISC-V, and other architectures lack equivalent instructions. For portable code, stick with `clock_gettime()`.

## Practical Recommendations

**For most applications:** Use `clock_gettime(CLOCK_MONOTONIC, ...)` for elapsed time and `clock_gettime(CLOCK_PROCESS_CPUTIME_ID, ...)` for CPU time. It’s portable, sufficiently accurate, requires no special privileges, and avoids the pitfalls of TSC.

**For high-frequency measurements at microsecond precision or tighter:** Use `clock_gettime(CLOCK_MONOTONIC_COARSE, ...)` to reduce overhead. Benchmark first to confirm `CLOCK_MONOTONIC` isn’t already fast enough for your use case.

**For cycle-accurate profiling on x86:** Use `rdtscp` with proper serialization only when you understand the caveats. Always verify results with `clock_gettime()` sanity checks. Never rely on raw TSC across different cores without compensating for drift or pinning threads.

**For production performance testing:** Use Linux `perf` tools instead of manual timing. Commands like `perf stat` and `perf record` handle CPU scaling, multi-core effects, and provide statistical confidence that manual timing cannot match.

**General rule:** Don’t measure time in nanoseconds unless you genuinely need that precision. Most performance bottlenecks reveal themselves at microsecond granularity with `clock_gettime(CLOCK_MONOTONIC)`. Measuring at finer granularity often introduces more noise than signal.
