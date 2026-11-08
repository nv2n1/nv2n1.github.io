---
title: "Catching and Handling Signals in C on Linux"
date: 2014-05-29 05:38:14 +0000
modified: 2026-04-11 16:22:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /catching-the-signal-sent-by-kill-in-c-on-linux/
---

Programs need to shut down gracefully—saving state, closing connections, flushing buffers—rather than terminating abruptly. A daemon might receive a termination signal and need to persist in-memory data before exiting. The challenge is catching these signals in C and responding appropriately.

## Signal basics

The `kill` command sends `SIGTERM` by default. This signal is catchable and allows for graceful shutdown.

`kill -9` sends `SIGKILL`, which cannot be caught, blocked, or ignored—the process terminates immediately. `SIGSTOP` also cannot be caught or ignored. Understanding this distinction is critical: you cannot make `SIGKILL` safe. If graceful shutdown is essential, rely on `SIGTERM`.

`Ctrl-C` from the terminal sends `SIGINT`, which is also catchable.

## Using sigaction to catch signals

The `sigaction()` system call is the modern, portable way to install signal handlers. Avoid the older `signal()` function—it has inconsistent behavior across platforms and less control.

### Key rules for signal handlers

**Only call async-signal-safe functions.** These functions won’t corrupt internal state if called during another function’s execution. Safe functions include: `write()`, `exit()`, `_Exit()`, `signal()`, `sigaction()`, `atomic` operations. Unsafe functions: `printf()`, `malloc()`, `pthread_*`, `syslog()`, most library functions.

**Keep handlers short and simple.** Do minimal work in the handler itself—typically just setting a flag.

**Use `sigaction()` with `SA_SIGINFO`** to get additional context about the signal through the `siginfo_t` structure.

**Use `volatile sig_atomic_t`** for flags shared between the handler and main code. This type is atomic and immune to compiler optimizations that would break signal safety.

## Example: catching SIGTERM

``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>

static volatile sig_atomic_t shutdown_requested = 0;

void sig_term_handler(int signum, siginfo_t *info, void *ptr)
{
    shutdown_requested = 1;
    const char msg[] = "SIGTERM received, shutting down gracefully.\n";
    write(STDERR_FILENO, msg, sizeof(msg) - 1);
}

void install_sigterm_handler(void)
{
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));

    sa.sa_sigaction = sig_term_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);

    if (sigaction(SIGTERM, &sa, NULL) == -1) {
        perror("sigaction");
        exit(EXIT_FAILURE);
    }
}

int main(void)
{
    install_sigterm_handler();

    printf("Daemon running (PID: %d). Send SIGTERM to stop.\n", getpid());

    while (!shutdown_requested) {
        sleep(1);
    }

    printf("Graceful shutdown complete.\n");
    return EXIT_SUCCESS;
}
```

Compile and test:

``` bash
gcc -o daemon daemon.c
./daemon &
kill $!
```

The handler sets a flag rather than performing complex work. The main loop checks the flag and exits cleanly. The `volatile sig_atomic_t` is crucial—it guarantees atomic reads and prevents the compiler from caching the value in a register.

## Catching multiple signals

Install handlers for different signals by calling `sigaction()` for each:

``` c
static volatile sig_atomic_t shutdown_requested = 0;
static volatile sig_atomic_t reload_config_requested = 0;

void sig_handler(int signum, siginfo_t *info, void *ptr)
{
    switch (signum) {
        case SIGTERM:
        case SIGINT:
            shutdown_requested = 1;
            break;
        case SIGHUP:
            reload_config_requested = 1;
            break;
    }
}

void install_signal_handlers(void)
{
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));

    sa.sa_sigaction = sig_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);

    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGHUP, &sa, NULL);
}

int main(void)
{
    install_signal_handlers();

    while (!shutdown_requested) {
        if (reload_config_requested) {
            reload_config_requested = 0;
            /* Reload configuration */
        }
        sleep(1);
    }

    return EXIT_SUCCESS;
}
```

## Blocking signals during critical sections

Use `sigprocmask()` to block signals during operations that must not be interrupted:

``` c
sigset_t set, oldset;
sigemptyset(&set);
sigaddset(&set, SIGTERM);
sigaddset(&set, SIGINT);

sigprocmask(SIG_BLOCK, &set, &oldset);
/* Critical section—signals are queued until unblocked */
sigprocmask(SIG_SETMASK, &oldset, NULL);
```

Blocked signals are queued and delivered once unblocked. In multi-threaded programs, use `pthread_sigmask()` instead—it blocks signals per-thread.

## Common signals and their uses

**SIGHUP** (hangup): Often used in daemons for configuration reload without shutdown. Send with `kill -HUP <pid>`.

**SIGUSR1, SIGUSR2**: Application-defined signals available for custom purposes. Use these when you need signals beyond the standard set.

**SIGCHLD**: Sent when a child process exits. Parent processes use this to detect and reap zombie processes. Install a handler if spawning subprocesses.

**SIGSEGV**: Segmentation fault. Can be caught for logging/diagnostics, but recovery is unreliable. Use primarily for cleanup before exit.

**SIGPIPE**: Sent when writing to a closed pipe or socket. Default behavior is to terminate. Daemons often ignore this with `signal(SIGPIPE, SIG_IGN)`.

For the full list and details, see `man 7 signal`.

## Best practices

- Test signal handling with `kill -TERM <pid>` and `kill -INT <pid>` from another terminal.
- Always initialize signal masks with `sigemptyset()` or `sigfillset()` before use.
- Check return values of `sigaction()` and `sigprocmask()`.
- Avoid calling non-async-safe functions in handlers; when in doubt, check `man 7 signal-safety`.
- In multi-threaded programs, dedicate a thread to signal handling with `sigwait()` or `sigwaitinfo()` instead of installing handlers.
- Document which signals your application handles and why.
