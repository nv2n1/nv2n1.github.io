---
title: "Printing to stderr and stdout in Go"
date: 2018-03-24 11:52:57 +0000
modified: 2026-04-12 17:00:07 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-print-a-line-to-stderr-and-stdout-in-go/
---

Go provides straightforward ways to write to standard output and standard error streams. Understanding when and how to use each is essential for building robust applications, especially in containerized and cloud environments where log separation matters.

## Using the fmt Package

The `fmt` package is the most common approach for printing to STDOUT:

``` go
package main

import "fmt"

func main() {
    fmt.Println("This goes to STDOUT")
    fmt.Printf("Formatted output: %v\n", 42)
}
```

For STDERR, use `fmt.Fprintln()` with `os.Stderr`:

``` go
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Fprintln(os.Stderr, "This goes to STDERR")
    fmt.Fprintf(os.Stderr, "Error with code: %d\n", 1)
}
```

The `Fprintln` and `Fprintf` functions accept an `io.Writer` as the first argument, allowing you to direct output to any writer—including files, network connections, or buffers.

## Using the log Package

For applications requiring structured logging, the `log` package writes to STDERR by default:

``` go
package main

import (
    "log"
)

func main() {
    log.Println("This message goes to STDERR")
    log.Printf("Request ID: %s\n", "abc123")
}
```

Create a custom logger for STDOUT if needed:

``` go
package main

import (
    "log"
    "os"
)

func main() {
    stdoutLog := log.New(os.Stdout, "[INFO] ", log.LstdFlags)
    stderrLog := log.New(os.Stderr, "[ERROR] ", log.LstdFlags)

    stdoutLog.Println("Normal operation")
    stderrLog.Println("Something went wrong")
}
```

## Using os.Stdout and os.Stderr Directly

For low-level control, write directly to the file descriptors:

``` go
package main

import (
    "os"
)

func main() {
    os.Stdout.WriteString("Direct output\n")
    os.Stderr.WriteString("Direct error\n")
}
```

This approach is useful when you need to bypass the buffering or formatting of higher-level packages.

## Practical Example: Error Handling

Here’s a real-world pattern that separates informational and error output:

``` go
package main

import (
    "flag"
    "fmt"
    "os"
)

func processFile(filename string) error {
    file, err := os.Open(filename)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Failed to open %s: %v\n", filename, err)
        return err
    }
    defer file.Close()

    fmt.Fprintf(os.Stdout, "Successfully opened %s\n", filename)
    return nil
}

func main() {
    flag.Parse()

    for _, filename := range flag.Args() {
        if err := processFile(filename); err != nil {
            os.Exit(1)
        }
    }
}
```

When running this in a shell, you can capture each stream separately:

``` bash
./program file1.txt file2.txt 2> errors.log 1> output.log
./program file1.txt 2>&1  # Merge both streams
./program file1.txt 2>/dev/null  # Suppress errors
```

## Best Practices

**Use STDOUT for normal operation output** — data your application intentionally produces that users or downstream processes need. In container environments, this flows to standard logging systems (Docker logs, Kubernetes logs, journald).

**Use STDERR for diagnostics and errors** — warnings, errors, debug information, and status messages that don’t belong in application output. Separating these streams allows operators to filter or handle them differently.

**Avoid mixing concerns** — don’t write error messages to STDOUT. This breaks log parsing and makes it harder for monitoring systems to distinguish problems from normal operation.

**Consider structured logging** — for production applications, use packages like `slog` (Go 1.21+) or third-party libraries like `zap` or `logrus`. They support JSON output, structured fields, and log levels, which are critical in cloud and containerized deployments:

``` go
package main

import "log/slog"

func main() {
    slog.Info("Application started", "version", "1.0.0")
    slog.Error("Database connection failed", "error", "timeout", "retry_count", 3)
}
```

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Printing to stderr and stdout in Go with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Printing to stderr and stdout in Go. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
