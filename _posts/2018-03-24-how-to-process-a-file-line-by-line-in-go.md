---
title: "Processing Files Line by Line in Go"
date: 2018-03-24 11:50:38 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /how-to-process-a-file-line-by-line-in-go/
---

Processing files line by line is a common task in Go. Here are the practical approaches, from simplest to most flexible.

## Using bufio.Scanner

The most straightforward method uses `bufio.Scanner`, which handles line splitting automatically:

``` go
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        fmt.Println(line)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
```

Scanner handles most cases well. By default it splits on newlines, but you can customize the split function if needed.

## Setting Buffer Size

By default, `Scanner` has a 64KB line buffer. For larger lines, increase it:

``` go
scanner := bufio.NewScanner(file)
buf := make([]byte, 0, 64*1024)
scanner.Buffer(buf, 1024*1024) // 1MB max line length
for scanner.Scan() {
    line := scanner.Text()
    // process line
}
```

## Custom Split Function

Process by delimiter other than newlines:

``` go
scanner := bufio.NewScanner(file)
scanner.Split(bufio.ScanWords) // splits on whitespace
for scanner.Scan() {
    word := scanner.Text()
    // process word
}
```

Or define your own split function for comma-separated values or other formats:

``` go
scanner := bufio.NewScanner(file)
scanner.Split(func(data []byte, atEOF bool) (advance int, token []byte, err error) {
    for i := 0; i < len(data); i++ {
        if data[i] == ',' {
            return i + 1, data[:i], nil
        }
    }
    if !atEOF {
        return 0, nil, nil
    }
    return len(data), data, bufio.ErrFinalToken
})
for scanner.Scan() {
    field := scanner.Text()
    // process field
}
```

## Using bufio.Reader

For more control, use `bufio.Reader` directly with `ReadString` or `ReadLine`:

``` go
reader := bufio.NewReader(file)
for {
    line, err := reader.ReadString('\n')
    if err != nil {
        if err == io.EOF {
            break
        }
        log.Fatal(err)
    }
    fmt.Print(line)
}
```

`ReadString` includes the delimiter. Use `strings.TrimSuffix(line, "\n")` to remove it if needed. This approach gives you more granular error handling per line.

## Handling Different Line Endings

Windows files use `\r\n`. `Scanner` handles this automatically, but if using `ReadString`, strip both:

``` go
import "strings"

line = strings.TrimRight(line, "\r\n")
```

## Processing Large Files

For multi-gigabyte files, consider concurrent processing:

``` go
type lineJob struct {
    num  int
    text string
}

scanner := bufio.NewScanner(file)
jobs := make(chan lineJob, 100)
go func() {
    lineNum := 0
    for scanner.Scan() {
        jobs <- lineJob{lineNum, scanner.Text()}
        lineNum++
    }
    close(jobs)
}()

for job := range jobs {
    // process job.text
}
```

## Performance Considerations

- `Scanner` is convenient but slightly slower than `Reader` for very tight loops
- Avoid repeated string allocations; use `scanner.Bytes()` instead of `scanner.Text()` if you don’t need strings
- Pre-allocate buffers when possible
- For CSV/structured data, consider the `encoding/csv` package instead

## Error Handling

Always check `scanner.Err()` after the loop, not just at each iteration. The scanner won’t report errors until after the loop ends:

``` go
for scanner.Scan() {
    // process line
}
if err := scanner.Err(); err != nil {
    log.Fatal(err)
}
```

Most line-by-line processing tasks fit well with `Scanner`. Reach for `Reader` when you need per-line error handling or custom buffering behavior.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Processing Files Line by Line in Go with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Processing Files Line by Line in Go. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
