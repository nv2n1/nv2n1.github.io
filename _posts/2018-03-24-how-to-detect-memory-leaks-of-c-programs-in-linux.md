---
title: "Memory Leak Detection Tools for C on Linux"
date: 2018-03-24 08:22:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-detect-memory-leaks-of-c-programs-in-linux/
---

Memory leak detection is critical for C program reliability. Several tools work at different stages of development—compile time, runtime, and production scenarios. Your choice depends on performance tolerance, integration needs, and how much detail you require.

## AddressSanitizer (ASan)

AddressSanitizer is the first tool to reach for in 2026. It’s compiler-integrated, fast, and catches a broader range of memory errors than older tools.

Compile with sanitizer flags:

``` bash
gcc -fsanitize=address -fsanitize=leak -g -O1 -o your_program your_program.c
clang -fsanitize=address -fsanitize=leak -g -O1 -o your_program your_program.c
```

Run the binary:

``` bash
./your_program
```

ASan instruments the binary at compile time and runs with roughly 2-3x slowdown—acceptable for development and testing. It catches heap overflows, use-after-free, double-free errors, and memory leaks in one pass.

For detailed output:

``` bash
ASAN_OPTIONS=verbosity=2:halt_on_error=1 ./your_program
LSAN_OPTIONS=report_objects=1 ./your_program
```

ASan is built into GCC 5+ and Clang, making it the practical default. When combined with `-O1` optimization, you get debugging symbols without severe performance loss.

For multi-threaded programs, you may want to suppress race detection warnings while focusing on leaks:

``` bash
ASAN_OPTIONS=detect_leaks=1:detect_races=0 ./your_program
```

## Valgrind

Valgrind remains valuable for deep debugging when ASan doesn’t catch something or when you need detailed allocation history. It instruments the binary at runtime without requiring recompilation.

Basic usage:

``` bash
valgrind --leak-check=full --show-leak-kinds=all ./your_program
```

Key flags:

- `--leak-check=full`: Shows each individual leak
- `--show-leak-kinds=all`: Reports definite, indirect, possible, and reachable leaks
- `--track-origins=yes`: Traces where uninitialized values originated (slower, use when needed)
- `--log-file=valgrind.log`: Writes output to a file
- `--suppressions=file.supp`: Suppresses known leaks from system libraries
- `--max-stacktrace=30`: Increases default stack depth for better context

For long-running programs:

``` bash
valgrind --leak-check=full --log-file=valgrind.%p.log ./your_program arg1 arg2
```

The main tradeoff: Valgrind runs programs 10-50x slower. Use it during targeted debugging sessions, not routine testing. For CI/CD pipelines, ASan is more practical.

To suppress third-party library leaks, create a suppression file:

``` bash
valgrind --gen-suppressions=all --leak-check=full ./your_program 2>&1 | grep -A 5 "^{" > leaks.supp
```

Then use it:

``` bash
valgrind --suppressions=leaks.supp --leak-check=full ./your_program
```

## LeakSanitizer (LSan) Standalone

LeakSanitizer can run without AddressSanitizer for lighter overhead if you only care about leaks:

``` bash
gcc -fsanitize=leak -g -O1 -o your_program your_program.c
./your_program
```

This is useful when ASan’s memory overhead is problematic on resource-constrained systems, though you lose detection of buffer overflows and use-after-free errors.

## gperftools (Google Performance Tools)

For production-like profiling with minimal overhead, Google’s heap profiler works well:

``` bash
sudo apt install google-perftools libgoogle-perftools-dev
gcc -o your_program your_program.c -ltcmalloc
```

Run with heap profiling:

``` bash
HEAPPROFILE=/tmp/heap_profile ./your_program
pprof --text /tmp/heap_profile.0001.heap
```

gperftools adds roughly 2-5% overhead and integrates naturally into long-running services. It’s useful for finding leak patterns in production scenarios where ASan isn’t suitable.

## Static Analysis

Clang’s static analyzer catches obvious issues at compile time:

``` bash
scan-build gcc -Wall -Wextra your_program.c
```

This catches use-after-free and null pointer dereferences statically but won’t detect runtime leaks. Run it as part of your build process, not as a substitute for runtime tools.

## Practical Workflow

Start with AddressSanitizer during development—compile once with `-fsanitize=address -fsanitize=leak -g`, run tests, and fix issues immediately. The fast feedback loop catches most problems early.

When ASan misses something or you need deep investigation, switch to Valgrind. Create a suppression file for third-party library leaks so you focus on your code.

For CI/CD integration, run ASan on every build. Schedule Valgrind runs weekly or pre-release if resources allow. Use static analysis as a baseline check that requires no runtime overhead.

In production, consider lightweight heap profiling with gperftools or LSan if you need leak detection under realistic load.

Enable debug symbols unconditionally during development:

``` bash
CFLAGS="-g -fsanitize=address -fsanitize=leak -O1"
make clean && make
```

Test with realistic data. Memory leaks often only appear under specific conditions—edge cases, large datasets, or particular access patterns. Your test suite should exercise these scenarios.
