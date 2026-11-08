---
title: "How to Work Around g++ Non-Trivial Designated Initializers"
date: 2018-03-24 08:18:25 +0000
layout: post
canonical: https://www.systutorials.com/g-sorry-unimplemented-non-trivial-designated-initializers-not-supported/
---

Designated initializers for aggregate types with non-trivial members (like `std::vector`) have inconsistent support across GCC versions. This error typically appears when you try to initialize a struct containing standard library containers using designated initializer syntax in the wrong order.

### The Problem

When you compile this code with older GCC versions:

``` cpp
struct Stat {
    vector<int> vec;
    int depth;
    vector<pair<int, int>> moves;
};

int main() {
    vector<int> init = {1, 2, 3};
    vector<pair<int, int>> tv = {{0, 1}, {2, 3}};

    Stat init_stat {.depth = 0, .moves = tv, .vec = init};
    return 0;
}
```

GCC 4.8.x and early 5.x versions report:

    error: sorry, unimplemented: non-trivial designated initializers not supported

This happens because the compiler can’t properly handle designated initializers when:

- The struct contains non-trivial types (containers, strings, etc.)
- The initialization order differs from the member declaration order

### Solution: Match Declaration Order

Reorder your designated initializers to match the exact order members are declared in the struct:

``` cpp
Stat init_stat {.vec = init, .depth = 0, .moves = tv};
```

The key difference: `.vec` is listed first because `vec` is the first member in the struct definition.

### Better Alternatives

If you’re stuck with an old compiler or want more robust code, consider these approaches:

**1. Use a constructor (most portable)**

``` cpp
struct Stat {
    vector<int> vec;
    int depth;
    vector<pair<int, int>> moves;

    Stat(vector<int> v, int d, vector<pair<int, int>> m)
        : vec(v), depth(d), moves(m) {}
};

Stat init_stat(init, 0, tv);
```

**2. Default member initializers with assignment**

``` cpp
struct Stat {
    vector<int> vec;
    int depth = 0;
    vector<pair<int, int>> moves;
};

Stat init_stat;
init_stat.vec = init;
init_stat.moves = tv;
```

**3. Brace initialization (works in C++11)**

``` cpp
Stat init_stat {{init}, 0, {tv}};
```

### Compiler Version Considerations

- **GCC 4.8.x – 5.x**: Partial support; order-dependent with non-trivial types
- **GCC 6.0+**: Improved support; designated initializers work more reliably
- **GCC 7.0+**: Full C++17 designated initializer support

If you’re targeting modern systems, upgrade your compiler. GCC 4.8 reached end-of-life in 2014. Most production environments use GCC 9.x or later, which handle this syntax reliably.

### Prevention

When writing new code targeting C++11/14, prefer constructors or aggregate initialization without designated initializers if non-trivial members are involved. Designated initializers became truly reliable in C++20 when the standard formalized their behavior more strictly.

If you must use designated initializers with containers:

- Always match the struct member declaration order
- Consider upgrading your build toolchain
- Test on the actual compiler version your target platform uses

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
