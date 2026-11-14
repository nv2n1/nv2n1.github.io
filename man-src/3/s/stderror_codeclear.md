---
title: "stderror_codeclear(3)"
name: "stderror_codeclear"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codeclear/"
---

std::error_code::clear - std::error_code::clear

<h2>Synopsis</h2>

<pre><code>void clear() noexcept;
(since C++ 11)
    Replaces the error code and error category with default values.

    Equivalent to *this = error_code(0, std::system_category()).
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 
