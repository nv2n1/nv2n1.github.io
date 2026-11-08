---
title: "How to Get the Size of Integers in OCaml"
date: 2018-03-24 08:15:56 +0000
layout: post
canonical: https://www.systutorials.com/length-of-int-in-ocaml/
---

OCaml’s `int` type size depends on your platform’s architecture. On 64-bit systems, `int` is 63 bits; on 32-bit systems, it’s 31 bits. This catches many people off guard when they test bitwise operations.

Here’s why: OCaml uses one bit as a tag to distinguish integers from pointers at runtime (the least significant bit). So on a 64-bit architecture, you get 63 bits for the actual value, not the full 64.

## Checking Your System

You can verify your platform’s int size:

``` ocaml
let int_bits = Sys.int_size;;
```

On 64-bit systems, this returns `63`. On 32-bit systems, it returns `31`.

## The Bit Shift Example

When you run this on a 64-bit machine:

``` ocaml
# (1 lsl 33);;
- : int = 8589934592
```

You’re shifting 1 left by 33 bits, which produces a 34-bit number. This is larger than 2^31, confirming you have more than 31 bits available. The result fits comfortably in a 63-bit signed integer.

If you try this on a 32-bit system, you’d get integer overflow instead.

## Counting Set Bits

Here’s a common approach to count the number of 1-bits in an integer:

``` ocaml
let rec count1s x =
    match (x lsr 1, x land 1) with
    | 0, n -> n
    | y, n -> n + count1s y
```

Testing with `-1` (all bits set):

``` ocaml
# count1s (-1);;
- : int = 63
```

On a 64-bit system, this returns `63` because `-1` has all 63 value bits set to 1. On a 32-bit system, it would return `31`.

For better performance with large integers, use the built-in `Stdlib.Int.popcount` (available in OCaml 4.13+):

``` ocaml
# Int.popcount (-1);;
- : int = 63
```

## Handling Overflow

OCaml integers wrap silently on overflow:

``` ocaml
# let max_int = Int.max_value;;
val max_int : int = 4611686018427387903

# max_int + 1;;
- : int = -4611686018427387904
```

If you need arbitrary-precision arithmetic without overflow, use the `Zarith` library or OCaml’s `Bigint` module.

## Platform-Specific Code

When writing code that depends on integer size, use conditionals:

``` ocaml
if Sys.int_size = 63 then
  (* 64-bit specific logic *)
  ...
else
  (* 32-bit fallback *)
  ...
```

Or check at compile time with `Sys.word_size`, which tells you the word size in bits (typically 32 or 64).

Remember: OCaml’s tagged integer representation is a core part of its garbage collector design. It allows fast discrimination between heap-allocated values and immediate integers, which is why the tagging bit exists.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
