---
title: "Hexadecimal Input and Output in C++"
date: 2013-07-12 16:47:41 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/inputing-and-outputing-hex-numbers-with-iostream/
---

Use `std::hex` to format output as hexadecimal. This manipulator sets the basefield of the stream, affecting all subsequent integer output until you change it.

``` cpp
#include <iostream>

int main() {
    int x = 255;
    std::cout << "x in hexadecimal: " << std::hex << x << std::endl;
    return 0;
}
```

Output:

    x in hexadecimal: ff

By default, `std::hex` produces lowercase letters (a-f). Use `std::uppercase` for uppercase output:

``` cpp
#include <iostream>

int main() {
    int x = 255;
    std::cout << std::hex << std::uppercase << x << std::endl;
    return 0;
}
```

Output:

    FF

## Inputting Hexadecimal Integers

Use `std::hex` with `std::cin` to parse input as hexadecimal:

``` cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter a hexadecimal integer: ";
    std::cin >> std::hex >> x;
    std::cout << "You entered: " << x << std::endl;
    return 0;
}
```

If the user enters `ff`:

    Enter a hexadecimal integer: ff
    You entered: 255

Note that `std::cin >> std::hex >> x` accepts input with or without the `0x` prefix — both `ff` and `0xff` parse correctly as 255.

## Understanding Stream State Persistence

A critical detail: `std::hex` is sticky. Once applied, it affects all subsequent integer operations on that stream until explicitly changed:

``` cpp
#include <iostream>

int main() {
    int x = 255;
    int y = 100;

    std::cout << std::hex << x << std::endl;      // outputs: ff
    std::cout << y << std::endl;                  // outputs: 64 (still hex!)
    std::cout << std::dec << y << std::endl;      // outputs: 100 (decimal)
    return 0;
}
```

Always restore the desired base with `std::dec` when switching back to decimal. Alternatively, use the stream state save/restore pattern to isolate formatting changes:

``` cpp
#include <iostream>
#include <iomanip>

int main() {
    int x = 255;
    int y = 100;

    std::ios_base::fmtflags flags(std::cout.flags());

    std::cout << std::hex << x << std::endl;      // outputs: ff
    std::cout << y << std::endl;                  // outputs: 64 (hex)

    std::cout.flags(flags);                       // restore original state
    std::cout << y << std::endl;                  // outputs: 100 (decimal)
    return 0;
}
```

## Adding the 0x Prefix

To include the `0x` prefix in output, combine `std::hex` with `std::showbase`:

``` cpp
#include <iostream>

int main() {
    int x = 255;
    std::cout << std::hex << std::showbase << x << std::endl;
    return 0;
}
```

Output:

    0xff

## Handling Negative and Large Values

Negative integers output as two’s complement in hexadecimal:

``` cpp
#include <iostream>

int main() {
    int x = -1;
    std::cout << std::hex << x << std::endl;  // outputs: ffffffff (on 32-bit)
    return 0;
}
```

For unsigned types, you get the full positive range without sign extension:

``` cpp
#include <iostream>

int main() {
    unsigned int x = 255;
    std::cout << std::hex << x << std::endl;  // outputs: ff
    return 0;
}
```

When working with 64-bit values, the output expands accordingly:

``` cpp
#include <iostream>

int main() {
    unsigned long long x = -1ULL;
    std::cout << std::hex << x << std::endl;  // outputs: ffffffffffffffff
    return 0;
}
```

## Input Validation

When reading hex with `std::cin`, check for parse failures. Invalid input leaves the stream in a failed state, so clear the failbit and discard bad data:

``` cpp
#include <iostream>

int main() {
    unsigned int x;
    std::cout << "Enter hex value: ";

    if (!(std::cin >> std::hex >> x)) {
        std::cerr << "Invalid input" << std::endl;
        std::cin.clear();                           // clear failbit
        std::cin.ignore(10000, '\n');               // discard bad input
        return 1;
    }

    std::cout << "Parsed value: " << std::dec << x << std::endl;
    return 0;
}
```

## Modern Approach: std::format (C++20+)

For modern code, prefer `std::format` for cleaner, scoped formatting without stream state side effects:

``` cpp
#include <iostream>
#include <format>

int main() {
    int x = 255;
    std::cout << std::format("Value in hex: {:x}\n", x);      // lowercase: ff
    std::cout << std::format("Value in hex: {:X}\n", x);      // uppercase: FF
    std::cout << std::format("Value in hex: {:#x}\n", x);     // with prefix: 0xff
    return 0;
}
```

This approach avoids stream state issues entirely and integrates better with complex formatting requirements.

## Isolating Manipulator State with std::stringstream

If C++20 is unavailable, use `std::stringstream` with manipulators to isolate formatting changes and avoid polluting the main output stream state:

``` cpp
#include <iostream>
#include <sstream>
#include <iomanip>

int main() {
    int x = 255;
    int y = 100;

    std::stringstream ss;
    ss << std::hex << std::showbase << x;
    std::cout << "Value: " << ss.str() << std::endl;  // outputs: 0xff

    // main stream state unaffected
    std::cout << "Next value: " << std::dec << y << std::endl;  // outputs: 100
    return 0;
}
```

This pattern is safer than manipulating `std::cout` directly when hex formatting is temporary or localized.
