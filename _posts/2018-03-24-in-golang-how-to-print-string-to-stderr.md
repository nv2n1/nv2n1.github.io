---
title: "Printing Strings to stderr in Go"
date: 2018-03-24 11:50:41 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /in-golang-how-to-print-string-to-stderr/
---

Sending output to stderr keeps error messages separate from normal program output, making it easier to redirect and filter logs in shell scripts and pipelines.

## Basic Approach with fmt

The simplest method uses `fmt.Fprintln()` with `os.Stderr`:

``` go
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Fprintln(os.Stderr, "This is an error message")
}
```

This writes directly to stderr without any formatting overhead. You can also use `fmt.Fprintf()` for more control:

``` go
fmt.Fprintf(os.Stderr, "Error: %v\n", err)
```

## Using the log Package

For most applications, the `log` package is better than raw `fmt` calls. It automatically includes timestamps and optional caller information:

``` go
package main

import (
    "log"
    "os"
)

func main() {
    logger := log.New(os.Stderr, "ERROR: ", log.LstdFlags|log.Lshortfile)
    logger.Println("Something went wrong")
}
```

The flags control what metadata gets included:

- `log.LstdFlags` adds date and time
- `log.Lshortfile` adds filename and line number
- `log.Ldate`, `log.Ltime`, `log.Lmicroseconds` for finer control

## Structured Logging with slog

For production services, use the `slog` package (available since Go 1.21). It supports structured logging with key-value pairs and multiple output formats:

``` go
package main

import (
    "log/slog"
    "os"
)

func main() {
    logger := slog.New(slog.NewJSONHandler(os.Stderr, nil))
    logger.Error("database connection failed", "host", "db.example.com", "port", 5432)
}
```

Output:

``` json
{"time":"2026-01-15T10:23:45.123Z","level":"ERROR","msg":"database connection failed","host":"db.example.com","port":5432}
```

You can also use `slog.NewTextHandler()` for human-readable output:

``` go
logger := slog.New(slog.NewTextHandler(os.Stderr, &slog.HandlerOptions{
    Level: slog.LevelError,
}))
```

## Redirecting stderr in Shell

Once your Go program writes to stderr, you can handle it in your shell:

``` bash
# Redirect stderr to a file
./myapp 2> errors.log

# Redirect stderr to stdout
./myapp 2>&1

# Discard stderr
./myapp 2>/dev/null

# Separate stdout and stderr to different files
./myapp > output.log 2> errors.log
```

## When to Use Each Approach

- **`fmt.Fprintln(os.Stderr, ...)`**: Quick scripts or one-off tools where you need minimal overhead.
- **`log` package**: Small to medium applications needing basic timestamped output.
- **`slog`**: Production services, microservices, or anything requiring structured logging and log aggregation integration.

The standard library choices cover nearly all use cases. External logging libraries like `logrus` or `zap` exist but add dependencies; evaluate whether their features justify the extra weight for your project.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
