---
title: "stdchronoyearyear(3)"
name: "stdchronoyearyear"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearyear/"
---

std::chrono::year::year - std::chrono::year::year

<h2>Synopsis</h2>

<pre><code>year() = default;
(since C++ 20)

    explicit constexpr year(int y) noexcept;
(since C++ 20)</code></pre> 
Constructs a year object. 
1) Default constructor leaves the year value uninitialized. 
2) If y is in the range [-32767, 32767], constructs a year object holding the year value y. Otherwise the value held is unspecified. 
