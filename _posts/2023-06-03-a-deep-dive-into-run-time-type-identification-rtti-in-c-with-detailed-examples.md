---
title: "RTTI in C++: Dynamic Type Checking with Examples"
date: 2023-06-03 09:56:46 +0000
layout: post
canonical: https://www.systutorials.com/a-deep-dive-into-run-time-type-identification-rtti-in-c-with-detailed-examples/
---

RTTI is a C++ mechanism that allows you to determine an object’s type at runtime. It’s essential when working with polymorphism and inheritance hierarchies, but it comes with trade-offs you need to understand.

## Key RTTI Operators

**typeid()** — Returns a `std::type_info` object representing the type. You can compare type information or get a human-readable name via `.name()`.

**dynamic_cast** — Safely converts pointers or references down an inheritance hierarchy. For pointers, a failed cast returns `nullptr`; for references, it throws `std::bad_cast`.

Both require virtual functions in the base class. RTTI is disabled if your base class lacks a virtual destructor or virtual methods.

## Safe Downcasting with dynamic_cast

The primary use case for RTTI is safe downcasting:

``` cpp
class Animal {
public:
    virtual ~Animal() {}
    virtual void speak() = 0;
};

class Dog : public Animal {
public:
    void speak() override { std::cout << "Woof!\n"; }
    void fetch() { std::cout << "Fetching...\n"; }
};

class Cat : public Animal {
public:
    void speak() override { std::cout << "Meow!\n"; }
};

void process(Animal* a) {
    if (Dog* d = dynamic_cast<Dog*>(a)) {
        d->fetch();  // Safe; we confirmed it's a Dog
    } else if (Cat* c = dynamic_cast<Cat*>(a)) {
        std::cout << "It's a cat\n";
    }
}
```

## Using typeid for Type Checking

`typeid()` is useful when you need to examine or log type information:

``` cpp
void diagnose(Animal* a) {
    std::cout << "Type: " << typeid(*a).name() << "\n";

    if (typeid(*a) == typeid(Dog)) {
        std::cout << "Object is a Dog\n";
    }
}
```

Note: `typeid(*a).name()` produces compiler-specific mangled names. Use `__cxa_demangle()` on GCC/Clang to get readable output, or rely on the comparison directly.

## Reference Casting and Exception Handling

With references, `dynamic_cast` throws on failure rather than returning null:

``` cpp
void processRef(Animal& a) {
    try {
        Dog& d = dynamic_cast<Dog&>(a);
        d.fetch();
    } catch (const std::bad_cast& e) {
        std::cerr << "Not a Dog: " << e.what() << "\n";
    }
}
```

## When to Avoid RTTI

Modern C++ offers better alternatives for most scenarios:

**Virtual Functions** — If you need type-specific behavior, add a virtual method to the base class and override it in derived classes. This is faster and clearer:

``` cpp
class Animal {
public:
    virtual ~Animal() {}
    virtual void performSpecialAction() {}
};

class Dog : public Animal {
public:
    void performSpecialAction() override { fetch(); }
};
```

**std::variant** — For small, fixed type hierarchies where inheritance feels overkill, use `std::variant` with `std::visit`:

``` cpp
struct Dog { void fetch() {} };
struct Cat { void scratch() {} };
struct Bird { void sing() {} };

using Pet = std::variant<Dog, Cat, Bird>;

void interact(Pet& pet) {
    std::visit([](auto& p) {
        if constexpr (std::is_same_v<decltype(p), Dog&>) {
            p.fetch();
        } else if constexpr (std::is_same_v<decltype(p), Cat&>) {
            p.scratch();
        }
    }, pet);
}
```

`std::variant` avoids the runtime overhead of virtual function tables and provides compile-time type safety with `std::visit`.

## Performance Considerations

RTTI adds overhead:

- Virtual function table lookups for `dynamic_cast`
- Type information stored in memory
- Pointer comparison during casting

For performance-critical code (real-time systems, tight loops), prefer virtual dispatch or `std::variant`. For typical application code, the overhead is negligible.

## RTTI Disabled Scenarios

If your compiler flag disables RTTI (e.g., `-fno-rtti` on GCC/Clang), `typeid()` and `dynamic_cast` won’t work. Some embedded or game engine builds disable it intentionally to reduce binary size. Check your build configuration if you encounter linker errors or unexpected null casts.

## Summary

Use RTTI when you genuinely need runtime type information in a heterogeneous object hierarchy. For most new code, reach for virtual functions first, then `std::variant` if appropriate. Reserve RTTI for integration scenarios or when you inherit code that relies on it. Always measure performance in your actual use case before assuming RTTI is a bottleneck.
