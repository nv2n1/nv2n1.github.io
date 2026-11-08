---
title: "Debugging Bash Scripts: Essential Techniques"
date: 2018-03-24 11:52:47 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-debug-a-bash-script/
---

Bash has several native flags that help you trace and validate script execution before and during runtime.

**Trace mode (-x):** Executes the script while printing each command before it runs.

``` bash
bash -x script.sh
```

This prints expanded commands to stderr, showing variable substitution and command execution order. You can enable tracing for specific sections using `set -x` and `set +x` within the script:

``` bash
#!/bin/bash

echo "Starting process"
set -x
dangerous_command "$variable"
set +x
echo "Done"
```

**Syntax check (-n):** Parses the script for syntax errors without executing it.

``` bash
bash -n script.sh
```

This catches missing quotes, unmatched brackets, and other parse-time errors. Combine it with `-x` for both checking and debugging:

``` bash
bash -xn script.sh
```

**Verbose mode (-v):** Prints each line as it’s read, before expansion.

``` bash
bash -v script.sh
```

Use this when `-x` output is too verbose—it shows the raw script lines instead of expanded commands.

## Static Analysis with ShellCheck

Before running scripts, use ShellCheck to catch common mistakes statically:

``` bash
shellcheck script.sh
```

It flags issues like unquoted variables, unreachable code, incorrect conditionals, and POSIX compliance problems. Install it via your package manager:

``` bash
# Debian/Ubuntu
sudo apt install shellcheck

# RHEL/Fedora
sudo dnf install shellcheck

# macOS
brew install shellcheck
```

Integrate it into your editor (VS Code, Vim, Emacs all have plugins) or CI pipeline to catch issues before they reach production.

## Interactive Debugging with bashdb

For complex scripts requiring breakpoints and variable inspection, bashdb provides a GDB-like debugger:

``` bash
bashdb script.sh
```

Common bashdb commands:

    break <line>          # Set breakpoint at line number
    continue              # Resume execution
    next                  # Step to next line
    step                  # Step into function calls
    print <variable>      # Display variable value
    list                  # Show source code around current line
    quit                  # Exit debugger

Install bashdb:

``` bash
# Most distributions
sudo apt install bashdb

# Or from source
git clone https://sourceforge.net/projects/bashdb/
```

## Practical Debugging Workflow

1.  **Run syntax check first:** `bash -n script.sh`
2.  **Use ShellCheck:** `shellcheck script.sh`
3.  **Trace execution for specific sections:** Add `set -x` and `set +x` around suspicious code
4.  **Use full trace for end-to-end debugging:** `bash -x script.sh 2>&1 | tee debug.log`
5.  **Set `PS4` for clearer trace output:**

``` bash
export PS4='[${BASH_SOURCE}:${LINENO}] '
bash -x script.sh
```

This adds the filename and line number to each traced command, making logs much more readable.

## Debugging Arrays and Complex Variables

Arrays don’t expand nicely with `-x`. Use explicit debugging statements:

``` bash
declare -a myarray=("one" "two" "three")

# Print entire array
echo "Array: ${myarray[@]}"

# Print with indices
for i in "${!myarray[@]}"; do
  echo "[$i]=${myarray[$i]}"
done
```

## Redirecting Trace Output

By default, `-x` writes to stderr. Separate debug output from normal output:

``` bash
bash -x script.sh 2>debug.log
bash -x script.sh 2>&1 | grep -E '^\+' | head -20
```

The latter filters for just the trace lines (prefixed with `+` by default).

Combining these approaches—static checks, targeted tracing, and interactive debugging—covers most debugging scenarios without needing external tools beyond ShellCheck.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Debugging Bash Scripts: Essential Techniques with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Debugging Bash Scripts: Essential Techniques. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
