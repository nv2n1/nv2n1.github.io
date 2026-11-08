---
title: "x86-64 Floating-Point Comparisons with SSE and AVX"
date: 2018-03-24 11:41:40 +0000
modified: 2026-04-11 16:00:19 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /x86-64-instructions-for-floating-point-comparisons/
---

The x86-64 ISA provides `ucomiss` and `ucomisd` for comparing SSE floating-point values. These instructions compute S1 – S2 and set the EFLAGS register (ZF, PF, CF) based on the result.

| Instruction | Operands | Purpose                                  |
|-------------|----------|------------------------------------------|
| `ucomiss`   | S2, S1   | Compare single-precision (32-bit) floats |
| `ucomisd`   | S2, S1   | Compare double-precision (64-bit) floats |

In AT&T syntax, the source operand is listed second. S1 must be in an XMM register (XMM0–XMM15), while S2 can be in an XMM register or memory.

### Flag Results

After comparison, the EFLAGS are set as follows:

- **ZF=0, CF=0, PF=0**: S1 \> S2
- **ZF=1, CF=0, PF=0**: S1 == S2
- **ZF=0, CF=1, PF=0**: S1 \< S2
- **ZF=1, CF=1, PF=1**: Either operand is NaN (unordered)

### Conditional Branches

Use these conditional jumps after `ucomiss` or `ucomisd`:

- `je` / `jz`: Equal
- `jb` / `jc`: Less than
- `ja`: Greater than
- `jbe`: Less than or equal
- `jae`: Greater than or equal
- `jp`: Unordered (NaN detected)

### Example: Double-Precision Comparison

``` asm
ucomisd %xmm1, %xmm0    # Compare XMM0 - XMM1
je equal_label          # Jump if equal
jb less_label           # Jump if XMM0 < XMM1
ja greater_label        # Jump if XMM0 > XMM1
jp nan_label            # Jump if either is NaN
```

## AVX Variants

Modern systems support AVX-based comparison instructions that work identically to their SSE counterparts but provide better register allocation in complex code:

``` asm
vcomisd %xmm1, %xmm0    # AVX double-precision
vcomiss %xmm1, %xmm0    # AVX single-precision
```

The `v`-prefixed instructions accept the same flag semantics and conditional branches as SSE versions.

## Handling NaN Values

Unordered comparisons—when either operand is NaN—set ZF, PF, and CF all to 1. Always check for NaN in security-sensitive code or when processing untrusted floating-point data:

``` asm
ucomisd %xmm1, %xmm0
jp handle_nan           # Jump if unordered (NaN present)
je handle_equal
jb handle_less
ja handle_greater
```

The `jp` (jump if parity) instruction detects NaN because PF is only set in the unordered case.

## Signaling vs. Quiet Comparisons

The `comiss` and `comisd` instructions behave like `ucomiss` and `ucomisd` respectively, except they signal (raise an exception) on Quiet NaN (QNaN) operands. Use signaling comparisons when you need to detect invalid operations:

``` asm
comisd %xmm1, %xmm0     # Signals on QNaN; unsignaled NaN handling
je equal_label
```

Use `ucomiss`/`ucomisd` when NaN should be silently handled as unordered.

## Masked Comparisons with Predicates

For vectorized operations or when you need specific comparison semantics, `cmpss` and `cmpsd` accept an immediate predicate operand:

``` asm
cmpsd $0, %xmm1, %xmm0  # XMM0 = (XMM0 == XMM1) ? all-bits-1 : 0
cmpsd $1, %xmm1, %xmm0  # XMM0 = (XMM0 < XMM1) ? all-bits-1 : 0
cmpsd $2, %xmm1, %xmm0  # XMM0 = (XMM0 <= XMM1) ? all-bits-1 : 0
```

Common predicates:

- `0`: Equal
- `1`: Less than
- `2`: Less than or equal
- `4`: Not equal
- `5`: Not less than (greater than or equal)
- `6`: Not less than or equal (greater than)

These return a vector mask (all 1s or all 0s per element) instead of setting flags, making them suitable for conditional value selection without branching.

## Practical Example: Min/Max Operations

``` asm
# Compute minimum of XMM0 and XMM1, store in XMM0
ucomisd %xmm1, %xmm0
jbe min_is_xmm0
movsd %xmm1, %xmm0     # XMM1 was smaller
min_is_xmm0:
# XMM0 now contains the minimum
```

Or use `minsd`/`minss` for the same result without explicit branching:

``` asm
minsd %xmm1, %xmm0     # XMM0 = min(XMM0, XMM1)
maxsd %xmm1, %xmm0     # XMM0 = max(XMM0, XMM1)
```
