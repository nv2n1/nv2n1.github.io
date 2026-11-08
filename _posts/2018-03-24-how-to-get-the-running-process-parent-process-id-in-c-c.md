---
title: "How to Get a Process\u2019s Parent PID in C/C++"
date: 2018-03-24 11:52:54 +0000
modified: 2026-04-11 17:12:51 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-the-running-process-parent-process-id-in-c-c/
---

To retrieve the parent process ID (PPID) of the current running process, use the `getppid()` system call. This is the standard and portable approach on Unix-like systems including Linux.

``` c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t ppid = getppid();
    printf("Parent process ID: %d\n", ppid);
    return 0;
}
```

Compile and run:

``` bash
gcc -o get_ppid get_ppid.c
./get_ppid
```

The `getppid()` call returns the PID of the parent process. This value can change if the parent terminates before the child—the kernel will reparent the process to init (PID 1) or systemd (on modern distributions).

## Getting PPID for a specific process

To retrieve the parent PID of any running process (not just the current one), read from `/proc/[pid]/stat`:

``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

pid_t get_ppid_of_process(pid_t pid) {
    char path[256];
    char stat_line[1024];
    pid_t ppid;

    snprintf(path, sizeof(path), "/proc/%d/stat", pid);
    FILE *f = fopen(path, "r");

    if (!f) {
        perror("fopen");
        return -1;
    }

    if (fgets(stat_line, sizeof(stat_line), f)) {
        // Format: pid (comm) state ppid ...
        // The PPID is the 4th field
        sscanf(stat_line, "%*d %*s %*c %d", &ppid);
        fclose(f);
        return ppid;
    }

    fclose(f);
    return -1;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <pid>\n", argv[0]);
        return 1;
    }

    pid_t target_pid = atoi(argv[1]);
    pid_t ppid = get_ppid_of_process(target_pid);

    if (ppid > 0) {
        printf("Parent PID of process %d: %d\n", target_pid, ppid);
    } else {
        fprintf(stderr, "Could not retrieve parent PID\n");
    }

    return 0;
}
```

## Using /proc/self for the current process

You can also read `/proc/self/stat` directly without calling `getppid()`:

``` c
#include <stdio.h>

pid_t get_ppid_from_proc() {
    FILE *f = fopen("/proc/self/stat", "r");
    if (!f) return -1;

    pid_t ppid;
    char line[1024];

    if (fgets(line, sizeof(line), f)) {
        sscanf(line, "%*d %*s %*c %d", &ppid);
        fclose(f);
        return ppid;
    }

    fclose(f);
    return -1;
}
```

This approach is useful when you need to parse other fields from `/proc/[pid]/stat` simultaneously.

## In C++

For C++, wrap the logic in a class or use the same system calls directly:

``` cpp
#include <iostream>
#include <unistd.h>
#include <fstream>
#include <sstream>

class ProcessInfo {
public:
    static pid_t GetParentPID() {
        return getppid();
    }

    static pid_t GetParentPID(pid_t pid) {
        std::string path = "/proc/" + std::to_string(pid) + "/stat";
        std::ifstream f(path);

        if (!f.is_open()) {
            return -1;
        }

        std::string line;
        if (std::getline(f, line)) {
            std::istringstream iss(line);
            pid_t p, ppid;
            std::string comm, state;

            iss >> p >> comm >> state >> ppid;
            return ppid;
        }

        return -1;
    }
};

int main() {
    std::cout << "My PPID: " << ProcessInfo::GetParentPID() << std::endl;
    std::cout << "PPID of PID 1: " << ProcessInfo::GetParentPID(1) << std::endl;
    return 0;
}
```

## Important considerations

**Permission access**: Reading `/proc/[pid]/stat` for processes owned by other users may be restricted by file permissions.

**Process reparenting**: If a parent process exits before its children, the kernel automatically reparents those children to PID 1 (systemd on modern systems). Subsequent `getppid()` calls will return 1.

**Containerized environments**: Within containers, PID 1 is typically the container init process (often `dumb-init` or the application itself), not the host’s systemd. `getppid()` will return the actual parent within the container namespace.

**Performance**: `getppid()` is a system call and adds minimal overhead. Reading from `/proc` involves disk I/O and is slower for bulk queries across many processes.

For simple cases where you need the current process’s parent, `getppid()` is the right choice. For querying multiple processes or integrating with system monitoring, consider eBPF or `/proc` parsing approaches.
