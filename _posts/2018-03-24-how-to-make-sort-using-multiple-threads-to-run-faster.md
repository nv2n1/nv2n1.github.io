---
title: "How to Parallelize Sorting with Multi-Threading"
date: 2018-03-24 11:52:05 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-sort-using-multiple-threads-to-run-faster/
---

The standard `sort` command is single-threaded by default, which limits performance on modern multi-core systems. Several approaches exist to speed up sorting operations using parallelism.

## GNU Sort with Parallel Sorting

Modern versions of GNU `sort` (8.23+) include built-in parallel sorting support. Enable it with the `--parallel` flag:

``` bash
sort --parallel=4 large_file.txt > sorted_output.txt
```

The `--parallel` option specifies how many threads to use. Setting it to the number of CPU cores typically yields best results:

``` bash
sort --parallel=$(nproc) large_file.txt > sorted_output.txt
```

For very large files, also adjust the buffer size with `-S`:

``` bash
sort --parallel=$(nproc) -S 2G large_file.txt > sorted_output.txt
```

The `-S` flag allocates more memory for sorting operations, reducing I/O overhead. Use roughly 50-75% of available RAM for optimal performance.

## Custom Multithreaded Sorting

For specialized sorting needs or when working with complex data structures, implement parallel sorting in Python or C.

### Python with Concurrent Processing

``` python
import sys
from multiprocessing import Pool
import os

def chunk_and_sort(args):
    filename, start, end = args
    with open(filename, 'rb') as f:
        f.seek(start)
        if start > 0:
            f.readline()  # Skip partial line

        lines = []
        while f.tell() < end:
            lines.append(f.readline())

        return sorted(lines)

def merge_sorted_chunks(chunks):
    import heapq
    return b''.join(heapq.merge(*chunks))

if __name__ == '__main__':
    filename = sys.argv[1]
    num_workers = os.cpu_count()

    file_size = os.path.getsize(filename)
    chunk_size = file_size // num_workers

    chunks = [(filename, i * chunk_size, (i + 1) * chunk_size) 
              for i in range(num_workers)]

    with Pool(num_workers) as pool:
        sorted_chunks = pool.map(chunk_and_sort, chunks)

    result = merge_sorted_chunks(sorted_chunks)
    sys.stdout.buffer.write(result)
```

### C Implementation with pthreads

``` c
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LINES 1000000
#define LINE_SIZE 4096

typedef struct {
    char **lines;
    int count;
} thread_data_t;

int compare_strings(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

void* sort_chunk(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;
    qsort(data->lines, data->count, sizeof(char*), compare_strings);
    return NULL;
}

int main() {
    int num_threads = sysconf(_SC_NPROCESSORS_ONLN);
    pthread_t threads[num_threads];
    thread_data_t thread_data[num_threads];

    // Read and distribute data...
    // Create threads
    for (int i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, sort_chunk, &thread_data[i]);
    }

    // Wait for completion
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    // Merge sorted chunks...
    return 0;
}
```

## Performance Considerations

**I/O is often the bottleneck.** Sorting CPU-bound workloads benefits significantly from parallelism, but if the data lives on slow storage or network filesystem, threading won’t help much. Use tools like `iostat` and `perf` to identify whether CPU or I/O is limiting performance.

**Memory allocation matters.** Allocate large buffers upfront rather than during sorting to avoid contention on the memory allocator. This is especially critical in multithreaded code.

**Profile before optimizing.** Use `time` to measure improvements:

``` bash
time sort --parallel=1 large_file.txt > /dev/null
time sort --parallel=$(nproc) large_file.txt > /dev/null
```

## External Sorting Tools

For data that doesn’t fit in memory, consider specialized tools:

- **GNU Sort with external merge**: Already handles this automatically with `-S` set below available RAM
- **mawk/gawk**: Less efficient than sort but can apply custom logic
- **Specialized databases**: For structured data (CSV, JSON), loading into SQLite or DuckDB and sorting there often outperforms text-based approaches

## Summary

Start with `sort --parallel=$(nproc) -S <size>` for most cases. Implement custom solutions only when sort’s options don’t meet specific requirements. Always verify improvements with actual benchmarks on representative data.
