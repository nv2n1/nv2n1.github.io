---
title: "Generating Mixed C and Assembly Listings with GCC and objdump"
date: 2013-07-12 16:47:44 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /generate-a-mixed-source-and-assembly-listing-using-gcc/
---

When debugging and optimizing C/C++ programs, you need to see how the compiler translates your source code into assembly. A mixed source and assembly listing lets you trace exactly what machine instructions correspond to each line of your source.

## Using objdump (Recommended Modern Approach)

The most straightforward method is to compile with debugging symbols and use `objdump` to generate mixed listings without recompilation:

``` bash
gcc -g source.c -o binary
objdump -S binary > listing.txt
```

The `-S` flag intermixes source code (from `-g` symbols) with disassembly. For C++ projects, demangle symbols with `-C`:

``` bash
objdump -SC binary > listing.txt
```

To use Intel syntax instead of AT&T (GCC’s default):

``` bash
objdump -S -M intel binary > listing.txt
```

This approach is cleaner than older methods because it separates compilation from listing generation, making it easier to work with existing binaries and avoiding the complexity of passing assembler flags.

## Using GCC’s Assembler Flags (Alternative)

If you need to generate listings during compilation, use the `-Wa,-adhln` flags:

``` bash
gcc -Wa,-adhln -g source.c -o binary > listing.s
```

The assembler flags control output:

- `a`: Enable listings
- `d`: Omit debugging directives (reduces noise)
- `h`: Include high-level source code
- `l`: Include assembly instructions
- `n`: Omit forms processing (no pagination)

The listing goes to stdout; redirect it to a file while the binary is produced at the `-o` location.

## Single-File Example

For a simple program:

``` c
#include <stdio.h>

int main()
{
  printf("Hello world!\n");
  return 0;
}
```

Compile and generate listing:

``` bash
gcc -g helloworld.c -o helloworld
objdump -S helloworld > helloworld.txt
```

The resulting file contains interleaved source and assembly:

        4:helloworld.c  ****   printf("Hello world!\n");
           0000000000001139 <main>:
        1139:   55                      push   %rbp
        113a:   48 89 e5                mov    %rsp,%rbp
        113d:   bf f4 11 00 00          mov    $0x11f4,%edi
        1142:   e8 e9 fe ff ff          call   1030 <puts@plt>

The left columns show the instruction address in hex (1139, 113a), machine bytecode, and mnemonics. Each source line is mapped back to its corresponding instructions.

## Multi-File Projects

For projects with multiple source files, compile all together:

``` bash
gcc -g fun1.c main.c -o binary
objdump -S binary > combined.txt
```

Given these files:

**fun1.c:**

``` c
#include <stdio.h>

void fun1()
{
    printf("Hello world!\n");
}
```

**main.c:**

``` c
#include <stdio.h>

void fun1();

int main()
{
    fun1();
    return 0;
}
```

The combined listing shows each function’s prologue and epilogue (stack frame setup/teardown) aligned with their source lines, making it easy to understand calling conventions and register allocation decisions.

## Comparing Optimization Levels

Assembly output changes dramatically with optimization flags. Generate listings at different levels to understand compiler behavior:

``` bash
gcc -g -O0 source.c -o binary_O0
objdump -S binary_O0 > opt0.txt

gcc -g -O2 source.c -o binary_O2
objdump -S binary_O2 > opt2.txt

gcc -g -O3 source.c -o binary_O3
objdump -S binary_O3 > opt3.txt
```

At `-O0`, you’ll see obvious one-to-one source-to-instruction mapping. At `-O2` and `-O3`, the compiler reorders instructions, eliminates dead code, inlines functions, and restructures loops—sometimes making single source lines compile to dozens of instructions or disappear entirely.

## Filtering Large Outputs

For large projects, listings can reach thousands of lines. Extract specific functions with grep:

``` bash
objdump -S binary | grep -A 50 "<main>:"
```

Or use awk to print lines around a specific function:

``` bash
objdump -S binary | awk '/^[0-9a-f]* <my_function>:/,/^[0-9a-f]* <[^>]*>:/' | head -n 50
```

To extract and save a function’s assembly:

``` bash
objdump -S binary | sed -n '/^[0-9a-f]* <target_function>:/,/^[0-9a-f]* <[^>]*>:/p' > function.asm
```

## Understanding the Output Format

Each non-empty line contains:

- **Instruction address**: Hexadecimal memory address (1139, 113a)
- **Machine code**: Raw bytes the processor executes
- **Mnemonic**: Human-readable instruction name (mov, call, push)
- **Operands**: Registers, memory addresses, or immediate values
- **Source line**: (if available) The corresponding source code line

CFI directives (`.cfi_*`) encode call frame information for stack unwinding. These aren’t executable code but are used by debuggers (GDB, LLDB) and exception handling mechanisms (libunwind) to traverse the stack correctly during debugging or unwinding exceptions.

## Architecture Considerations

Assembly output is architecture-specific. The examples above use x86-64 with AT&T syntax (GCC’s default). On other architectures, instruction names and register conventions differ:

- **ARM**: `ldr`, `str`, `bl` instead of `movl`, `call`
- **ARM64 (AArch64)**: `ldr`, `str`, `bl` with 64-bit registers
- **RISC-V**: `addi`, `sw`, `jal` with different register naming
- **PowerPC**: Different register conventions and instruction formats

Check your target architecture’s instruction set documentation for specific details. Force Intel syntax with:

``` bash
objdump -S -M intel binary > listing.txt
```

## Using gdb for Interactive Analysis

For more control, use GDB directly:

``` bash
gdb ./binary
(gdb) disassemble main
(gdb) disassemble /m main
```

The `/m` flag shows mixed source and assembly interactively. Set breakpoints at specific addresses and step through assembly while viewing source:

``` bash
(gdb) break *0x1139
(gdb) run
(gdb) stepi
```

## Practical Debugging Workflow

Combine mixed listings with a debugger for efficient analysis:

1.  Compile with `-g` and your desired optimization level (`-O0` for clarity, `-O2` for realistic behavior)
2.  Generate the listing with `objdump -S binary > listing.txt`
3.  Search for the function of interest in the listing
4.  Cross-reference addresses with GDB breakpoints
5.  Step through assembly while viewing the source-instruction correlation
6.  Compare behavior at different optimization levels to spot compiler-related issues

Mixed source-assembly listings are invaluable for understanding compiler behavior, optimizing hot code paths, debugging low-level issues, and reverse-engineering binaries where source isn’t available.
