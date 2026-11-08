---
title: "Sequence Points in C: Understanding Evaluation Order and Side Effects"
date: 2018-03-24 11:44:26 +0000
layout: post
canonical: https://www.systutorials.com/which-are-sequence-points-in-c/
---

A sequence point is a point in execution where all side effects from previous evaluations are guaranteed to be complete and visible. Understanding sequence points is critical for writing correct C code, especially when dealing with expressions that modify variables.

The C standard defines side effects as changes to the state of the execution environment (variable modifications, I/O operations, etc.). Between sequence points, the order in which side effects occur is undefined, which can lead to unpredictable behavior if you’re not careful.

## Where Sequence Points Occur

The C standard guarantees sequence points at these locations:

1.  **End of a full expression** — An expression statement like `x = 5;` or the expression in `if (x > 10)`. Subexpressions within a larger expression do not have sequence points between them.

2.  **Logical operators** — After evaluating the left operand of `&&`, `||`, and the ternary operator `?:`

3.  **Comma operator** — After the left operand of `,`

4.  **Function calls** — After all arguments are evaluated and before the function executes

## The Critical Rule

Between consecutive sequence points, an object’s stored value can be modified at most once by a single expression. Furthermore, if you access a variable’s value between modifications (within the same sequence point), that access must be to determine what value to store—not for some other purpose.

## Examples of Undefined Behavior

These are classic mistakes that violate sequence point rules:

``` c
// Undefined behavior: i is modified twice between sequence points
i = ++i + i++;
```

Here, `++i` modifies `i`, then `i++` modifies it again, and the order is unspecified. The result is unpredictable.

``` c
// Undefined behavior: accessing i for both reading and modification
a[i] = i++;
```

The increment happens, but whether `a[i]` uses the old or new value of `i` is undefined.

``` c
// Undefined behavior: multiple increments without sequence points
printf("%d %d\n", i++, i++);
```

The order in which the two `i++` operations execute is not guaranteed.

## Safe Alternatives

When you need to modify a variable multiple times or use its value, separate operations with sequence points:

``` c
// Safe: separate statements create sequence points
i = i + 1;
i = i + 1;

// Safe: comma operator provides a sequence point
i = ++i, i + 1;  // i incremented, then separate expression

// Safe: use temporary variables
int temp = i++;
a[temp] = i++;
```

## Practical Impact

In modern C code (C99 and later), compilers are often smart enough to warn about these violations if you enable warnings (`-Wall -Wextra`). GCC and Clang will flag obvious cases like `i = ++i + i++`.

However, some violations are subtle and may only manifest on certain architectures or optimization levels. The safest approach is to **never modify a variable and read it in the same statement**. Keep your expressions simple and let the compiler optimize—don’t try to be too clever.

The sequence point rules exist because C compilers have significant freedom in how they schedule operations for performance. Relying on undefined behavior might work on your machine today but fail on another compiler, architecture, or after a compiler upgrade.
