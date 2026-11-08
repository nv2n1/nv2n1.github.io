---
title: "Code alignment matters more than code size for performance"
date: 2018-03-24 07:56:40 +0000
author: "Q A"
layout: post
categories: [system-administration-cloud]
canonical: /large-but-correctly-aligned-and-optimized-code-is-faster-than-less-bytes-per-instruction-opcode-packed-code/
---

The conventional wisdom that smaller code is always better has been thoroughly invalidated on modern processors. A statement from kernel development circles captured this well: for performance-critical paths like interrupt handlers, large-but-correctly-aligned-and-optimized code consistently outperforms byte-packed alternatives.

Consider this comparison:

``` asm
mov eax, [foo]
add eax, 1
mov [foo], eax
```

versus:

``` asm
inc [foo]
```

The three-instruction sequence is faster on contemporary CPUs, despite being larger. This counterintuitive result stems from how modern processors actually execute code.

## Why Alignment and Decoded Instruction Cache Matter

Modern x86-64 CPUs don’t execute raw bytes—they execute decoded micro-operations (µops). The instruction decoder itself is a bottleneck. When instructions are misaligned or tightly packed, the decoder must work harder:

- **Instruction boundaries become ambiguous**: The decoder must track where one instruction ends and the next begins, consuming decode cycles
- **Decoded µop cache misses increase**: CPUs like recent Intel and AMD designs cache decoded instructions. Poor alignment reduces hit rates
- **Front-end stalls occur**: When the decoder can’t keep up, the pipeline stalls waiting for the next batch of µops

The `inc [foo]` instruction, while shorter, requires a memory read-modify-write cycle with additional complexity. The three-instruction sequence allows the CPU to:

- Fetch `mov eax, [foo]` cleanly
- Process `add eax, 1` as a simple ALU operation
- Write back with `mov [foo], eax`

## Alignment in Practice

Proper alignment means:

- **Function entry points**: Align to 16 bytes for modern CPUs (some benefit from 32-byte alignment)
- **Loop headers**: Align hot loops to 16-byte boundaries
- **Branch targets**: Align jump destinations when possible

Use compiler flags to enforce this:

``` bash
gcc -O3 -falign-functions=16 -falign-loops=16 code.c
clang -O3 -falign-functions=16 -falign-loops=16 code.c
```

## Instruction Selection and Front-End Throughput

The three-instruction sequence wins because:

- Each instruction decodes independently without stalling the decoder
- The CPU can execute them in parallel through superscalar execution
- Register pressure is lighter (data flows through `eax`)
- Memory dependencies are explicit and easier for the CPU to predict

The `inc [foo]` variant creates a memory dependency that serializes execution and forces the decoder to handle a more complex instruction form.

## Real-World Impact: Interrupt Handlers

Interrupt handlers exemplify where this matters. They run in privileged mode where:

- Cache hierarchies may be less predictable
- Context switches are expensive
- Latency is critical
- Code paths must be optimized for common cases

An interrupt handler saving registers might use:

``` asm
mov [rsp - 8], rax      ; align store
mov [rsp - 16], rcx     ; separate instructions
mov [rsp - 24], rdx
```

Rather than attempting to pack these into fewer bytes, explicit alignment ensures the front-end never stalls.

## Modern Compiler Behavior

Modern compilers (GCC 11+, Clang 13+) generally understand these principles and will:

- Avoid `inc [mem]` and `dec [mem]` forms in favor of load-modify-store
- Maintain alignment automatically with `-O3`
- Use profile-guided optimization (PGO) to align hot paths

Hand-written assembly should follow the same logic. Benchmarking with `perf` will confirm:

``` bash
perf stat -e cycles,instructions,stalled-cycles-frontend ./your_binary
```

If stalled-cycles-frontend is high relative to total cycles, you likely have front-end pressure from misalignment or dense packing.

## The Bottom Line

On processors from the last decade onward, code density is rarely the limiting factor. The instruction decoder and µop cache are far more constrained than instruction bandwidth. Larger, well-aligned code that respects instruction boundaries outperforms shorter, tightly-packed alternatives in real workloads.

This principle applies beyond interrupts: it matters for any latency-sensitive code path where front-end efficiency determines throughput. When optimizing, measure with `perf`, profile with hardware counters, and don’t assume smaller is faster.
