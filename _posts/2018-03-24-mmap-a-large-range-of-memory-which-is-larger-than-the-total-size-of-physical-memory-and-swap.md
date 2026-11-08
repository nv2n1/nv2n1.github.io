---
title: "Memory-mapping Ranges Larger Than Available RAM and Swap"
date: 2018-03-24 07:43:06 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/mmap-a-large-range-of-memory-which-is-larger-than-the-total-size-of-physical-memory-and-swap/
---

When you mmap() a range larger than your system’s total physical memory plus swap, the kernel normally reserves swap space to back the mapping. If that reservation would exceed available swap, mmap() fails with ENOMEM. The MAP_NORESERVE flag lets you bypass this reservation requirement.

## Understanding the Default Behavior

By default, when you call mmap() with MAP_ANONYMOUS or a file-backed mapping, the kernel reserves swap space equal to the requested size. This reservation is a safety measure: it guarantees that if pages are dirtied and need to be paged out, swap space will be available. On a system with 32GB of RAM and 16GB of swap, attempting to map 100GB without MAP_NORESERVE will fail.

The kernel enforces this through the overcommit accounting system, configurable via `/proc/sys/vm/overcommit_memory`:

- 0 (default): Heuristic overcommit — reservations are enforced but allow some flexibility
- 1: Always allow — no reservations, potential OOM killer invocations
- 2: Strict — reserves based on configured ratio

## Using MAP_NORESERVE

Adding MAP_NORESERVE tells the kernel to skip swap reservation for that specific mapping. This is useful for sparse allocations where you expect only a fraction of pages to be accessed, or for temporary buffers where you’re willing to risk SIGKILL if memory becomes critically constrained.

``` c
#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
    // Map 1TB without reserving swap
    size_t size = 1UL << 40;  // 1TB
    int prot = PROT_READ | PROT_WRITE;
    int flags = MAP_ANONYMOUS | MAP_PRIVATE | MAP_NORESERVE;

    void *addr = mmap(NULL, size, prot, flags, -1, 0);
    if (addr == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    printf("Mapped %lu bytes at %p\n", size, addr);

    // Accessing pages commits them; this may still fail if system runs out of memory
    // Write to a few scattered pages
    for (unsigned long i = 0; i < 10; i++) {
        unsigned long offset = i * (1UL << 30);  // 1GB intervals
        if (offset < size) {
            char *page = (char *)addr + offset;
            *page = 'A' + (i % 26);
        }
    }

    sleep(5);
    munmap(addr, size);
    return 0;
}
```

Compile and run:

``` bash
gcc -o mmap_noreserve mmap_noreserve.c
./mmap_noreserve
```

## Important Considerations

**Risk of OOM Kill**: Without swap reservation, if you actually populate the pages and memory becomes exhausted, the kernel’s OOM killer will terminate your process or others. MAP_NORESERVE doesn’t prevent OOM — it just defers the problem until pages are accessed.

**Sparse Access Patterns**: This flag is most practical when you genuinely use only a small fraction of the mapped range. A 10TB mapping where you access 100MB of scattered pages makes sense. A 10TB mapping where you access most pages defeats the purpose.

**File-Backed Mappings**: MAP_NORESERVE works with both anonymous and file-backed mappings. For files, the kernel still doesn’t reserve swap, but the file’s on-disk data is already allocated:

``` c
int fd = open("largefile.dat", O_RDWR);
void *addr = mmap(NULL, file_size, PROT_READ | PROT_WRITE, 
                   MAP_SHARED | MAP_NORESERVE, fd, 0);
```

**Checking System Limits**: Use `cat /proc/meminfo` to see MemAvailable and SwapFree. Check `/proc/sys/vm/max_map_count` (default 65536) if you’re creating many mappings — hitting this limit will fail mmap() regardless of memory availability.

## Alternative: Overcommit Settings

Instead of per-mapping flags, you can adjust system-wide overcommit policy:

``` bash
# Allow aggressive overcommit (risky but flexible)
echo 1 | sudo tee /proc/sys/vm/overcommit_memory

# Return to heuristic mode
echo 0 | sudo tee /proc/sys/vm/overcommit_memory
```

With `overcommit_memory=1`, mmap() succeeds freely without reservations, but you lose protection against runaway allocation. This is coarser than MAP_NORESERVE and affects all processes.

## Practical Example: Sparse Ring Buffer

A common use case is a ring buffer where you map far more space than you’ll use:

``` c
size_t buffer_size = 256UL << 20;  // 256MB actual use
size_t virtual_size = buffer_size * 4;  // Map 1GB to avoid wraparound bookkeeping
void *ring = mmap(NULL, virtual_size, PROT_READ | PROT_WRITE,
                   MAP_ANONYMOUS | MAP_PRIVATE | MAP_NORESERVE, -1, 0);

// Use only the first buffer_size bytes; remaining pages never touched
memset(ring, 0, buffer_size);
```

This pattern is safe: only the accessed portion consumes memory.

## Summary

MAP_NORESERVE is a tool for specific scenarios where you know your access pattern is sparse and you accept the OOM risk. It’s not a solution for genuinely needing terabytes of memory — it’s a way to reserve virtual address space cheaply. Use it deliberately, document why, and monitor your system for memory pressure.
