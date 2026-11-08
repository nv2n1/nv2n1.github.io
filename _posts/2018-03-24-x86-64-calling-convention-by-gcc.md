---
title: "GCC x86-64 Calling Conventions Explained"
date: 2018-03-24 08:13:44 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /x86-64-calling-convention-by-gcc/
---

The x86-64 architecture on Linux follows the System V AMD64 ABI calling convention. Understanding this is essential when writing assembly, optimizing code, debugging, or interfacing with C libraries.

## Register usage for arguments

Integer and pointer arguments use these registers in order:

- `RDI` — first argument
- `RSI` — second argument
- `RDX` — third argument
- `RCX` — fourth argument
- `R8` — fifth argument
- `R9` — sixth argument

Floating-point arguments use XMM registers:

- `XMM0` through `XMM7` — floating-point arguments

If a function takes both integer and floating-point arguments, they occupy their respective registers independently. The first integer argument still uses `RDI` even if floating-point arguments are present.

Additional arguments beyond the sixth integer or eighth floating-point argument are passed on the stack, in right-to-left order (the caller pushes them).

## Return values

- `RAX` — return value (also `RDX:RAX` for 128-bit returns)
- `XMM0` and `XMM1` — floating-point return values

## System calls

System calls follow a slightly different convention. The syscall number goes in `RAX`, and arguments use the same registers as normal calls except `R10` is used instead of `RCX` for the fourth argument. This avoids clobbering `RCX`, which the `syscall` instruction uses internally.

## Caller and callee saved registers

- **Caller-saved** (volatile): `RAX`, `RCX`, `RDX`, `RSI`, `RDI`, `R8`, `R9`, `R10`, `R11`, and XMM0-XMM15
- **Callee-saved** (non-volatile): `RBX`, `RSP`, `RBP`, `R12`, `R13`, `R14`, `R15`

The callee must preserve these registers if it uses them. The caller cannot assume them to survive a function call.

## Stack alignment and red zone

The stack must be 16-byte aligned *before* a `call` instruction. Since `call` pushes an 8-byte return address, the stack is 8 bytes misaligned at function entry. Most code compensates by immediately pushing another 8-byte value (like `rbp`) to restore alignment.

The 128 bytes below `RSP` form a “red zone” that is safe from signal handlers. Functions can use this space for temporary data without allocating stack space, though signal handlers will overwrite it.

## Practical example

``` c
#include <stdio.h>

long add_five(long a, long b, long c, long d, long e, long f, long g) {
    return a + b + c + d + e + f + g;
}

int main() {
    long result = add_five(1, 2, 3, 4, 5, 6, 7);
    printf("%ld\n", result);
    return 0;
}
```

In this function:

- `a` through `f` arrive in `RDI`, `RSI`, `RDX`, `RCX`, `R8`, `R9`
- `g` (the seventh argument) is passed on the stack
- The result is returned in `RAX`

Examine the calling convention in practice with `objdump -d` or `gdb` to verify how arguments are passed.

## Variadic functions

Functions with variable arguments (like `printf`) are more complex. They must track how many floating-point arguments were passed in XMM registers via `RAX`. The System V ABI specifies that `RAX` should contain the number of vector registers used for floating-point arguments (0-8). This allows variadic functions to know whether to retrieve arguments from registers or the stack.

## References

- <a href="http://x86-64.org/documentation/abi.pdf" rel="nofollow noopener" target="_blank">System V AMD64 ABI Specification</a>
- <a href="https://www.amd.com/content/dam/amdsite/documents/x86-open64-abi.pdf" rel="nofollow noopener" target="_blank">AMD Developer Documentation</a>

## 2026 Comprehensive Guide: Best Practices

This extended guide covers GCC x86-64 Calling Conventions Explained with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for GCC x86-64 Calling Conventions Explained. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
