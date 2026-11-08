---
title: "GCC Inline Assembly on Linux: Extended Syntax and Examples"
date: 2013-07-12 16:47:46 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/inline-assembly-with-gcc-on-linux/
---

GCC allows you to embed assembly code directly in C/C++ programs through inline assembly (`asm` and `__asm__`). This is useful when you need fine-grained control over processor execution—forcing variables into specific registers, reading CPU state efficiently, or hand-optimizing critical sections verified by profiling.

## Basic Syntax

GCC uses AT&T syntax by default on x86/x86-64. The simplest form is:

``` c
asm("assembly code here");
```

For meaningful control over how the compiler allocates registers and handles operands, use extended inline assembly:

``` c
asm("instruction" : output_operands : input_operands : clobber_list);
```

The colons separate four sections:

1.  **Assembly instructions** — what code to emit
2.  **Output operands** — variables modified by the assembly
3.  **Input operands** — variables read by the assembly
4.  **Clobber list** — registers or flags the assembly modifies that aren’t explicit outputs

## Simple Example

Here’s a basic example that adds two numbers in assembly:

``` c
#include <stdio.h>

int main() {
    int a = 5, b = 3, result;

    asm("addl %2, %0"
        : "=r" (result)
        : "0" (a), "r" (b));

    printf("Result: %d\n", result);
    return 0;
}
```

Breaking this down:

- `"addl %2, %0"` — AT&T syntax: add `%2` (b) into `%0` (result)
- `"=r" (result)` — output operand: result lives in a register, `=` means write-only
- `"0" (a)` — input operand: a uses the same register as output operand 0
- `"r" (b)` — input operand: b in any general-purpose register

## Operand Constraints

The constraint letter specifies where a variable can live:

| Constraint   | Meaning                                         |
|--------------|-------------------------------------------------|
| `r`          | Any general-purpose register                    |
| `a, b, c, d` | Specific registers: rax, rbx, rcx, rdx (x86-64) |
| `m`          | Memory location                                 |
| `i`          | Immediate constant value                        |
| `x`          | XMM register (SSE)                              |
| `y`          | MMX register                                    |

Output modifiers:

- `=` — write-only (output)
- `+` — read-write (input and output)
- `&` — early-clobber (modified before inputs are read)

## Clobber List

If your assembly modifies registers beyond those declared as outputs, list them in the clobber section:

``` c
asm("movq $0x1234, %%rax"
    : 
    : 
    : "rax");
```

Use `"cc"` to indicate the instruction modifies condition flags:

``` c
asm("addq %1, %0"
    : "+r" (x)
    : "r" (y)
    : "cc");
```

Use `"memory"` if the assembly reads or writes arbitrary memory (forces a memory barrier):

``` c
asm volatile("mfence" : : : "memory");
```

## x86-64 Considerations

On x86-64, registers are 64-bit. Key differences from 32-bit:

- Use `movq` instead of `movl` (quad vs long word)
- Registers: `%rax, %rbx, %rcx, %rdx, %rsi, %rdi, %r8–%r15`
- System V AMD64 ABI passes first 6 integer arguments in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`

**Escaping percent signs**: Inside asm strings, use `%%` to emit a literal `%`:

``` c
asm("movq %%rax, %%rbx" : : : "rbx");
```

This produces the instruction `movq %rax, %rbx` in the final assembly.

## Volatile Modifier

Use `volatile` to prevent the compiler from optimizing away the assembly:

``` c
asm volatile("nop");
asm volatile("cli" : : : "memory");  // Disable interrupts
```

Without `volatile`, GCC may remove or reorder instructions it believes have no side effects.

## Intel Syntax Alternative

While AT&T is standard on Linux, you can switch to Intel syntax inline:

``` c
asm(".intel_syntax noprefix\n\t"
    "mov rax, rbx\n\t"
    ".att_syntax prefix");
```

However, AT&T remains the default and is more portable across GCC toolchains.

## Practical Examples

**Reading the carry flag:**

``` c
unsigned char read_carry_flag() {
    unsigned char cf = 0;
    asm("setc %0" : "=r" (cf));
    return cf;
}
```

**Atomic increment** (though prefer `<stdatomic.h>` or C++ `<atomic>`):

``` c
void atomic_increment(int *ptr) {
    asm volatile("lock incl %0" : "+m" (*ptr));
}
```

**CPUID instruction:**

``` c
void cpuid(int code, int *a, int *b, int *c, int *d) {
    asm volatile("cpuid"
                 : "=a" (*a), "=b" (*b), "=c" (*c), "=d" (*d)
                 : "a" (code)
                 : "memory");
}
```

**Reading a Model-Specific Register (MSR) — kernel context:**

``` c
unsigned long read_msr(unsigned int msr) {
    unsigned int low, high;
    asm volatile("rdmsr"
                 : "=a" (low), "=d" (high)
                 : "c" (msr));
    return ((unsigned long)high << 32) | low;
}
```

**Memory barrier:**

``` c
static inline void memory_barrier() {
    asm volatile("" : : : "memory");
}
```

## Compiling and Verification

``` bash
gcc -O2 -o inline_test inline_test.c
objdump -d inline_test | grep -A 20 "<main>"
```

Use `objdump` to disassemble and verify the generated code matches expectations. Check that register allocations are sensible and the compiler didn’t move your assembly unexpectedly.

For verbose compilation output:

``` bash
gcc -O2 -S inline_test.c  # Generates inline_test.s
cat inline_test.s | grep -A 30 "main:"
```

## When to Avoid Inline Assembly

- **Portability**: Code ties itself to specific architectures and compilers
- **Maintainability**: Developers must understand both C and assembly
- **Optimization**: Modern compilers routinely beat hand-written code; profile first
- **Standards**: Use `<stdatomic.h>` for atomics and compiler intrinsics (`<immintrin.h>`, `<arm_neon.h>`) for SIMD instead
- **Kernel interfaces**: For system calls, use libc wrappers; for kernel drivers, use inline assembly only when absolutely necessary

## References

- <a href="https://gcc.gnu.org/onlinedocs/gcc/Using-Inline-Assembly-with-C.html" rel="nofollow noopener" target="_blank">GCC Inline Assembly Documentation</a>
- <a href="https://en.cppreference.com/w/c/language/asm" rel="nofollow noopener" target="_blank">cppreference: Inline assembly</a>
- <a href="https://refspecs.linuxbase.org/elf/x86_64-abi-0.99.pdf" rel="nofollow noopener" target="_blank">x86-64 System V ABI</a>

Reserve inline assembly for low-level system work, performance-critical paths where profiling proved assembly necessary, or when interfacing directly with hardware or kernel code. Always validate generated assembly matches your intent.
