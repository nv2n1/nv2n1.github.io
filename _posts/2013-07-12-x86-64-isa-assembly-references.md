---
title: "x86-64 Assembly: Essential Reference Guide"
date: 2013-07-12 16:47:46 +0000
layout: post
canonical: https://www.systutorials.com/x86-64-isa-assembly-references/
---

x86-64 (Intel 64, AMD64) is the dominant 64-bit instruction set architecture for consumer and enterprise computing. Whether you’re reverse-engineering binaries, writing performance-critical code, or understanding system internals, a solid grasp of x86-64 assembly is essential.

## Learning Foundations

**CMU’s Introduction to Computer Systems (15-213)** course materials remain the gold standard for foundational machine-level programming. The accompanying x86-64 Machine-Level Programming document supplements Chapter 3 of *Computer Systems: A Programmer’s Perspective* and is still current for practical learning.

If you’re transitioning from 32-bit x86, review calling conventions, register usage, and AT&T vs. Intel syntax differences. Understanding the ABI before writing code saves significant debugging time.

**Interactive resources** like Godbolt (compiler explorer) let you write C/C++ and immediately see the generated x86-64 assembly. This is invaluable for learning how modern compilers optimize code and understanding why certain patterns compile to specific instructions.

## Official ISA References

### Intel

The **Intel 64 and IA-32 Architectures Software Developer Manuals** (freely available as PDFs) are the canonical reference. They span multiple volumes:

- **Volume 1**: Basic architecture and instruction set fundamentals
- **Volume 2**: Instruction set reference (alphabetically organized by mnemonic)
- **Volume 3**: System programming (protected mode, paging, interrupts, segmentation)
- **Volume 4**: Model-specific registers (MSRs) and performance monitoring

These manuals are thousands of pages long. Bookmark specific sections and use the PDF search function liberally rather than attempting cover-to-cover reading.

### AMD

The **AMD64 Architecture Programmer’s Manual** covers Ryzen, EPYC, and Opteron processors. AMD’s documentation often includes clearer explanations of microarchitectural details than Intel’s, making it worth consulting alongside Intel’s manuals when optimizing code.

## Performance and Optimization

Understanding instruction latencies and throughput is critical for performance-sensitive code.

**Intel’s Optimization Reference Manual** and **AMD’s Software Optimization Guide** detail:

- Instruction latencies and throughputs across different processor generations
- Execution unit limitations and pipeline behavior
- Memory hierarchy characteristics and cache line sizes
- Microoperation breakdowns for complex instructions
- Stall conditions and common performance pitfalls

**Agner Fog’s CPU instruction timing tables** consolidate latency and throughput data across Intel and AMD processors, including branch prediction behavior. These tables are more concise than vendor manuals for quick lookups.

## System-Level Specifications

### Calling Conventions and ABIs

The **System V AMD64 ABI** specification defines calling conventions, register usage, stack layout, and ELF binary format for x86-64 Unix-like systems. Essential when writing assembly that interoperates with C/C++.

On Windows, the **Microsoft x64 calling convention** differs significantly—different register preservation rules, parameter passing mechanism, and shadow space on the stack. Always verify your target platform’s ABI before writing assembly.

Key differences to remember:

- **System V (Linux/BSD)**: First 6 integer arguments in `rdi, rsi, rdx, rcx, r8, r9`; caller cleans stack
- **Microsoft x64 (Windows)**: First 4 arguments in `rcx, rdx, r8, r9`; 32 bytes of shadow space required; callee cleans stack

## Assemblers and Tools

**GAS (GNU Assembler)** uses AT&T syntax and is standard on Unix-like systems. The manual is thorough but can be cryptic for beginners.

**NASM** (Netwide Assembler) uses Intel syntax, which many find more readable. NASM is portable and widely used in security research and bootloader development.

**Disassemblers and debuggers**:

- `objdump -d` — quick binary disassembly
- `lldb` / `gdb` — instruction-level stepping and register inspection
- **Ghidra** — advanced static analysis and decompilation
- **Radare2** — scriptable reverse engineering framework

## Practical Workflow

1.  **Write small C functions** and compile with `gcc -S` or use Godbolt to see generated assembly
2.  **Compare your hand-written assembly** against compiler output to understand optimization patterns
3.  **Use `objdump -d -M intel`** to disassemble with Intel syntax (easier to read than AT&T)
4.  **Step through with gdb**: set breakpoints, inspect registers with `info registers`, and step with `si`
5.  **Keep references open**: Intel Volume 2 for instruction definitions, your target ABI spec for calling conventions

## Essential References at a Glance

- **Intel Software Developer Manuals**: <a href="https://www.intel.com/content/www/en/en/developer/articles/technical/intel-sdm.html" rel="nofollow noopener" target="_blank">https://www.intel.com/content/www/en/en/developer/articles/technical/intel-sdm.html</a>
- **AMD64 Programmer’s Manual**: <a href="https://www.amd.com/en/technologies/specifications/processor-instructions" rel="nofollow noopener" target="_blank">https://www.amd.com/en/technologies/specifications/processor-instructions</a>
- **System V AMD64 ABI**: <a href="https://refspecs.linuxbase.org/elf/x86_64-abi-0.99.pdf" rel="nofollow noopener" target="_blank">https://refspecs.linuxbase.org/elf/x86_64-abi-0.99.pdf</a>
- **Agner Fog’s optimization guides**: <a href="https://www.agner.org/optimize/" rel="nofollow noopener" target="_blank">https://www.agner.org/optimize/</a>
- **Godbolt**: <a href="https://godbolt.org/" rel="nofollow noopener" target="_blank">https://godbolt.org/</a>
- *Computer Systems: A Programmer’s Perspective* (CS:APP) — comprehensive textbook with assembly throughout

When you hit a performance wall or need clarification on instruction behavior, the official manuals are your authority. Agner Fog’s tables and optimization guides are faster for quick lookups. Godbolt is your best tool for understanding how C compiles to assembly and building intuition.
