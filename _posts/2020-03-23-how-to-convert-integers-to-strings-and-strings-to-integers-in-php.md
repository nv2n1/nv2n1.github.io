---
title: "Safe Integer and String Conversion in PHP"
date: 2020-03-23 15:51:58 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /how-to-convert-integers-to-strings-and-strings-to-integers-in-php/
---

Type conversion is a constant necessity when handling user input, database results, and API responses in PHP. While PHP’s loose typing offers flexibility, explicit conversion remains essential for security, performance, and code clarity.

## Integer to String Conversion

Several methods convert integers to strings:

**Casting** is the most direct approach:

``` php
$myInt = 42;
$str = (string) $myInt;  // "42"
```

**String interpolation** works implicitly in double-quoted strings:

``` php
$myInt = 42;
$str = "{$myInt}";  // "42"
```

**The strval() function** provides explicit conversion:

``` php
$str = strval(42);  // "42"
```

For performance-critical code, casting is marginally faster than function calls. In PHP 8.0+ with JIT compilation enabled, the difference is negligible for most workloads. If concatenating many values, use the dot operator with cast types rather than relying on interpolation:

``` php
$result = (string) $id . '-' . (string) $timestamp;
```

## String to Integer Conversion

Converting strings to integers requires care, especially with untrusted input.

**Casting** truncates decimal portions and ignores trailing non-numeric characters:

``` php
$str = "123";
$int = (int) $str;  // 123

$str = "123abc";
$int = (int) $str;  // 123 (trailing chars ignored)

$str = "3.14";
$int = (int) $str;  // 3 (truncated, not rounded)
```

**The intval() function** behaves identically to casting but accepts a base parameter for different number systems:

``` php
$int = intval("1010", 2);   // 10 (binary)
$int = intval("FF", 16);    // 255 (hexadecimal)
$int = intval("755", 8);    // 493 (octal)
```

### Edge Cases

Be aware of these behaviors:

``` php
(int) "0xFF";       // 0 (hex prefix ignored without intval)
intval("0xFF", 16); // 255 (requires explicit base parameter)
intval("  456");    // 456 (leading whitespace trimmed)
intval("");         // 0 (empty string)
intval("abc");      // 0 (non-numeric prefix returns 0)
intval("-789");     // -789 (negative values handled correctly)
```

## Strict Types and Modern PHP

PHP 8.0+ supports strict type enforcement via `declare(strict_types=1);` at the top of a file. When enabled, type mismatches throw `TypeError` instead of silently converting:

``` php
<?php
declare(strict_types=1);

function processAmount(int $amount): string {
    return "Amount: $amount";
}

processAmount("500");  // TypeError: must be of type int, string given
processAmount(500);    // Works fine
```

For APIs and services accepting user input, strict types force explicit validation and conversion rather than relying on PHP’s implicit coercion. This eliminates entire categories of injection vulnerabilities.

## Type Juggling Vulnerabilities

PHP’s loose typing can create subtle security holes through type juggling:

``` php
// Without strict types, dangerous comparisons occur
if ((int) $_GET['id'] == 10) {
    // User passes id=10e0 or id=10.0 — both cast to 10
}

// Type juggling comparison issues
"0" == 0;           // true
"0e0" == 0;         // true
"123abc" == 123;    // true
```

With `declare(strict_types=1);`, these comparisons require explicit type matching, eliminating ambiguous coercion.

## Validation Over Blind Conversion

For user input, validation is preferable to blind conversion. The filter extension provides robust validation:

``` php
$input = $_POST['user_id'];

// Validate before converting
if (filter_var($input, FILTER_VALIDATE_INT) === false) {
    throw new InvalidArgumentException('Invalid integer');
}
$userId = (int) $input;
```

For positive integers only, `ctype_digit()` is faster and reliable:

``` php
if (!ctype_digit($input) || $input > PHP_INT_MAX) {
    throw new InvalidArgumentException('Invalid positive integer');
}
$userId = (int) $input;
```

The `filter_var()` approach is more robust—it rejects values that would cast to zero accidentally, like empty strings or non-numeric prefixes:

``` php
filter_var("", FILTER_VALIDATE_INT);      // false
filter_var("abc", FILTER_VALIDATE_INT);   // false
filter_var("123", FILTER_VALIDATE_INT);   // 123
filter_var("-456", FILTER_VALIDATE_INT);  // -456
```

## Performance Considerations

For tight loops or high-throughput code:

- Casting `(int)` and `(string)` are marginally faster than function calls
- Type declarations eliminate runtime coercion overhead
- In PHP 8.0+ with JIT compilation, differences are negligible for most applications

Use type hints in function signatures to enable compiler optimizations:

``` php
function calculateTotal(int $price, int $quantity): int {
    return $price * $quantity;
}

// JIT can aggressively optimize this with explicit types
for ($i = 0; $i < 1000000; $i++) {
    $total = calculateTotal(100, 5);
}
```

The JIT compiler optimizes typed functions more aggressively, but measurable differences appear only in extreme scenarios. Prioritize code clarity and security over micro-optimizations.
