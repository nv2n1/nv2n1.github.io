---
title: "Modern C++ References: Best Practices and Guidelines"
date: 2013-07-12 19:06:24 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /c-reference-and-styles/
---

**cppreference.com** is the authoritative resource for C++ language and standard library documentation. It covers all C++ standards from C++98 through C++26 with clear examples and cross-references. Bookmark it as your primary reference.

The official C++ standard drafts are available through the C++ standards committee. While final standards require purchase, draft versions and proposals are freely available—useful for understanding language features and library behavior at a deeper level.

Key cppreference sections you’ll reference constantly:

- Containers (vector, map, unordered_map, deque, flat_map, etc.)
- Algorithms and iterators, including ranges (C++20+)
- Memory management (smart pointers, allocators)
- Concurrency primitives (threads, mutexes, condition variables, semaphores)
- Type traits and metaprogramming utilities
- Formatting and string handling

Keep documentation locally accessible. Network latency during debugging sessions adds up. Download an offline copy if your environment has limited connectivity—cppreference offers offline builds.

## Style Guidelines

Style consistency matters more than which specific rules you follow, but community standards have emerged.

### Google C++ Style Guide

- No exceptions for new code
- Naming conventions: `ClassName`, `methodName`, `member_variable_`
- Comprehensive coverage of modern C++ practices
- Widely adopted in large codebases

### LLVM Coding Standards

- Emphasis on readable, maintainable code
- Clear guidance on C++17 and later features
- Strong stance on const-correctness and RAII

### C++ Core Guidelines

- Maintained by Bjarne Stroustrup and the C++ standards committee
- Modern, principles-based approach
- Covers safety and correctness, not just style
- Supported by tools like clang-tidy with specific rule sets

### Your Team’s Guide

Document decisions on:

- Naming conventions
- Spacing and indentation
- const usage
- Error handling strategy
- Minimum C++ version requirement

Enforce via linters (`clang-tidy`, `cppcheck`) and formatters (`clang-format`). Store in your repository and reference in the README.

## Automated Enforcement

Manual code reviews catch style violations slowly and inconsistently. Use tooling to enforce standards automatically.

### Code Formatting

Format code to project standard:

``` bash
clang-format -i yourfile.cpp
```

Create a `.clang-format` file in your project root:

``` bash
clang-format --dump-config > .clang-format
# Edit to match your preferences and commit to version control
```

Example `.clang-format` configuration for modern C++:

``` yaml
BasedOnStyle: LLVM
IndentWidth: 4
ColumnLimit: 100
AlignTrailingComments: true
AllowShortFunctionsOnASingleLine: InlineOnly
BreakBeforeBraces: Allman
```

### Linting and Static Analysis

Check against common issues and style violations:

``` bash
clang-tidy yourfile.cpp -- -I/path/to/includes
```

Run deeper static analysis:

``` bash
cppcheck --enable=all src/
```

### CMake Integration

Integrate formatting and linting into your build:

``` cmake
# Format code before building
add_custom_target(format
  COMMAND clang-format -i ${CMAKE_SOURCE_DIR}/src/*.cpp
  COMMAND clang-format -i ${CMAKE_SOURCE_DIR}/include/*.hpp
)
add_dependencies(${PROJECT_NAME} format)

# Enable clang-tidy checks during compilation
set(CMAKE_CXX_CLANG_TIDY 
  clang-tidy 
  -checks=readability-*,modernize-*,performance-*
  -header-filter=.*
)

# Optional: fail on compiler warnings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror -Wall -Wextra -Wpedantic")
```

### CI/CD Pipeline Checks

Fail the build on style violations:

``` bash
#!/bin/bash
set -e

clang-format --dry-run --Werror src/*.cpp include/*.hpp
clang-tidy src/*.cpp -- -I./include
cppcheck --error-exitcode=1 --enable=all src/
```

Integrate into your CI pipeline (GitHub Actions, GitLab CI, Jenkins, etc.) so violations are caught before merge.

## Key Style Principles

### const-Correctness

Apply const liberally to methods and parameters. It documents intent, enables compiler optimizations, and catches mutations early:

``` cpp
const std::string& getName() const { return name_; }
void update(const User& user);
```

### RAII

Resources (memory, files, locks) are tied to object lifetime. This avoids leaks and makes code exception-safe by default. Use smart pointers instead of manual `new`/`delete`:

``` cpp
std::unique_ptr<File> file = std::make_unique<File>("data.txt");
std::vector<std::thread> workers;
// Automatic cleanup when scope exits
```

### Naming Clarity

Avoid single-letter variables outside loops. `user_count` beats `n`. Use names that reveal intent:

``` cpp
// Good
for (int i = 0; i < batch_size; ++i) { /* ... */ }
int active_connections = 0;

// Avoid
for (int i = 0; i < bs; ++i) { /* ... */ }
int n = 0;
```

### Error Handling

Pick a strategy and stick to it across the project:

``` cpp
// Optional approach (lightweight, no error detail)
std::optional<User> findUser(int id);

// Expected approach (C++23 or backport, includes error info)
std::expected<Data, Error> parse(std::string_view input);

// Exception approach (explicit error handling)
try {
  processData(input);
} catch (const std::invalid_argument& e) {
  log_error("Invalid input: {}", e.what());
}
```

Mixing approaches creates bugs. Choose one, document it, and enforce it.

### Modern C++ Features

Use C++17 or C++20 features in new code. Avoid C++98 patterns. If your codebase supports an older standard, document this decision and the rationale.

Structured bindings (C++17):

``` cpp
auto [name, age] = getUserData();
```

Ranges (C++20):

``` cpp
auto adults = users 
  | std::views::filter([](const User& u) { return u.age >= 18; })
  | std::views::transform([](const User& u) { return u.name; });
```

std::optional (C++17):

``` cpp
if (auto user = findUser(42)) {
  std::cout << user->name << "\n";
}
```

## Setup in Your Project

Link your chosen guide and configuration files in the project README. New contributors should know what’s expected before submitting pull requests. Automated tooling means style issues are caught before review, leaving human reviewers to focus on logic and correctness.

Example README section:

``` markdown
## Code Style

This project follows the [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines) 
with our team's [style configuration](.clang-format).

Before submitting a PR:
- Run `cmake --build . --target format` to format code
- Run `cmake --build .` to check linting during build
- Ensure CI passes on your branch
```
