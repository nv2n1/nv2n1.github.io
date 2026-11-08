---
title: "Closing File Streams in C with fclose()"
date: 2013-07-12 16:47:45 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/fclose-close-a-stream/
---

`fclose()` closes a file stream and disassociates it from its underlying file descriptor. It’s part of the C standard library, defined in `<stdio.h>`.

``` c
#include <stdio.h>
int fclose(FILE *stream);
```

When called, `fclose()` flushes buffered output, closes the file descriptor, and deallocates the `FILE` structure. The function works with both input and output streams. After `fclose()` returns, the stream pointer becomes invalid and must not be used again.

## Return Values and Error Handling

`fclose()` returns:

- **0** on success
- **EOF** on error, with `errno` set to indicate the failure

Common error codes include:

- `EBADF`: Invalid file descriptor
- `EIO`: I/O error during flush or close
- `EINTR`: Signal interrupted the call
- `ENOSPC`: File system full (during flush)

Always check the return value. Errors during `fclose()` often indicate I/O problems that occurred during the flush operation, even if earlier writes appeared successful.

``` c
#include <stdio.h>
#include <errno.h>
#include <string.h>

FILE *fp = fopen("file.txt", "r");
if (fp == NULL) {
    perror("fopen");
    return 1;
}

// ... file operations ...

if (fclose(fp) == EOF) {
    fprintf(stderr, "fclose error: %s\n", strerror(errno));
    return 1;
}
```

## Data Durability: The Critical Gap

A frequently overlooked issue: `fclose()` only flushes user-space buffers managed by the C library. Data may still reside in kernel buffers and not be physically written to disk. For applications handling critical data, this distinction matters.

If you call `fsync()` after `fclose()`, it won’t work:

``` c
FILE *fp = fopen("data.txt", "w");
fprintf(fp, "important data");
fclose(fp);
fsync(fileno(fp));  // Error — fp is already closed
```

Instead, sync the file descriptor before closing:

``` c
#include <unistd.h>
#include <stdio.h>

FILE *fp = fopen("data.txt", "w");
if (fp == NULL) {
    perror("fopen");
    return 1;
}

fprintf(fp, "important data");
fflush(fp);

int fd = fileno(fp);
if (fsync(fd) == -1) {
    perror("fsync");
    fclose(fp);
    return 1;
}

if (fclose(fp) == EOF) {
    perror("fclose");
    return 1;
}
```

If metadata synchronization isn’t needed, use `fdatasync()` instead for better performance:

``` c
if (fdatasync(fd) == -1) {
    perror("fdatasync");
    fclose(fp);
    return 1;
}

if (fclose(fp) == EOF) {
    perror("fclose");
    return 1;
}
```

Even `fsync()` doesn’t guarantee durability on all storage systems. Network filesystems, certain SSDs with write caches, and storage arrays may still lose data after a crash. For critical applications, investigate your storage layer and consider additional measures like replication or write-ahead logging.

## Basic Example

``` c
#include <stdio.h>

int main(void)
{
    FILE *fp = fopen("output.txt", "w");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    fprintf(fp, "fclose example\n");

    if (fclose(fp) == EOF) {
        perror("fclose");
        return 1;
    }

    return 0;
}
```

## Resource Cleanup Patterns

Ensure `fclose()` is called on all code paths after a successful `fopen()`. In complex functions with multiple error conditions, use a cleanup label with `goto`:

``` c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int process_file(const char *filename)
{
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    int ret = 0;
    char buf[256];

    while (fgets(buf, sizeof(buf), fp) != NULL) {
        if (some_error_condition) {
            fprintf(stderr, "Processing error\n");
            ret = 1;
            break;
        }
    }

    if (ferror(fp)) {
        fprintf(stderr, "Read error: %s\n", strerror(errno));
        ret = 1;
    }

cleanup:
    if (fclose(fp) == EOF) {
        fprintf(stderr, "fclose error: %s\n", strerror(errno));
        return 1;
    }

    return ret;
}
```

For simpler cases, structure code with early returns:

``` c
FILE *fp = fopen("file.txt", "r");
if (fp == NULL) {
    perror("fopen");
    return 1;
}

if (some_error_condition) {
    fclose(fp);
    return 1;
}

// ... more processing ...

if (fclose(fp) == EOF) {
    perror("fclose");
    return 1;
}
```

## Common Mistakes

**Double close**: Don’t close the same stream twice:

``` c
fclose(fp);
fclose(fp);  // Undefined behavior
```

**Use after close**: Don’t read from or write to a closed stream:

``` c
fclose(fp);
fprintf(fp, "data");  // Undefined behavior
```

**Resource leaks**: Ensure `fclose()` executes on all paths where `fopen()` succeeded:

``` c
FILE *fp = fopen("file.txt", "r");
if (some_error_condition) {
    return 1;  // fp never closed — resource leak
}
fclose(fp);
```

## Portability

`fclose()` is specified in C89, C99, C11, and C23 standards, as well as POSIX specifications. Behavior is consistent across POSIX systems including Linux, BSD, and macOS.
