---
title: "Handling Floating Point Math in Bash with bc, awk, and dc"
date: 2013-07-12 16:47:47 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/floating-point-in-bash-shell/
---

Bash has no native floating point support. The `(( ))` and `$(( ))` arithmetic expansions only handle integers. For decimals, you need external tools — primarily `bc`, `awk`, or `dc`.

## bc: Arbitrary Precision Calculator

`bc` is the standard choice for floating point math in shell scripts. It’s POSIX-compliant, available on every Unix-like system, and handles arbitrary precision — critical for financial calculations where rounding errors accumulate.

### Basic Syntax

Run `bc` interactively:

``` bash
$ bc
1.2 + 8.2
9.4
quit
```

The `scale` variable controls decimal places in output. By default, `bc` produces no decimal point:

``` bash
$ echo "2.5 + 3.5" | bc
6
```

Set `scale` explicitly:

``` bash
$ echo "scale=2; 2.5 + 3.5" | bc
6.00
```

### Using bc in Scripts

Pipe expressions to `bc` with the `-q` flag to suppress prompts:

``` bash
#!/bin/bash

result=$(echo "scale=4; 1.2 + 8.2" | bc -q)
echo "Result: $result"
```

Use variables in expressions:

``` bash
#!/bin/bash

num1=15.5
num2=3.2
result=$(echo "scale=3; $num1 * $num2" | bc -q)
echo "$num1 * $num2 = $result"
```

### Arithmetic Operations

Standard operators work as expected:

``` bash
# Addition, subtraction, multiplication, division
echo "scale=2; 10 / 3" | bc -q          # 3.33

# Exponentiation
echo "scale=0; 2 ^ 10" | bc -q          # 1024

# Square root
echo "scale=4; sqrt(16)" | bc -q        # 4.0000

# Absolute value
echo "scale=2; abs(-5.5)" | bc -q       # 5.5
```

### Math Library Functions

Use the `-l` flag to load the standard math library. Functions use single-letter names and work with radians:

``` bash
# Trigonometric functions
echo "scale=6; s(0.5)" | bc -l          # sine(0.5)
echo "scale=6; c(0)" | bc -l            # cosine(0)
echo "scale=6; a(1)" | bc -l            # arctangent(1)

# Exponential and logarithm
echo "scale=6; e(1)" | bc -l            # e^1
echo "scale=6; l(2)" | bc -l            # natural log of 2
```

### Real-World Examples

Convert Celsius to Fahrenheit:

``` bash
#!/bin/bash

celsius=$1
fahrenheit=$(echo "scale=2; $celsius * 9/5 + 32" | bc -q)
echo "$celsius°C = $fahrenheit°F"
```

Calculate compound interest:

``` bash
#!/bin/bash

principal=$1
rate=$2
years=$3

result=$(echo "scale=2; $principal * e($years * l(1 + $rate/100))" | bc -l)
echo "Final amount: \$$result"
```

Calculate average with high precision:

``` bash
#!/bin/bash

sum=$(echo "12.5 + 8.3 + 9.7" | bc -q)
count=3
average=$(echo "scale=6; $sum / $count" | bc -q)
echo "Average: $average"
```

## Handling Precision in Financial Code

Always set `scale` explicitly for monetary calculations to avoid floating point surprises:

``` bash
# Good: explicit decimal handling for financial math
echo "scale=10; 0.1 + 0.2" | bc -q      # 0.3000000000

# Calculate price with tax
price=19.99
tax_rate=0.08
total=$(echo "scale=2; $price * (1 + $tax_rate)" | bc -q)
echo "Total: \$$total"
```

## Alternatives to bc

### awk for Simpler Math

`awk` handles floating point natively and is faster for quick calculations:

``` bash
echo "1.5 3.7" | awk '{print $1 + $2}'  # 5.2

# Process multiple values
echo "5.1 3.2" | awk '{print $1 * $2}'  # 16.32
```

Use `awk` for file processing or when you’re already parsing structured data. It’s overkill for standalone arithmetic.

### dc: Reverse Polish Notation Calculator

`dc` is older and uses reverse Polish notation, making it less intuitive but sometimes more compact:

``` bash
echo "scale=2; 10 3 / p" | dc           # 3.33 (10/3)
```

### python3 for Complex Logic

If your script already uses Python, invoke it for math:

``` bash
python3 -c "print(1.2 + 8.2)"           # 10.0
```

Don’t import Python just for arithmetic — `bc` is lighter and faster.

## When to Use What

- **bc**: Default choice for most shell scripts. Reliable, portable, handles arbitrary precision.
- **awk**: Use when processing files or combining math with data extraction.
- **dc**: Avoid unless you need reverse Polish notation for specific automation.
- **python3**: Only if the script already depends on Python.

For production scripts handling financial data, timeouts, or distributed systems, `bc` remains the standard. It’s predictable, well-understood, and available everywhere.
