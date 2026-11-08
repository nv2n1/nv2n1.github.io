---
title: "How GCC Inlines Recursive Functions at -O3"
date: 2020-04-05 13:45:50 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /gcc-may-save-you-some-recursive-functions-calls-an-analysis-of-a-function-call-stack-length-example/
---

GCC applies sophisticated optimizations to recursive functions, and recursive inlining is one of the most dramatic. When the compiler can’t use simple tail-call optimization—because a function has side effects like `printf` that reference stack parameters—it often unrolls multiple recursion iterations into a single function body. Understanding this behavior matters for performance tuning, debugging, and predicting stack usage.

## The Problem: Why Tail-Call Optimization Fails

Tail-call optimization normally converts a recursive call into a jump, reusing the same stack frame. But when a recursive function takes the address of its parameters (like `printf("stack: %p\n", (void*)&recursion_times)`), each call needs its own stack location. The compiler can’t reuse frames, so recursion inlining becomes the fallback optimization strategy.

## Test Case: Observing Stack Behavior Across Optimization Levels

Here’s a simple program that shows stack allocation patterns:

``` c
#include <stdio.h>

void RecursiveFunction(int recursion_times)
{
  printf("stack: %p\n", (void*)&recursion_times);

  if (recursion_times <= 1) return;

  return RecursiveFunction(--recursion_times);
}

int main(int argc, char* argv[])
{
  RecursiveFunction(4);
  return 0;
}
```

Build and test across optimization levels:

``` bash
#!/bin/bash

set -o errexit

for opt in 0 1 2 s 3 ; do
  echo "Building with -O$opt"
  gcc -fno-stack-protector -O$opt prog.c -o prog.$opt
  ./prog.$opt
  objdump -d ./prog.$opt > prog.$opt.asm
  echo "Done with -O$opt"
done
```

The `-fno-stack-protector` flag removes stack canaries, making assembly easier to read. Run this on a modern Linux system with GCC 11 or later.

### Results: -O0 to -O2 (Predictable Behavior)

    Building with -O0
    stack: 0x7fff3690668c
    stack: 0x7fff3690666c
    stack: 0x7fff3690664c
    stack: 0x7fff3690662c

Stack addresses decrease consistently by `0x20` bytes per call—one frame per recursion level. The assembly for -O0 is straightforward:

``` asm
000000000000064a <RecursiveFunction>:
  64a:   55                      push   %rbp
  64b:   48 89 e5                mov    %rsp,%rbp
  64e:   48 83 ec 10             sub    $0x10,%rsp
  652:   89 7d fc                mov    %edi,-0x4(%rbp)
  655:   48 8d 45 fc             lea    -0x4(%rbp),%rax
  659:   48 89 c6                mov    %rax,%rsi
  65c:   48 8d 3d d1 00 00 00    lea    0xd1(%rip),%rdi
  663:   b8 00 00 00 00          mov    $0x0,%eax
  668:   e8 b3 fe ff ff          callq  520 <printf@plt>
  66d:   8b 45 fc                mov    -0x4(%rbp),%eax
  670:   83 f8 01                cmp    $0x1,%eax
  673:   7e 15                   jle    68a <RecursiveFunction+0x40>
  675:   8b 45 fc                mov    -0x4(%rbp),%eax
  678:   83 e8 01                sub    $0x1,%eax
  67b:   89 45 fc                mov    %eax,-0x4(%rbp)
  67e:   8b 45 fc                mov    -0x4(%rbp),%eax
  681:   89 c7                   mov    %eax,%edi
  683:   e8 c2 ff ff ff          callq  64a <RecursiveFunction>
  688:   eb 01                   jmp    68b <RecursiveFunction+0x41>
  68a:   90                      nop
  68b:   c9                      leaveq
  68c:   c3                      retq
```

Each call allocates `0x20` bytes: `0x8` for the saved RBP, `0x10` for locals, and `0x8` pushed by the `callq` instruction. `-O1` and `-O2` follow the same pattern—multiple frames, one per recursion level.

### Results: -O3 (Recursive Inlining)

    Building with -O3
    stack: 0x7ffd414fb53c
    stack: 0x7ffd414fb54c
    stack: 0x7ffd414fb50c
    stack: 0x7ffd414fb51c

Addresses now grow and shrink unpredictably. The assembly reveals the secret:

``` asm
0000000000000690 <RecursiveFunction>:
  690:   48 83 ec 28             sub    $0x28,%rsp
  694:   48 8d 35 e9 00 00 00    lea    0xe9(%rip),%rsi
  69b:   31 c0                   xor    %eax,%eax
  69d:   48 8d 54 24 0c          lea    0xc(%rsp),%rdx
  6a2:   89 7c 24 0c             mov    %edi,0xc(%rsp)
  6a6:   bf 01 00 00 00          mov    $0x1,%edi
  6ab:   e8 90 fe ff ff          callq  540 <__printf_chk@plt>
  6b0:   8b 44 24 0c             mov    0xc(%rsp),%eax
  6b4:   83 f8 01                cmp    $0x1,%eax
  6b7:   7f 07                   jg     6c0 <RecursiveFunction+0x30>
  6b9:   48 83 c4 28             add    $0x28,%rsp
  6bd:   c3                      retq
  6be:   66 90                   xchg   %ax,%ax
  6c0:   83 e8 01                sub    $0x1,%eax
  6c3:   48 8d 54 24 1c          lea    0x1c(%rsp),%rdx
  6c8:   48 8d 35 b5 00 00 00    lea    0xb5(%rip),%rsi
  6cf:   89 44 24 0c             mov    %eax,0xc(%rsp)
  6d3:   89 44 24 1c             mov    %eax,0x1c(%rsp)
  6d7:   bf 01 00 00 00          mov    $0x1,%edi
  6dc:   31 c0                   xor    %eax,%eax
  6de:   e8 5d fe ff ff          callq  540 <__printf_chk@plt>
  6e3:   8b 7c 24 1c             mov    0x1c(%rsp),%edi
  6e7:   83 ff 01                cmp    $0x1,%edi
  6ea:   7e cd                   jle    6b9 <RecursiveFunction+0x29>
  6ec:   83 ef 01                sub    $0x1,%edi
  6ef:   89 7c 24 1c             mov    0x1c(%rsp),%rsp
  6f3:   e8 98 ff ff ff          callq  690 <RecursiveFunction>
  6f8:   eb bf                   jmp    6b9 <RecursiveFunction+0x29>
```

Notice `__printf_chk` is called twice within this single function instance. GCC has unrolled two iterations of the recursion loop into one function body. The first `recursion_times` is stored at `0xc(%rsp)`, the second at `0x1c(%rsp)` (0x10 bytes apart). Only after handling both unrolled iterations does it call `RecursiveFunction` again.

Key optimizations here:

- **No frame pointer**: RBP is eliminated; only RSP-relative addressing is used
- **Direct printf call**: `__printf_chk` is called directly instead of through the PLT
- **Iteration unrolling**: Two loop iterations merged into one function body, reducing function call overhead significantly

## Controlling Recursive Inlining with GCC Parameters

GCC provides tuneable parameters that control when and how aggressively recursive inlining occurs. These are controlled via the `--param` flag:

**Main parameters:**

- `max-inline-insns-recursive`: Maximum instruction count for recursive inlined copies (default: 450)
- `max-inline-insns-recursive-auto`: Limit for non-inline functions at -O3+ (default: 450)
- `max-inline-recursive-depth`: Maximum recursion depth to inline (default: 8)
- `min-inline-recursive-probability`: Only inline if recursion probability exceeds this threshold as a percentage (default: 10)

### Disable Recursive Inlining

To keep recursion predictable for debugging:

``` bash
gcc -O3 -fno-inline-functions prog.c -o prog
```

This prevents inlining entirely while keeping other -O3 optimizations.

### Inline More Aggressively

To merge three iterations instead of two:

``` bash
gcc -O3 --param min-inline-recursive-probability=5 prog.c -o prog
```

With `min-inline-recursive-probability=5`, the compiler becomes more willing to inline, resulting in three `__printf_chk` calls and three separate storage locations within a single function instance:

    stack: 0x7ffdfa315a7c
    stack: 0x7ffdfa315a88
    stack: 0x7ffdfa315a8c
    stack: 0x7ffdfa315a4c
    stack: 0x7ffdfa315a58
    stack: 0x7ffdfa315a5c
    stack: 0x7ffdfa315a1c
    stack: 0x7ffdfa315a28
    stack: 0x7ffdfa315a2c
    stack: 0x7ffdfa3159ec

To reduce inlining depth further:

``` bash
gcc -O3 --param max-inline-recursive-depth=2 prog.c -o prog
```

This limits the compiler to only two levels of recursion before stopping the unrolling.

## Practical Implications and Trade-offs

Recursive inlining exchanges code size for reduced function call overhead. For deep recursion, the benefit is substantial—each call eliminated saves register setup, argument marshaling, and return instruction cycles.

However, there are real downsides:

**Larger binary size**: Unrolled code increases `.text` section size. For embedded systems or code-size-critical scenarios (bootloaders, firmware), this can be unacceptable.

**Instruction cache pressure**: More code in a single function can degrade cache locality, potentially offsetting the call overhead savings.

**Debugging confusion**: GDB stack traces may show fewer frame levels than expected. Variable addresses appear at unexpected offsets relative to RSP instead of RBP.

**Stack depth unpredictability**: While inlining reduces the number of `call`/`ret` instructions, each unrolled iteration still consumes stack space for its local variables. For very deep recursion, this can interact poorly with stack size limits.

**Profiler artifacts**: Recursive inlining can confuse sampling profilers that rely on return addresses on the stack.

## Using the `noinline` Attribute

If your recursive function has complex side effects, interacts with profiling tools, or needs predictable stack behavior, use the `noinline` attribute:

``` c
__attribute__((noinline))
void RecursiveFunction(int recursion_times)
{
  printf("stack: %p\n", (void*)&recursion_times);
  if (recursion_times <= 1) return;
  return RecursiveFunction(--recursion_times);
}
```

This prevents GCC from unrolling the function regardless of optimization level. You retain predictable, debuggable behavior at the cost of losing the performance benefit.

Combine with `__attribute__((noreturn))` if the function doesn’t return normally:

``` c
__attribute__((noinline, noreturn))
void RecursiveFunction(int recursion_times) { ... }
```

This prevents inlining while also helping the compiler eliminate dead code after the call.

## When to Leave Inlining Enabled

Keep recursive inlining enabled (don’t use `noinline`) when:

- Recursion depth is shallow but frequent (parsing, tree traversal with small heights)
- Performance is critical and code size is not constrained
- The function has no complex interactions with profilers or debuggers
- You’ve tested and verified the stack usage is within limits

Use `-O2` instead of `-O3` during development if you need cleaner stack traces for debugging without completely disabling inlining.
