---
title: "Converting Strings to Long Integers in C"
date: 2018-03-24 08:08:16 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/c-converting-string-to-long/
---

Converting strings to long integers is fundamental in C. The standard library provides `strtol()`, `strtoul()`, `strtoll()`, and `strtoull()` for this purpose. These functions handle the conversion robustly and let you detect parsing errors through their return value and `endptr` argument.

## Function Signatures

All four functions share a similar interface:

``` c
long strtol(const char *str, char **endptr, int base);
unsigned long strtoul(const char *str, char **endptr, int base);
long long strtoll(const char *str, char **endptr, int base);
unsigned long long strtoull(const char *str, char **endptr, int base);
```

**Parameters:**

- `str`: The string to convert
- `endptr`: A pointer to a char pointer that receives the address of the first character that couldn’t be converted (or `str` if no conversion occurred). Pass `NULL` if you don’t need this information.
- `base`: The number system base (2-36). Use `0` to auto-detect (8 for octal if prefixed with `0`, 16 for hex if prefixed with `0x`/`0X`, otherwise 10).

## Basic Usage with strtol

``` c
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main() {
    char str[] = "12345";
    char *endptr;
    long num = strtol(str, &endptr, 10);

    if (*endptr != '\0') {
        printf("Unconverted portion: %s\n", endptr);
    }
    printf("Converted value: %ld\n", num);
    return 0;
}
```

## Error Handling

The functions set `errno` on overflow/underflow. Always check for this:

``` c
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <limits.h>

int main() {
    char str[] = "99999999999999999999999999";
    char *endptr;

    errno = 0;
    long num = strtol(str, &endptr, 10);

    if (errno == ERANGE) {
        if (num == LONG_MAX) {
            printf("String overflowed: clamped to LONG_MAX\n");
        } else if (num == LONG_MIN) {
            printf("String underflowed: clamped to LONG_MIN\n");
        }
    }

    if (*endptr != '\0') {
        printf("Invalid character at position: %s\n", endptr);
    }

    return 0;
}
```

## Unsigned Variants

Use `strtoul()` for unsigned long or `strtoull()` for unsigned long long:

``` c
unsigned long ul = strtoul("18446744073709551615", NULL, 10);
unsigned long long ull = strtoull("18446744073709551615", NULL, 10);
```

## Long Long Integers

For values beyond the `long` range, use `strtoll()` or `strtoull()`:

``` c
char str[] = "9223372036854775807";  // LLONG_MAX
char *endptr;
long long num = strtoll(str, &endptr, 10);
```

## Base Detection

Set `base` to `0` for automatic detection:

``` c
strtol("0x1F", NULL, 0);   // Returns 31 (hex)
strtol("077", NULL, 0);    // Returns 63 (octal)
strtol("99", NULL, 0);     // Returns 99 (decimal)
```

## Detecting Failed Conversions

``` c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int parse_long(const char *str, long *result, int base) {
    char *endptr;
    errno = 0;

    *result = strtol(str, &endptr, base);

    // Check for range error
    if (errno == ERANGE) {
        return -1;  // Overflow/underflow
    }

    // Check for invalid characters
    if (endptr == str || *endptr != '\0') {
        return -1;  // No conversion or trailing garbage
    }

    return 0;  // Success
}

int main() {
    long val;
    if (parse_long("12345", &val, 10) == 0) {
        printf("Success: %ld\n", val);
    } else {
        printf("Parse failed\n");
    }
    return 0;
}
```

## Whitespace and Sign Handling

The functions skip leading whitespace and handle optional `+` or `-` signs:

``` c
strtol("  -1234", NULL, 10);   // Returns -1234
strtol("\t+999", NULL, 10);    // Returns 999
```

## Key Points

- Always check `errno` after calling these functions if overflow/underflow is possible
- Use `endptr` to detect invalid characters or incomplete conversions
- Prefer `strtol()` and `strtoll()` over deprecated alternatives like `atol()`
- When using `base = 0`, be aware that leading zeros trigger octal parsing
- These functions are thread-safe in modern implementations
