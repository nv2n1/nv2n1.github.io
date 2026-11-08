---
title: "Handling Linux Signals in C"
date: 2018-03-24 11:40:55 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-catch-the-kill-signals-sent-by-kill-in-c-on-linux/
---

When a process receives a signal from `kill` or `pkill`, it needs a signal handler to intercept and respond to it. Without one, most signals terminate the process immediately. This guide covers setting up robust signal handlers for production daemons.

## Understanding Signals

The `kill` command sends signals to processes. By default, it sends SIGTERM (signal 15), requesting graceful termination. Common signals include:

- **SIGTERM (15)**: Termination signal — processes should clean up and exit
- **SIGKILL (9)**: Kill signal — cannot be caught or ignored; terminates immediately
- **SIGHUP (1)**: Hangup signal — traditionally signals configuration reload
- **SIGUSR1 (10) and SIGUSR2 (12)**: User-defined signals for custom handling
- **SIGPIPE (13)**: Broken pipe — common in network daemons

Send specific signals with `kill -SIGNAL pid` or `pkill -SIGNAL progname`.

## Basic Signal Handler with sigaction()

Use `sigaction()` instead of the older `signal()` function — it’s more reliable and portable for long-running processes.

``` c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

volatile sig_atomic_t shutdown_requested = 0;

void signal_handler(int sig) {
    if (sig == SIGTERM) {
        fprintf(stderr, "SIGTERM received, initiating graceful shutdown\n");
        shutdown_requested = 1;
    } else if (sig == SIGUSR1) {
        fprintf(stderr, "SIGUSR1 received, reloading configuration\n");
    }
}

int main() {
    struct sigaction sa;

    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = signal_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;  // Restart interrupted system calls

    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGUSR1, &sa, NULL);

    printf("Daemon running with PID %d\n", getpid());

    while (!shutdown_requested) {
        printf("Working...\n");
        sleep(2);
    }

    printf("Cleaning up and exiting\n");
    return 0;
}
```

Compile and test:

``` bash
gcc -o daemon daemon.c
./daemon &
kill -SIGTERM $(pgrep daemon)
# or
pkill -SIGTERM daemon
```

## Why sigaction() Over signal()

The older `signal()` function has platform-specific behavior and unreliable semantics. `sigaction()` provides explicit control:

- **sa_handler**: Function to call when signal arrives
- **sa_mask**: Additional signals to block during handler execution
- **sa_flags**: Behavior flags like `SA_RESTART` to automatically restart interrupted system calls

The `SA_RESTART` flag is critical — it prevents `read()`, `write()`, `select()`, and other blocking calls from failing with `EINTR` when interrupted by signals.

## Handling Multiple Signals Safely

For complex applications, use `sigprocmask()` to block signals during critical sections:

``` c
sigset_t set, oldset;
sigemptyset(&set);
sigaddset(&set, SIGTERM);
sigaddset(&set, SIGUSR1);

// Block signals during critical section
sigprocmask(SIG_BLOCK, &set, &oldset);
// ... critical code that modifies shared state ...
// Restore previous mask
sigprocmask(SIG_SETMASK, &oldset, NULL);
```

This prevents signal handlers from interrupting operations on shared data structures.

## Signal Safety Requirements

Signal handlers execute asynchronously and have strict constraints:

- Keep handlers short and simple
- Only call async-safe functions (see `man 7 signal-safety` for the full list)
- Safe functions include: `write()`, `open()`, `close()`, `signal()`, `sigaction()`
- **Unsafe functions**: `printf()`, `malloc()`, `pthread_mutex_lock()`, most library functions

Use `volatile sig_atomic_t` for variables modified in signal handlers:

``` c
volatile sig_atomic_t signal_count = 0;

void handler(int sig) {
    signal_count++;  // Safe: sig_atomic_t
}
```

## Preventing Crashes on Broken Pipes

Network daemons often crash when clients disconnect unexpectedly. Ignore SIGPIPE:

``` c
signal(SIGPIPE, SIG_IGN);
```

Alternatively, use `MSG_NOSIGNAL` with `send()` on individual socket operations.

## SIGKILL Cannot Be Caught

SIGKILL (9) is special — it cannot be caught, blocked, or ignored. The kernel terminates the process immediately. If graceful shutdown fails, SIGKILL is the last resort:

``` bash
kill -SIGTERM pid      # Request graceful shutdown
sleep 5
kill -SIGKILL pid      # Force termination if needed
```

## systemd Integration

Modern systemd-managed daemons must handle SIGTERM within the timeout period (default 90 seconds). systemd sends SIGTERM, waits, then sends SIGKILL if necessary. Ensure your daemon:

1.  Registers SIGTERM handler
2.  Stops accepting new work
3.  Completes in-flight operations
4.  Exits cleanly

``` c
sigaction(SIGTERM, &sa, NULL);  // Always required for systemd services
signal(SIGPIPE, SIG_IGN);        // Prevent network-related crashes
```

## Complete Daemon Example

``` c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <syslog.h>

volatile sig_atomic_t shutdown_requested = 0;
volatile sig_atomic_t reload_requested = 0;

void signal_handler(int sig) {
    switch (sig) {
        case SIGTERM:
        case SIGINT:
            shutdown_requested = 1;
            break;
        case SIGHUP:
            reload_requested = 1;
            break;
    }
}

void reload_config() {
    fprintf(stderr, "Reloading configuration\n");
    reload_requested = 0;
}

int main() {
    struct sigaction sa;

    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = signal_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;

    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGHUP, &sa, NULL);
    signal(SIGPIPE, SIG_IGN);

    printf("Daemon running with PID %d\n", getpid());

    while (!shutdown_requested) {
        if (reload_requested) {
            reload_config();
        }

        printf("Working...\n");
        sleep(2);
    }

    printf("Shutting down gracefully\n");
    return 0;
}
```

Test configuration reload without restarting:

``` bash
./daemon &
kill -SIGHUP $(pgrep daemon)  # Trigger reload
```

## Key Takeaways

- Use `sigaction()` for all signal handling — never `signal()`
- Keep `sa_flags = SA_RESTART` to avoid `EINTR` errors
- Use `volatile sig_atomic_t` for shared state
- Keep handlers minimal; only set flags and exit
- Ignore SIGPIPE in network daemons
- SIGKILL cannot be caught — only SIGTERM matters for graceful shutdown
- systemd expects clean SIGTERM handling within 90 seconds
