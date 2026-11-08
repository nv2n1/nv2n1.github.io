---
title: "How to Write Output to STDERR and STDOUT in PHP"
date: 2018-03-24 11:53:02 +0000
modified: 2026-04-12 16:47:25 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-print-a-line-to-stderr-and-stdout-in-php/
---

In PHP, STDOUT and STDERR are standard output streams that handle different types of output. STDOUT carries normal program output, while STDERR carries error messages and diagnostic information. Properly directing output to the correct stream is essential for building reliable scripts and applications.

## Using `fwrite()` with Stream Handles

The most straightforward approach uses `fwrite()` with PHP’s predefined stream constants:

``` php
// Write to STDOUT
fwrite(STDOUT, "This is normal output\n");

// Write to STDERR
fwrite(STDERR, "This is an error message\n");
```

These constants (`STDOUT`, `STDERR`, and `STDIN`) are available in CLI mode and point to the actual file descriptors (1 and 2 respectively on Unix-like systems).

## Using `echo` and `error_log()`

For simpler cases, `echo` writes to STDOUT by default:

``` php
echo "Standard output message\n";
```

For STDERR, use `error_log()`:

``` php
error_log("Error message");
```

Note that `error_log()` writes to the configured error log file (typically specified in `php.ini`), but in CLI scripts it often goes to STDERR. For more direct control, stick with `fwrite(STDERR, ...)`.

## Practical Example: Logging Script Output

Here’s a realistic script that separates normal output from errors:

``` php
<?php

function log_error($message) {
    fwrite(STDERR, "[ERROR] " . date('Y-m-d H:i:s') . " - " . $message . "\n");
}

function log_info($message) {
    fwrite(STDOUT, "[INFO] " . date('Y-m-d H:i:s') . " - " . $message . "\n");
}

// Usage
log_info("Processing file: config.json");

if (!file_exists('config.json')) {
    log_error("Configuration file not found");
    exit(1);
}

log_info("Configuration loaded successfully");
?>
```

When running this script:

- Redirect only errors: `php script.php 2>/dev/null`
- Redirect only output: `php script.php 2>&1 >/dev/null`
- Capture both separately: `php script.php > output.log 2> errors.log`

## Handling in Web SAPI

Note that `STDOUT` and `STDERR` constants are unavailable in the Apache/PHP-FPM web SAPIs. In web contexts, use `error_log()` for diagnostic information instead:

``` php
error_log("Debug information", 0); // Send to configured error handler
```

Check your `php.ini` to verify where `error_log` output is directed (typically `/var/log/php-fpm/error.log` or similar).

## Best Practices

- **Separate concerns**: Use STDERR for errors and diagnostics, STDOUT for data output. This allows users to redirect streams independently.
- **Always terminate messages with newline**: Include `\n` at the end to avoid output buffering issues.
- **Exit codes matter**: Pair error messages with appropriate exit codes (`exit(1)` for failure, `exit(0)` for success).
- **Use structured logging**: Include timestamps and severity levels in error messages.
- **Test locally with Docker**: Verify stream handling works correctly across different environments before deploying.

``` php
<?php
// Complete CLI script example
if ($argc < 2) {
    fwrite(STDERR, "Usage: {$argv[0]} <filename>\n");
    exit(1);
}

$file = $argv[1];

if (!is_readable($file)) {
    fwrite(STDERR, "Error: Cannot read file '$file'\n");
    exit(1);
}

fwrite(STDOUT, "Processing: $file\n");
// Process file...
exit(0);
?>
```

This separation ensures your script integrates well with shell pipelines, log aggregation systems, and monitoring tools that expect proper stream handling.

## 2026 Best Practices and Advanced Techniques

For How to Write Output to STDERR and STDOUT in PHP, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
