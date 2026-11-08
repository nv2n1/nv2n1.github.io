---
title: "How to Detect If stderr Is Redirected in Bash"
date: 2018-03-24 11:54:37 +0000
layout: post
canonical: https://www.systutorials.com/how-to-judge-whether-its-stderr-is-redirected-to-a-file-in-a-bash-script-on-linux/
---

You need to detect whether STDERR (file descriptor 2) is connected to a terminal or redirected to a file or pipe. This is useful for conditional logging, color output, or error handling that depends on the output destination.

## Using file descriptor tests

The primary method is the `-t` test operator, which checks if a file descriptor is associated with a terminal (TTY):

``` bash
if [[ -t 2 ]]; then
    echo "STDERR is connected to a terminal"
else
    echo "STDERR is redirected"
fi
```

The `-t` operator takes a file descriptor number as its argument:

- `-t 0` checks stdin
- `-t 1` checks stdout
- `-t 2` checks stderr

## Practical example with conditional logging

A common use case is disabling colored output when STDERR is redirected to a file:

``` bash
#!/bin/bash

if [[ -t 2 ]]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    NC='\033[0m'  # No Color
else
    RED=''
    GREEN=''
    NC=''
fi

error_msg() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

success_msg() {
    echo -e "${GREEN}[OK]${NC} $1" >&2
}

error_msg "Something went wrong"
success_msg "Operation completed"
```

Run this with different redirections to see the behavior:

``` bash
./script.sh                    # Colors enabled
./script.sh 2>/dev/null        # STDERR redirected, colors disabled
./script.sh 2>&1 | tee log.txt # Piped, colors disabled
```

## Checking all output streams

For more comprehensive handling, check multiple file descriptors:

``` bash
if [[ -t 1 ]]; then
    echo "stdout is a terminal"
fi

if [[ -t 2 ]]; then
    echo "stderr is a terminal"
fi

if [[ -t 0 ]]; then
    echo "stdin is a terminal (interactive)"
fi
```

## Detecting pipes specifically

If you need to distinguish between a file and a pipe, use `stat`:

``` bash
# Check if FD 2 is a regular file
if [[ -f /proc/self/fd/2 ]]; then
    echo "STDERR is redirected to a file"
elif [[ -p /proc/self/fd/2 ]]; then
    echo "STDERR is piped"
elif [[ -t 2 ]]; then
    echo "STDERR is a terminal"
fi
```

This approach reads `/proc/self/fd/2`, which contains symlinks to the actual file descriptors. The `-f` test checks for regular files, and `-p` checks for pipes (named pipes/FIFOs).

## Practical application in error handling

Here’s a complete example that adapts behavior based on STDERR redirection:

``` bash
#!/bin/bash

setup_logging() {
    if [[ -t 2 ]]; then
        # Interactive: use colors and immediate output
        LOG_FUNC=log_terminal
    else
        # Redirected: plain text only
        LOG_FUNC=log_file
    fi
}

log_terminal() {
    local level="$1"
    shift
    case "$level" in
        ERROR)   echo -e "\033[0;31m[ERROR]\033[0m $*" >&2 ;;
        WARN)    echo -e "\033[0;33m[WARN]\033[0m $*" >&2 ;;
        INFO)    echo -e "\033[0;32m[INFO]\033[0m $*" >&2 ;;
    esac
}

log_file() {
    local level="$1"
    shift
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [$level] $*" >&2
}

log() {
    $LOG_FUNC "$@"
}

setup_logging

log ERROR "Database connection failed"
log WARN "Retrying operation"
log INFO "Operation succeeded"
```

Test it:

``` bash
./script.sh                           # Colored output
./script.sh 2>error.log               # Timestamped plain text
```

## Important notes

- The `-t` test is POSIX-compliant and works across all UNIX-like systems
- File descriptor 2 specifically refers to STDERR; don’t confuse with 1 (stdout)
- When both stdout and stderr are redirected together (`2>&1`), both the `-t 1` and `-t 2` tests will fail
- This approach works in subshells and functions too
- The `/proc/self/fd` approach is Linux-specific; use `-t` for portability
