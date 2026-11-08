---
title: "Debugging File Access in Linux: Using strace and lsof"
date: 2018-03-24 08:22:44 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-which-files-are-opened-by-a-linux-program/
---

When debugging a program or understanding what it actually touches on your filesystem, you need to see which files it opens. Two tools do this well: **strace** traces system calls in real time, while **lsof** inspects a running process without the overhead.

## Using strace to capture file operations

The simplest approach is to run strace and filter for file-related syscalls:

``` bash
strace -e trace=open,openat,openat2 cat ~/.bashrc 2>&1
```

This shows which files the program tries to open. On modern Linux kernels, `openat()` and `openat2()` are the primary syscalls—`open()` is rarely used now. Including all three ensures you catch everything.

The output looks like:

    openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
    openat(AT_FDCWD, "/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
    openat(AT_FDCWD, "/home/user/.bashrc", O_RDONLY) = 5
    openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3

The number at the end (3, 5, etc.) is the file descriptor. A negative number means the open failed.

### Filtering for successful opens only

To reduce noise, show only successful file opens:

``` bash
strace -e trace=open,openat,openat2 cat ~/.bashrc 2>&1 | grep "= [0-9]"
```

### Writing to a file for later analysis

For programs that make many syscalls, save the full trace and grep it afterward:

``` bash
strace -e trace=open,openat,openat2 -o /tmp/trace.log someprogram
grep "= [0-9]" /tmp/trace.log
```

If you need to see all syscalls (not just opens), examine the full log:

``` bash
strace -o /tmp/trace.log cat ~/.bashrc
less /tmp/trace.log
```

This reveals memory mapping, library loading, signal handlers, and exit status—useful for debugging permission issues or missing dependencies.

### Following child processes

Programs that fork (shells, make, compilers) spawn child processes. Use `-f` to trace them:

``` bash
strace -f -e trace=open,openat,openat2 make build 2>&1 | tee /tmp/trace.log | grep "= [0-9]"
```

The `-f` flag is essential for build systems and daemons.

## Using lsof for running processes

If the program is already running, `lsof` is faster and doesn’t require restarting:

``` bash
# Start the program in the background
long_running_process &
PID=$!

# Inspect open files from another terminal
lsof -p $PID
```

Output includes file descriptors, file paths, access modes, and inode information in a clean table:

    COMMAND     PID USER   FD   TYPE DEVICE SIZE   NODE NAME
    python3   12345 user  cwd    DIR  10,2 4096  524288 /home/user/app
    python3   12345 user    3r   REG  10,2  1024 654321 /etc/config.yaml
    python3   12345 user    4w   REG  10,2  0    654322 /var/log/app.log
    python3   12345 user    5u  IPv4       0t0      TCP localhost:8080

Filter for specific file types:

``` bash
# Only regular files
lsof -p $PID | grep REG

# Only directories
lsof -p $PID | grep DIR

# Only network connections
lsof -p $PID | grep IPv4
```

## Comparing the tools

| Tool | Pros | Cons |
|----|----|----|
| **strace** | Shows all file operations, syscall details, includes failed attempts | Slower (5-50% overhead), requires starting the process |
| **lsof** | Fast, shows live state, clean output | Only shows currently open files, no historical operations |

Use **strace** when you need to understand what a program *tries* to do. Use **lsof** when you need to see what’s *currently* open.

## Practical examples

Check what files a web server actually reads:

``` bash
strace -e trace=open,openat,openat2 -f nginx -g 'daemon off;' 2>&1 | grep "\.conf\|\.html\|\.js"
```

Monitor a database process’s file activity:

``` bash
lsof -p $(pgrep postgres) | grep -E "REG|DIR"
```

Debug why a script is slow (check for repeated file opens):

``` bash
strace -c python3 slow_script.py
```

The `-c` flag shows a summary of syscall counts and time spent in each.

## Important notes

- strace requires the same user as the target process or root privileges
- File descriptor numbers are local to each process
- `openat2()` requires Linux 5.1+; older kernels use `openat()` exclusively
- strace output is verbose—filter by syscall type to reduce overhead
- For production debugging, prefer `lsof` over `strace` to minimize performance impact
