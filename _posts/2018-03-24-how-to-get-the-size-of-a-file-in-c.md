---
title: "Getting File Size in C"
date: 2018-03-24 08:08:22 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-size-of-a-file-in-c/
---

There are several ways to determine a file’s size in C, each with different trade-offs. Choose based on whether you have a file descriptor, stream, or just the filename.

### Using `stat()` with a Filename

If you know the filename, `stat()` is the most straightforward approach:

``` c
#include <sys/stat.h>
#include <stdio.h>

int main(const char *filename) {
    struct stat st;

    if (stat(filename, &st) == -1) {
        perror("stat");
        return 1;
    }

    off_t size = st.st_size;
    printf("File size: %ld bytes\n", size);
    return 0;
}
```

Always check the return value — `stat()` returns -1 on error and sets `errno`. Use `perror()` or check `errno` directly for debugging.

### Using `fstat()` with a File Descriptor

If you already have a file descriptor (from `open()`, `fileno()`, etc.), use `fstat()`:

``` c
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int fd = open("myfile.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    struct stat st;
    if (fstat(fd, &st) == -1) {
        perror("fstat");
        close(fd);
        return 1;
    }

    off_t size = st.st_size;
    printf("File size: %ld bytes\n", size);
    close(fd);
    return 0;
}
```

### Using `fseek()` and `ftell()` with a Stream

If you’re working with a `FILE*` stream, you can seek to the end and use `ftell()`:

``` c
#include <stdio.h>

long get_file_size(FILE *f) {
    if (fseek(f, 0, SEEK_END) == -1) {
        return -1;
    }

    long size = ftell(f);

    if (fseek(f, 0, SEEK_SET) == -1) {
        return -1;
    }

    return size;
}
```

This approach **modifies the file pointer position**, so you must seek back to the beginning before reading. It also works only on seekable streams; pipes, sockets, and some other files will fail. Additionally, `ftell()` returns a `long`, which may overflow on very large files (though this is rare in practice).

### Why Prefer `stat()` or `fstat()`

For most use cases, `stat()` or `fstat()` are better choices because:

- They don’t require reading or seeking through the file
- `fstat()` works with any file descriptor, including pipes and sockets (though it may return -1 for some)
- They return `off_t`, a 64-bit type on modern systems, handling large files correctly
- They provide additional metadata (permissions, timestamps, inode, etc.) if needed

### Important Notes on Large Files

For files larger than 2GB, ensure your system is configured for large file support. On 32-bit systems, you may need to compile with `-D_FILE_OFFSET_BITS=64` or use the `stat64()` and `fstat64()` functions. Modern 64-bit systems handle this automatically.

Also be aware that `st.st_size` reflects the logical file size, not necessarily disk usage. For sparse files, the actual space used may be much less. For allocated space, check `st.st_blocks` (measured in 512-byte blocks).

### Example: Complete File Reading Function

Here’s a practical function combining size detection with safe memory allocation:

``` c
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

char *read_file(const char *filename) {
    struct stat st;

    if (stat(filename, &st) == -1) {
        perror("stat");
        return NULL;
    }

    if (st.st_size > 1024 * 1024 * 1024) {  // 1GB limit
        fprintf(stderr, "File too large\n");
        return NULL;
    }

    char *buffer = malloc(st.st_size + 1);
    if (!buffer) {
        perror("malloc");
        return NULL;
    }

    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        perror("open");
        free(buffer);
        return NULL;
    }

    ssize_t bytes_read = read(fd, buffer, st.st_size);
    close(fd);

    if (bytes_read != st.st_size) {
        fprintf(stderr, "Read error\n");
        free(buffer);
        return NULL;
    }

    buffer[st.st_size] = '\0';
    return buffer;
}
```

Always validate file sizes before allocating memory to prevent denial-of-service scenarios.
