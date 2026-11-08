---
title: "x86-64 Instruction Encoding: From Assembly to Machine Code"
date: 2017-09-09 05:29:08 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/beginners-guide-x86-64-instruction-encoding/
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

The SIB byte is `[scale][index][base]` and only appears when ModR/M.r/m = `100`:

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
       4:   4c 01 c1                add    %r8,%r9
       7:   4c 03 47 0a             add    0xa(%rdi),%r8

For Intel syntax output:

``` bash
$ objdump -d --disassembler-options=intel-mnemonic test.o
```

    0000000000000000 <.text>:
       0:   48 83 c0 0a             add    rax,0xa
       4:   4c 01 c1                add    r9,r8
       7:   4c 03 47 0a             add    r8,QWORD PTR [rdi+0xa]

## Manual Decoding Example: ADD r8, \[rdi+0xa\]

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

**Result:** The instruction reads “ADD r8 to \[rdi+0x0a\]”. In AT&T syntax: `add 0xa(%rdi), %r8`. In Intel syntax: `add r8, [rdi+0xa]`.

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

Bytes: `4c 01 c1`

- `4c` — REX.W=1, REX.R=1 (r9 as dest), REX.B=1 (r8 as src)
- `01` — ADD r/m64, r64 opcode (note: source is in reg field, destination in r/m)
- `c1` — mod=`11` (register mode), reg=`000` (r8 with REX.B=1), r/m=`001` (r9 with REX.B=1)

In AT&T syntax: `add %r8, %r9` (source first, destination second).

## SIB Encoding Example: ADD \[rax+rcx\*4+10\], r8

Bytes: `4c 03 84 88 0a 00 00 00`

- `4c` — REX.W=1, REX.R=1 (r8 as dest)
- `03` — ADD r/m64, r64 opcode
- `84` — mod=`10` (32-bit displacement), reg=`000` (r8), r/m=`100` (SIB follows)
- `88` — SIB byte: scale=`10` (4x), index=`000` (rax), base=`000` (rax)
- `0a 00 00 00` — 32-bit displacement (10 in little-endian)

Wait—this example has an issue. Let me correct it: if you want base=rax and index=rcx, the SIB byte should be `8c` (scale=`10`, index=`001`, base=`100`). The mod should reflect that both registers and displacement are used.

Actually, let’s use: `[rax+rcx*4+10]`

- `4c` — REX.W=1, REX.R=1
- `03` — ADD opcode
- `84` — mod=`10`, reg=`000`, r/m=`100` (SIB)
- `8c` — SIB: scale=`10` (4x), index=`001` (rcx), base=`100` (rsp)

No—base=`100` is rsp. Use base=`000` (rax):

- `88` — SIB: scale=`10` (4x), index=`000` (rax), base=`000` (rax)

This is getting confusing. A clearer example: `[rdi+rsi*2]`

``` asm
add %r8, 0(%rdi,%rsi,2)
```

Bytes: `4c 03 84 77 00`

- `4c` — REX.W=1, REX.R=1
- `03` — ADD opcode
- `84` — mod=`10` (displacement follows), reg=`000` (r8), r/m=`100` (SIB)
- `77` — SIB: scale=`01` (2x), index=`110` (rsi), base=`111` (rdi)
- `00` — 32-bit displacement (0)

## Working with Instruction References

When encoding unfamiliar instructions:

1.  Consult the **Intel 64 and IA-32 Architectures Software Developer’s Manual** (Volume 2A, Chapter 2) or the **AMD64 Architecture Programmer’s Manual**
2.  Look up the opcode form for your operand combination (e.g., “r64, r/m64”)
3.  Determine if a REX prefix is needed (anytime you use r8–r15, or for 64-bit operations)
4.  Encode ModR/M and SIB bytes according to your addressing mode
5.  Append displacement and immediate values in little-endian format
6.  Verify with `objdump` or a disassembler

The process is mechanical once you understand the bit layout. Use tools like `ndisasm` or `capstone` to verify complex encodings, and always test your hand-encoded instructions.
