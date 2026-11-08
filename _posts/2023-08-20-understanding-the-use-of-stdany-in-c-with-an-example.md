---
title: "Using std::any for Type-Safe Polymorphism in C++"
date: 2023-08-20 09:01:44 +0000
author: "Ethan Ainsworth"
layout: post
canonical: https://www.systutorials.com/understanding-the-use-of-stdany-in-c-with-an-example/
---

`std::any` (C++17) is a type-safe container for single values of any type. It lets you store an `int`, string, custom struct, or vector in the same variable without losing type information—unlike `void*` pointers, which are inherently unsafe.

## How It Works

`std::any` uses type erasure: it wraps whatever you give it, remembers the exact type, and lets you retrieve it safely. Attempt the wrong type and you get `std::bad_any_cast` instead of undefined behavior.

Under the hood, `std::any` typically allocates on the heap for larger objects, though small-object optimization (SBO) can eliminate this for tiny types. The key trade-off: flexibility over performance.

## Basic Example

``` cpp
#include <iostream>
#include <any>
#include <map>
#include <string>

int main() {
    std::map<std::string, std::any> config;
    config["volume"] = 75;
    config["username"] = std::string("Admin");
    config["fullscreen"] = true;
    config["framerate"] = 60.0;

    // Safe retrieval with type checking
    if (config["volume"].type() == typeid(int)) {
        int vol = std::any_cast<int>(config["volume"]);
        std::cout << "Volume: " << vol << std::endl;
    }

    // This would throw std::bad_any_cast
    try {
        std::string user = std::any_cast<std::string>(config["volume"]);
    } catch (const std::bad_any_cast& e) {
        std::cout << "Type mismatch: " << e.what() << std::endl;
    }

    return 0;
}
```

## Checking and Casting

Always verify the type before casting. Three approaches:

``` cpp
std::any value = 42;

// Method 1: type() comparison
if (value.type() == typeid(int)) {
    int x = std::any_cast<int>(value);
}

// Method 2: Pointer cast (returns nullptr on mismatch, no exception)
if (auto ptr = std::any_cast<int>(&value)) {
    std::cout << "Got: " << *ptr << std::endl;
}

// Method 3: Exception-based (throws on mismatch)
try {
    int x = std::any_cast<int>(value);
} catch (const std::bad_any_cast&) {
    std::cout << "Wrong type" << std::endl;
}
```

The pointer version is safest for conditional logic since it won’t throw.

## When to Use std::any

`std::any` shines in scenarios where the set of types is truly open-ended at compile time:

- Configuration systems that load from files
- Plugin architectures where plugins define custom data types
- Scripting engine bindings
- Message queues with heterogeneous payloads
- Event systems with variable argument types

## std::any vs std::variant

Don’t confuse these two. `std::variant` stores one of a **fixed, known set** of types:

``` cpp
std::variant<int, std::string, double> v = "hello";
// Compiler knows exactly what's possible
```

`std::any` stores **any type at all**:

``` cpp
std::any a = "hello";
// Runtime determines the type
```

**Choose `std::variant`** for:

- Known type sets (faster, no heap allocation)
- Performance-sensitive code
- APIs where you want to restrict what callers can pass

**Choose `std::any`** for:

- Truly open-ended scenarios
- Plugin/extension systems
- Configuration or data exchange where types arrive at runtime

## Performance Considerations

`std::any` has measurable overhead:

1.  **Heap allocation**: Most implementations allocate dynamically, except for very small objects (typically up to 32–48 bytes depending on the standard library).
2.  **Type lookup**: Runtime type checking adds a pointer dereference per cast.
3.  **Copy cost**: Copying an `std::any` copies the contained object, not just a pointer.

``` cpp
// Benchmark-relevant pattern
std::vector<std::any> data;
for (int i = 0; i < 1000000; ++i) {
    data.push_back(std::any(i));  // Allocates for each int
    int x = std::any_cast<int>(data.back());  // Runtime type check + dereference
}
```

In hot loops or real-time systems, prefer `std::variant` or just use the correct type directly.

## Resetting and Checking for Empty

``` cpp
std::any a = 42;

// Check if it holds a value
if (a.has_value()) {
    std::cout << "Contains something" << std::endl;
}

// Clear it
a.reset();
if (!a.has_value()) {
    std::cout << "Now empty" << std::endl;
}
```

## Practical Pattern: Visitor-Like Behavior

For multiple possible types, some codebases emulate `std::variant`‘s visitor pattern manually:

``` cpp
std::any val = "test";

if (val.type() == typeid(int)) {
    process_int(std::any_cast<int>(val));
} else if (val.type() == typeid(std::string)) {
    process_string(std::any_cast<std::string>(val));
} else if (val.type() == typeid(double)) {
    process_double(std::any_cast<double>(val));
}
```

It’s verbose but straightforward. If you find yourself writing this pattern often, `std::variant` is probably a better fit.
