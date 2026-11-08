---
title: "x86-64 Instruction Encoding: From Assembly to Machine Code"
date: 2017-09-09 05:29:08 +0000
modified: 2026-04-11 16:21:10 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /beginners-guide-x86-64-instruction-encoding/
---

Before encoding instructions, you need to understand the two assembly syntaxes you’ll encounter—they differ fundamentally in operand order and addressing format.

**Intel syntax** (Intel/AMD manuals):

- Operand order: destination, source
- Memory addressing: `[base+offset]`
- Example: `add r8, [rdi+0xa]`

**AT&T syntax** (GNU toolchains on Linux):

- Operand order: source, destination
- Memory addressing: `offset(%base)`
- Example: `addq 0xa(%rdi), %r8`

For most instructions, this reversal is consistent. Some multi-operand instructions (like `enter`) maintain the same logical order regardless of syntax.

## x86-64 Instruction Encoding Basics

x86-64 instructions encode as a variable-length byte sequence. Each instruction can contain:

- **Opcode** — the operation itself, often requiring a REX prefix in 64-bit mode
- **REX prefix** (optional) — extends register and operand width for 64-bit operations
- **ModR/M byte** — specifies registers and addressing modes
- **SIB byte** (optional) — scale-index-base byte for complex addressing
- **Displacement** (optional) — offset for memory operands
- **Immediate** (optional) — constant operand value

### REX Prefix Format

The REX prefix has the format `0100WRXB` (a single byte starting with bits `0100`):

- **W** — promotes operation to 64-bit width (1) or keeps 32-bit (0)
- **R** — extends the ModR/M `reg` field to access registers r8–r15
- **X** — extends the SIB `index` field to access r8–r15
- **B** — extends the ModR/M `r/m` field to access r8–r15

A REX prefix is required whenever you use r8–r15, or when you need 64-bit operand size on certain instructions.

### ModR/M Byte Format

The ModR/M byte breaks down as `[mod][reg][r/m]` (8 bits total):

- **mod (2 bits)** — addressing mode:
  - `00` — indirect addressing (e.g., `[rax]`)
  - `01` — indirect with 8-bit displacement (e.g., `[rax+offset]`)
  - `10` — indirect with 32-bit displacement
  - `11` — register direct
- **reg (3 bits)** — register operand (extended by REX.R)
- **r/m (3 bits)** — register or memory operand (extended by REX.B)

### SIB Byte Format (When Needed)

The SIB byte is `[scale][index][base]` and only appears when mod ≠ `11` and ModR/M.r/m = `100` (with mod = `11`, r/m `100` is simply the RSP register):

- **scale (2 bits)** — `00`=1x, `01`=2x, `10`=4x, `11`=8x
- **index (3 bits)** — index register (extended by REX.X)
- **base (3 bits)** — base register (extended by REX.B)

## Practical Tools: as and objdump

The fastest way to check instruction encodings is with `as` (GNU assembler) and `objdump`.

Create `test.s`:

``` asm
.text
    addq $10, %rax
    add %r8, %r9
    add 0xa(%rdi), %r8
```

Assemble and disassemble:

``` bash
$ as test.s -o test.o
$ objdump -d test.o
```

Output (AT&T syntax):

    test.o:     file format elf64-x86-64

    Disassembly of section .text:

    0000000000000000 <.text>:
       0:   48 83 c0 0a             add    $0xa,%rax
       4:   4d 01 c1                add    %r8,%r9
       7:   4c 03 47 0a             add    0xa(%rdi),%r8

For Intel syntax output:

``` bash
$ objdump -d -M intel test.o
```

    0000000000000000 <.text>:
       0:   48 83 c0 0a             add    rax,0xa
       4:   4d 01 c1                add    r9,r8
       7:   4c 03 47 0a             add    r8,QWORD PTR [rdi+0xa]

## Manual Decoding Example: ADD r8, [rdi+0xa]

Let’s decode the bytes `4c 03 47 0a` from the third instruction above.

**Step 1: Parse the REX prefix**

`4c` in binary is `0100 1100`:

- Bits 7-4: `0100` — this is a REX prefix
- W=1 — 64-bit operation
- R=1 — register field uses high bit (accessing r8–r15)
- X=0 — SIB index field not extended
- B=0 — r/m field accesses rax–rdi

**Step 2: Parse the opcode**

`03` is the opcode for `ADD r64, r/m64` (the “add r/m64 to r64” form from the ISA manual).

**Step 3: Parse the ModR/M byte**

`47` in binary is `0100 0111`:

- mod=`01` — indirect with 8-bit displacement
- reg=`000` — register 0 (combined with REX.R=1, this becomes register 8, i.e., r8)
- r/m=`111` — register 7 (rdi, since REX.B=0)

**Step 4: Parse the displacement**

`0a` is the 8-bit displacement (10 in decimal).

**Result:** The instruction adds the qword at [rdi+0xa] to r8. In AT&T syntax: `add 0xa(%rdi), %r8`. In Intel syntax: `add r8, [rdi+0xa]`.

## General-Purpose Register Encoding

Registers encode as 3-bit values in ModR/M and SIB bytes, with REX extension bits providing the 4th bit for r8–r15:

| Code | RAX–RDI (0–7) | R8–R15 (8–15) |
|------|---------------|---------------|
| 000  | RAX           | R8            |
| 001  | RCX           | R9            |
| 010  | RDX           | R10           |
| 011  | RBX           | R11           |
| 100  | RSP           | R12           |
| 101  | RBP           | R13           |
| 110  | RSI           | R14           |
| 111  | RDI           | R15           |

When using r8–r15, you encode the low 3 bits in ModR/M (or SIB) and set the corresponding REX bit (R, X, or B).

## Another Example: ADD r9, r8

Bytes: `4d 01 c1`

- `4d` — REX.W=1, REX.R=1 (extends the reg field for r8, the source), REX.B=1 (extends the r/m field for r9, the destination)
- `01` — ADD r/m64, r64 opcode (note: source is in reg field, destination in r/m)
- `c1` — mod=`11` (register mode), reg=`000` (r8 with REX.R=1), r/m=`001` (r9 with REX.B=1)

In AT&T syntax: `add %r8, %r9` (source first, destination second).

## SIB Encoding Example: ADD r8, [rax+rcx*4]

Assembly (AT&T syntax), adding the memory operand to r8:

``` asm
add (%rax,%rcx,4), %r8
```

Bytes: `4c 03 04 88`

- `4c` — REX.W=1, REX.R=1 (r8 in the reg field, the destination)
- `03` — ADD r64, r/m64 opcode
- `04` — mod=`00` (no displacement), reg=`000` (r8), r/m=`100` (SIB follows)
- `88` — SIB byte: scale=`10` (4x), index=`001` (rcx), base=`000` (rax)

With a displacement, mod changes and the displacement bytes follow the SIB. For `add 8(%rdi,%rsi,2), %r8`:

Bytes: `4c 03 44 77 08`

- `4c` — REX.W=1, REX.R=1
- `03` — ADD r64, r/m64 opcode
- `44` — mod=`01` (8-bit displacement), reg=`000` (r8), r/m=`100` (SIB)
- `77` — SIB: scale=`01` (2x), index=`110` (rsi), base=`111` (rdi)
- `08` — 8-bit displacement (8)

Note that GNU `as` prefers the opcode `01` form (ADD r/m64, r64, destination in r/m) when the memory operand is the destination, so `add %r8, (%rax,%rcx,4)` assembles to `4c 01 04 88` instead.

## Verifying the Encodings in C

The encodings above can be checked at runtime: copy the instruction bytes into
executable memory, call them like tiny functions, and compare the results. The
program below verifies every byte sequence used in this guide (and shows that
`4c 01 c1`, the wrong REX byte from an earlier version of this post, targets
`%rcx` and leaves `%r9` untouched).

``` c
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

typedef uint64_t u64;

static unsigned char *code;

/* Copy the instruction bytes into executable memory and append RET
 * (0xC3) so the snippet works as a tiny function. */
static void load(const unsigned char *b, size_t n) {
    if (!code)
        code = mmap(NULL, 4096, PROT_READ | PROT_WRITE | PROT_EXEC,
                    MAP_PRIVATE | MAP_ANON, -1, 0);
    memcpy(code, b, n);
    code[n] = 0xC3;
    __builtin___clear_cache((char *)code, (char *)code + n + 1);
}

static int fails;

static void report(const char *what, const unsigned char *b, size_t n,
                   u64 got, u64 want) {
    size_t i;
    printf("%-42s bytes: ", what);
    for (i = 0; i < n; i++)
        printf("%02x ", b[i]);
    printf("-> %llu  [%s]\n", (unsigned long long)got, got == want ? "PASS" : "FAIL");
    fails += got != want;
}

#define CLOBBERS "rax", "rcx", "rdx", "rsi", "rdi", \
                "r8", "r9", "r10", "r11", "cc", "memory"

int main(void) {
    u64 out;

    /* 4d 01 c1  (ADD r9, r8): r9 = r9 + r8 = 12 + 30 */
    {
        static const unsigned char b[] = {0x4d, 0x01, 0xc1};
        u64 a = 30, c = 12;
        load(b, sizeof b);
        asm volatile("movq %1, %%r8\n\tmovq %2, %%r9\n\tcall *%3\n\tmovq %%r9, %0"
                     : "=r"(out) : "r"(a), "r"(c), "r"(code) : CLOBBERS);
        report("add %r8, %r9        (12 + 30)", b, sizeof b, out, 42);
    }

    /* 4c 01 c1  (the bytes the guide first showed): ADD rcx, r8.
     * r9 must be untouched, proving these bytes target rcx, not r9. */
    {
        static const unsigned char b[] = {0x4c, 0x01, 0xc1};
        u64 a = 30, c = 12;
        load(b, sizeof b);
        asm volatile("movq %1, %%r8\n\tmovq %2, %%r9\n\tcall *%3\n\tmovq %%r9, %0"
                     : "=r"(out) : "r"(a), "r"(c), "r"(code) : CLOBBERS);
        report("add %r8, %rcx       (r9 stays 12)", b, sizeof b, out, 12);
    }

    /* 4c 03 47 0a  (ADD r8, [rdi+0xa]): r8 = 100 + *(u64*)(buf+10) */
    {
        static const unsigned char b[] = {0x4c, 0x03, 0x47, 0x0a};
        unsigned char buf[32];
        memset(buf, 0, sizeof buf);
        *(u64 *)(buf + 10) = 555;
        u64 base = 100;
        load(b, sizeof b);
        asm volatile("movq %1, %%rdi\n\tmovq %2, %%r8\n\tcall *%3\n\tmovq %%r8, %0"
                     : "=r"(out) : "r"(buf), "r"(base), "r"(code) : CLOBBERS);
        report("add 0xa(%rdi), %r8  (100 + 555)", b, sizeof b, out, 655);
    }

    /* 4c 03 04 88  (ADD r8, [rax+rcx*4]): rcx=2 scales to byte offset
     * 2*4=8, so the qword at arr+8, which is arr[1] */
    {
        static const unsigned char b[] = {0x4c, 0x03, 0x04, 0x88};
        u64 arr[8] = {9, 55, 9, 9, 9, 9, 9, 9};
        u64 idx = 2, base = 1000;
        load(b, sizeof b);
        asm volatile("movq %1, %%rax\n\tmovq %2, %%rcx\n\tmovq %3, %%r8\n\t"
                     "call *%4\n\tmovq %%r8, %0"
                     : "=r"(out)
                     : "r"(arr), "r"(idx), "r"(base), "r"(code) : CLOBBERS);
        report("add (%rax,%rcx,4), %r8   (1000 + arr[1])", b, sizeof b, out, 1055);
    }

    /* 4c 03 44 77 08  (ADD r8, [rdi+rsi*2+8]): r8 = 1 + *(u64*)(e+8+3*2) */
    {
        static const unsigned char b[] = {0x4c, 0x03, 0x44, 0x77, 0x08};
        unsigned char e[32];
        memset(e, 0, sizeof e);
        *(u64 *)(e + 8 + 3 * 2) = 999;
        u64 idx = 3, base = 1;
        load(b, sizeof b);
        asm volatile("movq %1, %%rdi\n\tmovq %2, %%rsi\n\tmovq %3, %%r8\n\t"
                     "call *%4\n\tmovq %%r8, %0"
                     : "=r"(out)
                     : "r"(e), "r"(idx), "r"(base), "r"(code) : CLOBBERS);
        report("add 8(%rdi,%rsi,2), %r8  (1 + 999)", b, sizeof b, out, 1000);
    }

    printf(fails ? "%d check(s) FAILED\n" : "all checks passed\n", fails);
    return fails != 0;
}
```

Build and run on an x86-64 Linux/BSD/macOS box:

``` bash
$ cc -Wall -O2 -o verify_encoding verify_encoding.c
$ ./verify_encoding
```

Output:

``` text
add %r8, %r9        (12 + 30)              bytes: 4d 01 c1 -> 42  [PASS]
add %r8, %rcx       (r9 stays 12)          bytes: 4c 01 c1 -> 12  [PASS]
add 0xa(%rdi), %r8  (100 + 555)            bytes: 4c 03 47 0a -> 655  [PASS]
add (%rax,%rcx,4), %r8   (1000 + arr[1])   bytes: 4c 03 04 88 -> 1055  [PASS]
add 8(%rdi,%rsi,2), %r8  (1 + 999)         bytes: 4c 03 44 77 08 -> 1000  [PASS]
all checks passed
```

Each line executes the raw bytes on a real CPU and checks the arithmetic,
including the SIB scale (`rcx=2` with scale 4 reads the qword at byte offset
`2*4=8`, which is `arr[1]`).

## Working with Instruction References

When encoding unfamiliar instructions:

1.  Consult the **Intel 64 and IA-32 Architectures Software Developer’s Manual** (Volume 2A, Chapter 2) or the **AMD64 Architecture Programmer’s Manual**
2.  Look up the opcode form for your operand combination (e.g., “r64, r/m64”)
3.  Determine if a REX prefix is needed (anytime you use r8–r15, or for 64-bit operations)
4.  Encode ModR/M and SIB bytes according to your addressing mode
5.  Append displacement and immediate values in little-endian format
6.  Verify with `objdump` or a disassembler

The process is mechanical once you understand the bit layout. Use tools like `ndisasm` or `capstone` to verify complex encodings, and always test your hand-encoded instructions.
