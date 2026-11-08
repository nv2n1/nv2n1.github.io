---
title: "String Splitting in C++: Building a Flexible Utility Function"
date: 2023-05-01 13:59:01 +0000
modified: 2026-04-11 17:11:07 +0000
author: "Ethan Ainsworth"
layout: post
categories: [languages-frameworks]
canonical: /splitting-a-string-by-another-string-in-cpp/
---

Unlike Python or JavaScript, C++ doesn’t provide a built-in `split()` method for strings. You’ll need to use library functions or write your own utility. The best approach depends on your compiler version, performance requirements, and whether you’re handling edge cases.

## The Classic Approach: find() and substr()

The most straightforward method uses `std::string::find()` to locate delimiters and `std::string::substr()` to extract segments. Here’s a reliable implementation:

``` cpp
#include <vector>
#include <string>

std::vector<std::string> split(const std::string& s, const std::string& delimiter) {
    std::vector<std::string> tokens;
    size_t start = 0;
    size_t end = s.find(delimiter);

    while (end != std::string::npos) {
        tokens.push_back(s.substr(start, end - start));
        start = end + delimiter.length();
        end = s.find(delimiter, start);
    }

    tokens.push_back(s.substr(start));
    return tokens;
}
```

This version avoids modifying the input string (unlike earlier approaches that used `erase()`), which is safer and clearer about intent.

**Example usage:**

``` cpp
auto parts = split("user:pass:host", ":");
// Result: {"user", "pass", "host"}
```

## Modern C++20/23: Ranges Library

If you’re using GCC 13+, Clang 16+, or MSVC 2022+, leverage `std::ranges::split()` from the Ranges library:

``` cpp
#include <ranges>
#include <string>
#include <vector>

std::vector<std::string> split_ranges(const std::string& s, char delimiter) {
    std::vector<std::string> tokens;
    auto ranges_result = s | std::views::split(delimiter);

    for (auto token : ranges_result) {
        tokens.push_back(std::string(token.begin(), token.end()));
    }

    return tokens;
}
```

This is more concise, but note that `std::views::split()` returns a range of `std::string_view` objects, not strings. You’ll need to convert them if you need actual `std::string` objects for long-term storage.

## Zero-Copy Approach: std::string_view

For performance-critical code (parsing large files, network buffers), avoid creating copies. Use `std::string_view` to reference portions of the original string:

``` cpp
#include <vector>
#include <string_view>

std::vector<std::string_view> split_view(std::string_view s, std::string_view delimiter) {
    std::vector<std::string_view> tokens;
    size_t start = 0;
    size_t end = s.find(delimiter);

    while (end != std::string_view::npos) {
        tokens.push_back(s.substr(start, end - start));
        start = end + delimiter.length();
        end = s.find(delimiter, start);
    }

    tokens.push_back(s.substr(start));
    return tokens;
}
```

This eliminates string copies entirely. Useful for one-pass parsing or batch processing where you don’t need to store tokens long-term.

## Handling Edge Cases

The implementations above work for most cases, but consider these scenarios:

**Empty tokens:** If your delimiter appears consecutively (e.g., `"a,,b"`), you’ll get empty strings in the result. If you want to skip them:

``` cpp
if (!token.empty()) {
    tokens.push_back(token);
}
```

**Trailing delimiters:** A string like `"a:b:"` will produce an empty final token. Decide whether to keep or discard it based on your use case.

**Multi-character delimiters:** The above functions handle these correctly. `split("foo::bar", "::")` produces `{"foo", "bar"}`.

## Using Boost for Production Code

For robust, well-tested string utilities, Boost.StringAlgorithms is mature and handles many edge cases:

``` cpp
#include <boost/algorithm/string.hpp>
#include <vector>
#include <string>

std::vector<std::string> tokens;
boost::split(tokens, "hello world example", boost::is_space());
```

Boost’s `split()` supports predicates for delimiters (not just exact strings) and token compression options.

## Performance Considerations

For CSV parsing, log file processing, or network protocol parsing with large inputs:

- **Prefer `std::string_view`** to avoid allocations
- **Reserve vector capacity** if you know approximate token count: `tokens.reserve(estimated_count)`
- **Avoid repeated allocations** by reusing a function’s return vector in tight loops
- **Profile first** before micro-optimizing—most string splits aren’t the bottleneck

Choose the method matching your C++ standard, performance needs, and error handling requirements. For modern codebases, `std::ranges::split()` is cleaner; for maximum compatibility with older projects, the find/substr approach remains reliable.
