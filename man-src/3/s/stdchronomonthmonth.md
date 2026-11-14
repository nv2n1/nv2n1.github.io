---
title: "stdchronomonthmonth(3)"
name: "stdchronomonthmonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonthmonth/"
---

std::chrono::month::month - std::chrono::month::month

<h2>Synopsis</h2>

<pre><code>month() = default;                             (1) (since C++20)

explicit constexpr month(unsigned m) noexcept; (2) (since C++20)</code></pre> 
Constructs a month object. 
1) Default constructor leaves the month value uninitialized. 
2) If m &lt;= 255, constructs a month object holding the month value m. Otherwise the value held is unspecified. 
