---
title: "Using Type Erasure in C++11 Lambda Parameters"
date: 2018-03-24 11:55:24 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /how-to-not-use-concrete-types-in-lambda-function-parameters-in-c11/
---

In C++11, lambda parameters required concrete types. Creating a truly generic lambda meant wrapping the logic in a template struct — awkward and verbose. C++14 introduced generic lambdas using `auto` for parameter deduction, eliminating this friction entirely.

## Basic Generic Lambda Syntax

The simplest approach uses `auto` in lambda parameters:

``` cpp
auto add = [](auto a, auto b) {
    return a + b;
};

// Works with integers
int result1 = add(5, 3);  // 8

// Works with floating point
double result2 = add(2.5, 3.7);  // 6.2

// Works with std::string
auto result3 = add(std::string("hello"), std::string(" world"));  // "hello world"
```

The compiler generates specialized code for each type combination you actually use. This is zero-overhead abstraction — no virtual dispatch, no runtime penalty.

## Using Concepts for Type Constraints (C++20)

Generic lambdas become more powerful with Concepts, which let you constrain what types `auto` accepts:

``` cpp
#include <concepts>

// Only accept integral types
auto integral_add = [](std::integral auto a, std::integral auto b) {
    return a + b;
};

// This works
int x = integral_add(10, 20);

// This fails at compile time (preventing silent bugs)
// double y = integral_add(1.5, 2.5);  // Error: double doesn't satisfy std::integral
```

Custom concepts give you fine-grained control:

``` cpp
template<typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<T>;
};

auto safe_add = [](Addable auto a, Addable auto b) {
    return a + b;
};
```

## Multiple Type Parameters with Constraints

When you need different types in different parameters:

``` cpp
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

auto multiply = [](Numeric auto x, Numeric auto y) {
    return x * y;
};

int a = multiply(5, 10);           // 50
double b = multiply(2.5, 4.0);     // 10.0
```

## Deduction Guides and Complex Scenarios

For more complex scenarios, you might need explicit template parameters. While lambdas don’t support template parameters directly in older standards, you can use `std::function` or write a template wrapper:

``` cpp
// For C++23 and beyond, explicit lambda template parameters are available
auto process = []<typename T>(T value) {
    if constexpr (std::integral<T>) {
        return value * 2;
    } else if constexpr (std::floating_point<T>) {
        return value * 1.5;
    }
};
```

## Performance Characteristics

Generic lambdas compile to the same machine code as hand-written template functions. The compiler specializes each instantiation:

- No virtual function overhead
- No type erasure penalty
- Monomorphization happens at compile time
- Binary size scales with the number of type combinations used

## Avoiding Common Pitfalls

**Type mismatch in parameters:** When `auto a` and `auto b` have different types, operations might fail silently or produce unexpected results:

``` cpp
auto generic_op = [](auto a, auto b) {
    return a + b;  // What if a is int and b is unsigned?
};
```

Concepts solve this:

``` cpp
auto safe_op = [](std::integral auto a, std::integral auto b) {
    return a + b;
};
```

**Lambda type identity:** Each lambda expression has a unique, unnamed type. You can’t write it explicitly, but `auto` captures it:

``` cpp
auto lambda1 = [](auto x) { return x * 2; };
auto lambda2 = [](auto x) { return x * 2; };

// lambda1 and lambda2 have different types, even though they're identical
```

If you need to store different lambdas in a container, use `std::function`:

``` cpp
std::vector<std::function<int(int)>> operations;
operations.push_back([](auto x) { return x * 2; });
operations.push_back([](auto x) { return x + 10; });
```

## Summary

Generic lambdas with `auto` are the standard approach in modern C++. Combine them with Concepts (C++20+) to enforce type safety at compile time. This gives you the flexibility of templates with the clarity of constraints, and you get peak performance with zero overhead.
