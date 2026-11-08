---
title: "Formatting Output with C++ cout"
date: 2018-03-24 08:18:30 +0000
layout: post
canonical: https://www.systutorials.com/c-cout-formatting-output/
---

C++ provides the `<iomanip>` header for controlling how data appears when printed to standard output. These manipulators give you precise control over formatting, alignment, precision, and radix.

### Basic Manipulators

The most common manipulators are persistent (they remain active until changed) or stateless (they apply once and reset).

**Width and Alignment:**

``` cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::setw(10) << "Name" << std::setw(10) << "Score" << '\n';
    std::cout << std::setw(10) << "Alice" << std::setw(10) << 95 << '\n';
    std::cout << std::setw(10) << "Bob" << std::setw(10) << 87 << '\n';
    return 0;
}
```

`std::setw()` sets the minimum field width for the next output only. By default, numeric values right-align and strings left-align within the field.

Use `std::left` and `std::right` to control alignment (these persist):

``` cpp
std::cout << std::left << std::setw(10) << "Name" 
          << std::right << std::setw(10) << "Score" << '\n';
```

**Floating-Point Precision:**

``` cpp
double pi = 3.14159265359;

std::cout << std::setprecision(3) << pi << '\n';        // 3.14
std::cout << std::fixed << std::setprecision(2) << pi << '\n';  // 3.14
std::cout << std::scientific << std::setprecision(2) << pi << '\n';  // 3.14e+00
```

- `std::setprecision(n)` without `std::fixed` sets total significant digits
- `std::fixed` switches to fixed-point notation
- `std::scientific` uses exponential notation
- These are persistent settings

**Number Base:**

``` cpp
int value = 255;

std::cout << std::dec << value << '\n';        // 255
std::cout << std::hex << value << '\n';        // ff
std::cout << std::oct << value << '\n';        // 377
std::cout << std::showbase << std::hex << value << '\n';  // 0xff
```

`std::showbase` adds the prefix (`0x` for hex, `0` for octal). This persists until you call `std::noshowbase`.

**Fill Characters:**

``` cpp
std::cout << std::setfill('*') << std::right 
          << std::setw(10) << 42 << '\n';  // ********42
```

The fill character persists across operations.

### Practical Example: Tabular Output

Here’s a realistic scenario formatting a data table:

``` cpp
#include <iostream>
#include <iomanip>
#include <vector>

struct Record {
    std::string name;
    int id;
    double salary;
};

int main() {
    std::vector<Record> records = {
        {"Alice Johnson", 1001, 75000.50},
        {"Bob Smith", 1002, 68500.00},
        {"Charlie Brown", 1003, 82300.75}
    };

    std::cout << std::left 
              << std::setw(20) << "Name"
              << std::right 
              << std::setw(8) << "ID"
              << std::setw(15) << "Salary"
              << '\n'
              << std::setfill('-') << std::setw(43) << "" << '\n'
              << std::setfill(' ');

    for (const auto& r : records) {
        std::cout << std::left << std::setw(20) << r.name
                  << std::right 
                  << std::setw(8) << r.id
                  << "$" << std::setw(13) << std::fixed 
                  << std::setprecision(2) << r.salary
                  << '\n';
    }

    return 0;
}
```

### Resetting Formatting

To reset all formatting flags to their default state:

``` cpp
std::cout.copyfmt(std::ios(NULL));
```

Or reset individual flags:

``` cpp
std::cout << std::noshowbase << std::defaultfloat << std::right;
```

`std::defaultfloat` (C++11) resets the floating-point format to the default.

### Low-Level Control with setf()

For more granular control, use the flags directly:

``` cpp
std::cout.setf(std::ios::showpoint);  // Always show decimal point
std::cout.setf(std::ios::uppercase);  // HEX, not hex
std::cout.unsetf(std::ios::floatfield);  // Reset float formatting
```

Most use cases are better served by the manipulators, but this approach is useful when you need to test or manipulate flags programmatically.

### Common Pitfalls

- `std::setw()` only affects the next output operation
- Many manipulators persist — change them back explicitly or save/restore the stream state
- `std::setprecision()` behaves differently depending on whether `std::fixed` is active
- For currency, padding with zeros typically requires both `std::setfill('0')` and careful positioning of symbols
