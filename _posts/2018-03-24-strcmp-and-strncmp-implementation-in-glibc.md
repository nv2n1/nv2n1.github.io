---
title: "glibc\u2019s strcmp and strncmp: Implementation Details"
date: 2018-03-24 08:13:44 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /strcmp-and-strncmp-implementation-in-glibc/
---

The `strcmp()` and `strncmp()` functions are fundamental string comparison utilities in the C standard library. Understanding their implementations reveals important aspects of character comparison, null-termination handling, and performance optimization.

## strcmp Implementation

The glibc implementation of `strcmp()` performs lexicographic comparison of two null-terminated strings, returning:

- A negative value if the first string is lexicographically less than the second
- Zero if the strings are equal
- A positive value if the first string is lexicographically greater than the second

``` c
#include <string.h>

#undef strcmp

int
strcmp(const char *p1, const char *p2)
{
  register const unsigned char *s1 = (const unsigned char *) p1;
  register const unsigned char *s2 = (const unsigned char *) p2;
  unsigned char c1, c2;

  do
    {
      c1 = (unsigned char) *s1++;
      c2 = (unsigned char) *s2++;
      if (c1 == '\0')
        return c1 - c2;
    }
  while (c1 == c2);

  return c1 - c2;
}

libc_hidden_builtin_def (strcmp)
```

Key points in this implementation:

- **Unsigned char casting**: Both pointers are cast to `unsigned char*` to ensure proper comparison semantics across different architectures, avoiding sign-extension issues with high-bit characters.
- **Null-termination check**: The loop exits when it encounters a null byte (`\0`), which marks the end of both strings.
- **Early termination**: If characters don’t match, the function returns immediately with the difference.
- **Return value**: The difference `c1 - c2` provides the required ordering semantics.

## strncmp Implementation

The `strncmp()` function extends `strcmp()` by limiting comparison to the first `n` characters. Modern glibc implementations use loop unrolling to improve performance:

``` c
#include <string.h>

#undef strncmp

#ifndef STRNCMP
#define STRNCMP strncmp
#endif

int
STRNCMP(const char *s1, const char *s2, size_t n)
{
  unsigned char c1 = '\0';
  unsigned char c2 = '\0';

  if (n >= 4)
    {
      size_t n4 = n >> 2;
      do
      {
        c1 = (unsigned char) *s1++;
        c2 = (unsigned char) *s2++;
        if (c1 == '\0' || c1 != c2)
          return c1 - c2;
        c1 = (unsigned char) *s1++;
        c2 = (unsigned char) *s2++;
        if (c1 == '\0' || c1 != c2)
          return c1 - c2;
        c1 = (unsigned char) *s1++;
        c2 = (unsigned char) *s2++;
        if (c1 == '\0' || c1 != c2)
          return c1 - c2;
        c1 = (unsigned char) *s1++;
        c2 = (unsigned char) *s2++;
        if (c1 == '\0' || c1 != c2)
          return c1 - c2;
      } while (--n4 > 0);
      n &= 3;
    }

  while (n > 0)
    {
      c1 = (unsigned char) *s1++;
      c2 = (unsigned char) *s2++;
      if (c1 == '\0' || c1 != c2)
        return c1 - c2;
      n--;
    }

  return c1 - c2;
}

libc_hidden_builtin_def (STRNCMP)
```

Key optimizations in `strncmp()`:

- **Loop unrolling**: When `n >= 4`, the function processes characters in blocks of 4, reducing the number of loop iterations and conditional checks.
- **Bit shift optimization**: `n >> 2` divides by 4 more efficiently than division.
- **Remainder handling**: After the unrolled loop, the final 0-3 characters are processed in a standard loop.
- **Early exit on mismatch or null**: Like `strcmp()`, it returns immediately when characters differ or a null terminator is encountered, even if `n` characters haven’t been compared yet.

## BSD Implementation Comparison

For reference, the BSD implementation of `strcmp()` is more compact:

``` c
int
strcmp(const char *s1, const char *s2)
{
  while (*s1 == *s2++)
    if (*s1++ == 0)
      return (0);
  return (*(const unsigned char *)s1 - *(const unsigned char *)(s2 - 1));
}
```

The BSD `strncmp()` is similarly minimal:

``` c
int
strncmp(const char *s1, const char *s2, size_t n)
{
  if (n == 0)
    return (0);
  do {
    if (*s1 != *s2++)
      return (*(const unsigned char *)s1 -
              *(const unsigned char *)(s2 - 1));
    if (*s1++ == 0)
      break;
  } while (--n != 0);
  return (0);
}
```

The BSD versions prioritize simplicity and code size, while glibc prioritizes performance through loop unrolling and optimized instruction patterns.

## Practical Considerations

When using these functions:

- **Always null-terminate**: Both `strcmp()` and `strncmp()` rely on null termination; buffer overflow protection depends on proper null-termination.
- **Use strncmp for untrusted input**: When comparing fixed-size buffers or data from untrusted sources, prefer `strncmp()` to avoid reading past buffer boundaries.
- **Encoding awareness**: These functions perform byte-by-byte comparison and don’t handle multibyte encodings (UTF-8, etc.) specially. For locale-aware or encoding-aware comparison, use `strcoll()` instead.
- **Performance**: For extremely hot paths, consider alternatives like `memcmp()` with explicit length if you know the strings are bounded, as it may have additional SIMD optimizations.

The glibc implementation represents a pragmatic balance between portability and performance, with architecture-specific variants available on various platforms for even better throughput.
