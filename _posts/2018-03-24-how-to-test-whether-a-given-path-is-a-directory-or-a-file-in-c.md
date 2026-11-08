---
title: "Checking if a Path is a Directory or File in C++"
date: 2018-03-24 11:54:49 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-test-whether-a-given-path-is-a-directory-or-a-file-in-c/
---

Determining whether a path points to a directory or regular file is a common task in system programming. You need to stat the path and inspect the file mode.

## Using lstat() and stat macros

The `lstat()` system call retrieves file metadata into a `struct stat`. For a given path, you can use the standard macros `S_ISDIR()`, `S_ISREG()`, and others to test the file type based on the `st_mode` field.

Key differences between `stat()` and `lstat()`:

- `stat()` follows symbolic links and returns info about the target
- `lstat()` returns info about the link itself without following it

Use `lstat()` when you need to detect and handle symlinks separately. Use `stat()` when you want transparent link dereferencing.

## Basic implementation

Here’s a working example:

``` cpp
#include <sys/stat.h>
#include <iostream>
#include <string>
#include <cstring>

std::string pathtype(const std::string& path) {
    struct stat s;

    if (lstat(path.c_str(), &s) != 0) {
        return "error";
    }

    if (S_ISDIR(s.st_mode)) {
        return "a dir";
    } else if (S_ISREG(s.st_mode)) {
        return "a file";
    } else if (S_ISLNK(s.st_mode)) {
        return "a symlink";
    } else {
        return "unknown";
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " path\n";
        return 1;
    }

    std::cout << pathtype(argv[1]) << "\n";
    return 0;
}
```

Compile with:

``` bash
g++ -o pathtype pathtype.cpp
```

Test it:

``` bash
$ touch /tmp/file.txt
$ ./pathtype /tmp/file.txt
a file

$ mkdir /tmp/dir.txt
$ ./pathtype /tmp/dir.txt
a dir

$ ln -s /tmp/file.txt /tmp/link.txt
$ ./pathtype /tmp/link.txt
a symlink
```

## Other file type checks

The `<sys/stat.h>` header provides additional macros for other file types:

- `S_ISREG()` — regular file
- `S_ISDIR()` — directory
- `S_ISLNK()` — symbolic link
- `S_ISCHR()` — character device
- `S_ISBLK()` — block device
- `S_ISFIFO()` — FIFO/named pipe
- `S_ISSOCK()` — socket

## Modern C++ approach using `std::filesystem`

For new C++ projects (C++17 and later), prefer `std::filesystem` for cleaner, more portable code:

``` cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " path\n";
        return 1;
    }

    try {
        fs::path p(argv[1]);

        if (fs::is_directory(p)) {
            std::cout << p << " is a dir\n";
        } else if (fs::is_regular_file(p)) {
            std::cout << p << " is a file\n";
        } else if (fs::is_symlink(p)) {
            std::cout << p << " is a symlink\n";
        } else {
            std::cout << p << " type is unknown\n";
        }
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
```

Compile with C++17 support:

``` bash
g++ -std=c++17 -o pathtype pathtype.cpp
```

The `std::filesystem` approach is preferred because it:

- Handles path separators correctly across platforms
- Throws exceptions for clear error handling
- Provides a consistent interface for many file operations
- Works on Windows, macOS, and Linux without modification

## Error handling

Always check the return value of `lstat()`. A return value of -1 indicates failure; check `errno` for the specific error:

``` cpp
#include <cerrno>

if (lstat(path.c_str(), &s) != 0) {
    std::cerr << "lstat failed: " << std::strerror(errno) << "\n";
    return 1;
}
```

Common errors:

- `ENOENT` — path does not exist
- `EACCES` — permission denied
- `ENOTDIR` — component of path is not a directory
