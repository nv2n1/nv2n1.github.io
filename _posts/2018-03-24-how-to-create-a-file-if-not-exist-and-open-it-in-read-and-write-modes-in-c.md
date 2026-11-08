---
title: "Opening or Creating a File in Read-Write Mode with C++"
date: 2018-03-24 11:55:24 +0000
modified: 2026-04-11 17:12:25 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-create-a-file-if-not-exist-and-open-it-in-read-and-write-modes-in-c/
---

When you need to open a file for both reading and writing, creating it if it doesn’t exist, C++ offers several approaches. The choice depends on your project’s requirements and how much control you need over the process.

## Using std::fstream

The most straightforward modern approach uses `std::fstream`, part of the standard library:

``` cpp
#include <fstream>

std::fstream file("myfile.txt", std::ios::in | std::ios::out | std::ios::app);

if (!file.is_open()) {
    std::cerr << "Failed to open file\n";
    return 1;
}

// File is now open for reading and writing
file << "Writing to file\n";
file.seekg(0);  // Seek to beginning for reading
std::string line;
std::getline(file, line);
```

The flags work as follows:

- `std::ios::in` — open for reading
- `std::ios::out` — open for writing
- `std::ios::app` — append mode (write at end of file)

However, this approach has a limitation: `std::fstream` won’t automatically create the file if it doesn’t exist when using `std::ios::in`. To handle file creation reliably, you need to check if the file exists first:

``` cpp
#include <fstream>
#include <filesystem>

std::string filename = "myfile.txt";

// Ensure file exists
if (!std::filesystem::exists(filename)) {
    std::ofstream create(filename);
    create.close();
}

std::fstream file(filename, std::ios::in | std::ios::out | std::ios::app);
if (!file.is_open()) {
    std::cerr << "Failed to open file\n";
    return 1;
}
```

## Using POSIX open()

For lower-level control over file permissions and behavior, use the POSIX `open()` function with file descriptor operations:

``` cpp
#include <fcntl.h>
#include <unistd.h>
#include <iostream>

int fd = open("myfile.txt", O_RDWR | O_CREAT | O_CLOEXEC, 0644);

if (fd == -1) {
    std::cerr << "Failed to open file: " << strerror(errno) << "\n";
    return 1;
}

// Use fd for read/write operations
// Don't forget to close when done
close(fd);
```

The flags mean:

- `O_RDWR` — open for reading and writing
- `O_CREAT` — create file if it doesn’t exist
- `O_CLOEXEC` — close file descriptor on exec (prevents descriptor leaks in child processes)
- `0644` — file permissions (rw-r–r–)

Always specify the third argument (permissions) when using `O_CREAT`. Without it, the actual permissions depend on your process’s umask, which can lead to overly permissive files.

## Working with File Descriptors

If you’re using `open()`, you’ll typically wrap the file descriptor in a stream for easier handling:

``` cpp
#include <fcntl.h>
#include <unistd.h>
#include <iostream>

int fd = open("myfile.txt", O_RDWR | O_CREAT, 0644);
if (fd == -1) {
    perror("open");
    return 1;
}

// Convert fd to FILE* for C-style I/O
FILE *fp = fdopen(fd, "r+");
if (!fp) {
    perror("fdopen");
    close(fd);
    return 1;
}

fprintf(fp, "Writing data\n");
fflush(fp);
fclose(fp);  // This also closes the underlying fd
```

## Comparison: Which to Use?

Use `std::fstream` for:

- New C++ projects
- Applications where standard library safety is important
- Cross-platform code (POSIX semantics vary across Unix-like systems)

Use POSIX `open()` for:

- Direct control over permissions and file behavior
- Integration with event-driven I/O (epoll, kqueue)
- Embedded or performance-critical code where you need precise control

## Common Pitfalls

**Opening in append mode and not seeking:** If you open with `std::ios::app` or `O_APPEND`, writes go to the end regardless of your file position. Use `std::ios::trunc` to clear the file on opening if you want to overwrite, not append.

**Not checking file descriptor values:** After `open()`, always verify `fd != -1`. After `std::fstream::open()`, call `is_open()` to confirm success.

**Permission issues:** On shared systems, verify your umask doesn’t create unintended permissions. Test with `stat` or `ls -l` after file creation.

**Platform differences:** File descriptor limits and behaviors differ between Linux, macOS, and BSD. Always check return values and handle errors gracefully.
