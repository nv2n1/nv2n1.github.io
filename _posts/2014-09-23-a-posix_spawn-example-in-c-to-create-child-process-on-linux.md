---
title: "Safe Process Creation with posix_spawn() in C"
date: 2014-09-23 14:35:38 +0000
modified: 2026-04-11 16:22:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /a-posix_spawn-example-in-c-to-create-child-process-on-linux/
---

The traditional fork-exec pattern works, but it’s error-prone. `posix_spawn()` handles process creation in a single call with several advantages:

- **Atomic operation**: Spawn and exec happen atomically, eliminating race conditions between fork and exec
- **No fork quirks**: You don’t need conditional logic for parent vs. child code paths — exec happens immediately in the child
- **Direct error handling**: Errors from exec are returned as errno values directly to the parent, not buried in exit status
- **Clearer control flow**: One function call beats fork/exec/wait logic and reduces accidental parent code execution in children

Avoid `system()` entirely. It spawns a shell, introduces shell injection vulnerabilities, and hides the actual process ID. `posix_spawn()` gives you direct control without those hazards.

## Basic Example: Running a Command

Here’s a practical example that runs a command via `/bin/sh -c`:

``` c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <spawn.h>
#include <sys/wait.h>
#include <errno.h>

extern char **environ;

void run_cmd(const char *cmd)
{
    pid_t pid;
    char *argv[] = {"sh", "-c", (char *)cmd, NULL};
    int status;

    printf("Running command: %s\n", cmd);

    status = posix_spawn(&pid, "/bin/sh", NULL, NULL, argv, environ);
    if (status != 0) {
        fprintf(stderr, "posix_spawn failed: %s\n", strerror(status));
        return;
    }

    printf("Child PID: %d\n", pid);

    // Wait for child to complete
    if (waitpid(pid, &status, 0) == -1) {
        perror("waitpid");
        return;
    }

    if (WIFEXITED(status)) {
        printf("Child exited with status: %d\n", WEXITSTATUS(status));
    } else if (WIFSIGNALED(status)) {
        printf("Child terminated by signal: %d\n", WTERMSIG(status));
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <command>\n", argv[0]);
        return 1;
    }

    run_cmd(argv[1]);
    return 0;
}
```

Compile and run:

``` bash
gcc -o run run.c
./run "echo 'Hello from child process'"
```

## Using posix_spawnp() for PATH Lookup

When you need the system to search `$PATH` for an executable instead of providing an absolute path, use `posix_spawnp()`:

``` c
void run_cmd_from_path(const char *cmd)
{
    pid_t pid;
    char *argv[] = {"sh", "-c", (char *)cmd, NULL};
    int status;

    // posix_spawnp searches PATH
    status = posix_spawnp(&pid, "sh", NULL, NULL, argv, environ);
    if (status != 0) {
        fprintf(stderr, "posix_spawnp failed: %s\n", strerror(status));
        return;
    }

    if (waitpid(pid, &status, 0) == -1) {
        perror("waitpid");
        return;
    }

    if (WIFEXITED(status)) {
        printf("Child exited with status: %d\n", WEXITSTATUS(status));
    } else if (WIFSIGNALED(status)) {
        printf("Child killed by signal: %d\n", WTERMSIG(status));
    }
}
```

Use the `p` variant when executing user-provided programs or system utilities that may exist in standard locations. For system utilities where you control the path, use `posix_spawn()` with absolute paths instead.

## Redirecting File Descriptors

Use `posix_spawn_file_actions_t` to customize file descriptor handling in the child. For example, redirect stdout and stderr to files:

``` c
#include <spawn.h>
#include <fcntl.h>

void run_cmd_with_redirect(const char *cmd, const char *output_file, const char *error_file)
{
    pid_t pid;
    char *argv[] = {"sh", "-c", (char *)cmd, NULL};
    posix_spawn_file_actions_t file_actions;
    int status;

    // Initialize file actions
    posix_spawn_file_actions_init(&file_actions);

    // Redirect stdout (FD 1) to output_file
    posix_spawn_file_actions_addopen(
        &file_actions, 1, output_file,
        O_WRONLY | O_CREAT | O_TRUNC, 0644
    );

    // Redirect stderr (FD 2) to error_file
    posix_spawn_file_actions_addopen(
        &file_actions, 2, error_file,
        O_WRONLY | O_CREAT | O_TRUNC, 0644
    );

    status = posix_spawn(&pid, "/bin/sh", &file_actions, NULL, argv, environ);

    // Always clean up
    posix_spawn_file_actions_destroy(&file_actions);

    if (status != 0) {
        fprintf(stderr, "posix_spawn failed: %s\n", strerror(status));
        return;
    }

    if (waitpid(pid, &status, 0) == -1) {
        perror("waitpid");
        return;
    }

    if (WIFEXITED(status)) {
        printf("Child exited with status: %d\n", WEXITSTATUS(status));
    }
}
```

File actions are processed in order, so you can chain multiple operations. You can also duplicate file descriptors or close inherited ones:

``` c
// Close a file descriptor
posix_spawn_file_actions_addclose(&file_actions, 3);

// Duplicate FD 3 to 4
posix_spawn_file_actions_adddup2(&file_actions, 3, 4);

// Open multiple files
posix_spawn_file_actions_addopen(&file_actions, 1, "stdout.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
posix_spawn_file_actions_addopen(&file_actions, 2, "stderr.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
```

File actions execute before the exec, so you can safely close inherited file descriptors to prevent them from leaking to the child.

## Configuring Signal Handling and Attributes

Use `posix_spawnattr_t` to control signal handling, process groups, and scheduling in the child process:

``` c
#include <signal.h>

void run_cmd_with_sigmask(const char *cmd)
{
    pid_t pid;
    char *argv[] = {"sh", "-c", (char *)cmd, NULL};
    posix_spawnattr_t attr;
    sigset_t mask;
    int status;

    // Initialize attributes
    posix_spawnattr_init(&attr);

    // Set signal mask for the child
    sigemptyset(&mask);
    sigaddset(&mask, SIGTERM);
    sigaddset(&mask, SIGINT);
    posix_spawnattr_setsigmask(&attr, &mask);

    // Reset SIGTERM and SIGINT to default action instead of inheriting parent's handling
    posix_spawnattr_setsigdefault(&attr, &mask);

    status = posix_spawn(&pid, "/bin/sh", NULL, &attr, argv, environ);
    posix_spawnattr_destroy(&attr);

    if (status != 0) {
        fprintf(stderr, "posix_spawn failed: %s\n", strerror(status));
        return;
    }

    if (waitpid(pid, &status, 0) == -1) {
        perror("waitpid");
        return;
    }
}
```

You can also set process groups with `posix_spawnattr_setpgroup()`, control signal inheritance with `posix_spawnattr_setsigdefault()`, and adjust scheduling priority with `posix_spawnattr_setschedparam()` on systems that support them. Signal masks are inherited from the parent unless explicitly changed.

## Comparing fork()/exec() vs. posix_spawn()

With fork()/exec(), you write conditional logic to separate parent and child paths:

``` c
pid_t pid = fork();
if (pid == 0) {
    // Child code
    execv(path, argv);
    perror("execv");  // Only reached if execv fails
    exit(1);
} else if (pid > 0) {
    // Parent code
    waitpid(pid, &status, 0);
} else {
    perror("fork");
}
```

With `posix_spawn()`, the separation is implicit:

``` c
status = posix_spawn(&pid, path, &file_actions, &attr, argv, environ);
if (status != 0) {
    fprintf(stderr, "posix_spawn failed: %s\n", strerror(status));
    return;
}
// Parent code only — child is already executing
waitpid(pid, &status, 0);
```

This eliminates the risk of accidentally executing parent code in the child and makes control flow much clearer.

## Error Handling and Debugging

`posix_spawn()` returns an errno value directly (not -1 like most system calls):

``` c
int status = posix_spawn(&pid, path, NULL, NULL, argv, environ);
if (status != 0) {
    fprintf(stderr, "Spawn error: %s\n", strerror(status));
    // status is an errno value, not the child's exit code
    return;
}
```

Common errno values include:

- `ENOENT`: executable not found
- `EACCES`: permission denied
- `ENOMEM`: out of memory
- `E2BIG`: argument list too long

Always use the `WIFEXITED()` and `WEXITSTATUS()` macros to safely extract the child’s exit status:

``` c
int child_status;
waitpid(pid, &child_status, 0);

if (WIFEXITED(child_status)) {
    int exit_code = WEXITSTATUS(child_status);
    printf("Child exited with code: %d\n", exit_code);
} else if (WIFSIGNALED(child_status)) {
    int signal = WTERMSIG(child_status);
    printf("Child killed by signal: %d\n", signal);
} else if (WIFSTOPPED(child_status)) {
    int signal = WSTOPSIG(child_status);
    printf("Child stopped by signal: %d\n", signal);
}
```

Don’t confuse the `posix_spawn()` return value with the child’s exit code — they’re completely separate values.

## Practical Considerations

**Custom environment variables**: Avoid passing `environ` directly if you need a custom environment. Build your own environment array instead:

``` c
char *custom_env[] = {
    "PATH=/usr/bin:/bin",
    "HOME=/root",
    "USER=root",
    NULL
};

status = posix_spawn(&pid, "/bin/sh", NULL, NULL, argv, custom_env);
```

**File descriptor cleanup**: Use `posix_spawn_file_actions_addclose()` to close inherited file descriptors before exec. This prevents accidental leaks of pipe ends or sockets.

**Signal inheritance**: Signal masks are inherited from the parent unless explicitly changed with `posix_spawnattr_setsigmask()`. Handlers (like ignoring SIGPIPE) are also inherited, so reset them in the child if needed.

**Choosing the right function**:

- Use `posix_spawn()` with absolute paths for system utilities where you control the location
- Use `posix_spawnp()` for user-provided commands or when searching `$PATH` is required
- Always check return values; spawning can fail for many reasons beyond “command not found”
