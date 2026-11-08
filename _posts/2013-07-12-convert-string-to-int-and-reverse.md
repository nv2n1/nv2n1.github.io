---
title: "Converting Strings to Integers in C++: Modern Approaches and Trade-offs"
date: 2013-07-12 16:47:41 +0000
modified: 2026-04-11 17:41:40 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /convert-string-to-int-and-reverse/
---

Converting strings to integers is a fundamental operation in C++, but the method you choose affects both code clarity and performance. Here are the four main approaches, ranked by use case.

## std::stoi() — The Default Choice

`std::stoi()` is the standard C++11 method for most situations. It’s exception-based, handles whitespace automatically, and works with custom number bases.

``` cpp
#include <iostream>
#include <string>

int main()
{
  std::string str("123");

  try {
    int n = std::stoi(str);
    std::cout << n << "\n";
  }
  catch (const std::invalid_argument&) {
    std::cerr << "Invalid argument\n";
    return 1;
  }
  catch (const std::out_of_range&) {
    std::cerr << "Out of range\n";
    return 1;
  }
  return 0;
}
```

**Function signature:**

``` cpp
int stoi(const std::string& str, std::size_t* pos = 0, int base = 10);
```

**Key behavior:**

- Automatically skips leading whitespace
- Supports bases 2–36 via the third parameter
- Throws `std::invalid_argument` if no conversion occurs
- Throws `std::out_of_range` if the value exceeds `int` bounds
- Optionally returns the position of the first unconverted character

For larger integers, use `std::stol()` for `long` or `std::stoll()` for `long long`.

**Base conversion example:**

``` cpp
std::string hexStr = "FF";
int number = std::stoi(hexStr, nullptr, 16);  // Result: 255
```

Use `std::stoi()` when code clarity matters more than raw performance, or when exception-based error handling fits your control flow.

## std::from_chars() — Maximum Performance (C++17+)

For performance-critical code, `std::from_chars()` provides low-overhead conversion without exceptions or global state manipulation:

``` cpp
#include <iostream>
#include <string>
#include <charconv>

int main()
{
  std::string text = "123";
  int number;

  auto [ptr, ec] = std::from_chars(text.data(), text.data() + text.size(), number);

  if (ec == std::errc()) {
    std::cout << number << "\n";
  } else if (ec == std::errc::invalid_argument) {
    std::cerr << "Invalid argument\n";
    return 1;
  } else if (ec == std::errc::out_of_range) {
    std::cerr << "Out of range\n";
    return 1;
  }
  return 0;
}
```

**Advantages:**

- No exception overhead — ideal for tight parsing loops
- Returns both conversion status and pointer to first unconverted character
- Supports custom bases via optional parameter
- Minimal allocations or state changes

**Partial parsing example:**

``` cpp
std::string text = "123abc";
int number;
auto [ptr, ec] = std::from_chars(text.data(), text.data() + text.size(), number);

if (ec == std::errc()) {
  std::cout << "Parsed: " << number << "\n";
  std::cout << "Remaining: " << std::string(ptr, text.data() + text.size()) << "\n";
}
```

Choose `std::from_chars()` when parsing large datasets or in performance-sensitive code paths. It’s the standard choice for new C++17+ projects.

## std::istringstream — Stream-Based Parsing

String streams treat strings as input streams, allowing familiar `>>` syntax:

``` cpp
#include <iostream>
#include <string>
#include <sstream>

int main()
{
  std::string text = "123";
  std::istringstream iss(text);
  int number;

  if (iss >> number && iss.eof()) {
    std::cout << number << "\n";
  } else {
    std::cerr << "Conversion failed\n";
    return 1;
  }
  return 0;
}
```

This approach:

- Uses familiar stream extraction syntax
- Requires checking both conversion success and stream state with `eof()`
- Avoids verbose try-catch blocks
- Naturally handles multiple consecutive values

**Parsing structured data:**

``` cpp
std::string text = "123 456 789";
std::istringstream iss(text);
int a, b, c;

if (iss >> a >> b >> c && iss.eof()) {
  std::cout << "Parsed: " << a << " " << b << " " << c << "\n";
}
```

Use `std::istringstream` when parsing space-separated or structured input formats, or when working with existing stream-based code.

## strtol() — C Interoperability

For C library compatibility or working in constrained environments, `strtol()` provides error reporting via `errno`:

``` cpp
#include <iostream>
#include <cstdlib>
#include <cerrno>
#include <string>

int main()
{
  std::string text = "123";
  errno = 0;

  char* endptr = nullptr;
  long value = std::strtol(text.c_str(), &endptr, 10);

  if (errno == ERANGE) {
    std::cerr << "Value out of range\n";
    return 1;
  }

  if (endptr == text.c_str()) {
    std::cerr << "No valid conversion\n";
    return 1;
  }

  if (*endptr != '\0') {
    std::cerr << "Partial conversion detected\n";
  }

  int number = static_cast<int>(value);
  std::cout << number << "\n";
  return 0;
}
```

**Critical points:**

- Always reset `errno` to 0 before calling
- Check `endptr` to detect failed conversions
- Returns `long`, requiring explicit cast to `int`
- Risk of overflow when casting `long` to `int`
- Avoid `atoi()` — it cannot distinguish between zero and conversion failure

Use `strtol()` only when interfacing with C code or legacy systems.

## Handling Edge Cases and Untrusted Input

Different methods handle edge cases differently:

``` cpp
#include <iostream>
#include <string>
#include <vector>

int main()
{
  std::vector<std::string> test_cases = {
    "",           // Empty
    "   ",        // Whitespace only
    "abc",        // No digits
    "123abc",     // Partial conversion
    "-456",       // Negative
    "0xFF",       // Hex notation
    "999999999999" // Overflow
  };

  for (const auto& str : test_cases) {
    try {
      int n = std::stoi(str);
      std::cout << "\"" << str << "\" -> " << n << "\n";
    }
    catch (const std::invalid_argument&) {
      std::cout << "\"" << str << "\" -> Invalid\n";
    }
    catch (const std::out_of_range&) {
      std::cout << "\"" << str << "\" -> Out of range\n";
    }
  }
  return 0;
}
```

**Expected behavior with `std::stoi()`:**

- Empty strings throw `std::invalid_argument`
- Whitespace-only strings throw `std::invalid_argument`
- Partial conversions succeed (e.g., “123abc” → 123)
- Hexadecimal requires explicit base: `std::stoi(str, nullptr, 16)`
- Out-of-range values throw `std::out_of_range`

## Choosing Your Method

| Situation                        | Use                  |
|----------------------------------|----------------------|
| General-purpose, readable code   | `std::stoi()`        |
| Parsing large datasets, C++17+   | `std::from_chars()`  |
| Structured/space-separated input | `std::istringstream` |
| C library interop, legacy code   | `strtol()`           |
| Never use                        | `atoi()`             |

For new C++17+ code, prefer `std::from_chars()` in performance-critical paths and `std::stoi()` elsewhere. Both are safer and more predictable than older C-style functions.
