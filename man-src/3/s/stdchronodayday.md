---
title: "stdchronodayday(3)"
name: "stdchronodayday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronodayday/"
---

std::chrono::day::day - std::chrono::day::day

<h2>Synopsis</h2>

<pre><code>day() = default;                             (1) (since C++20)

explicit constexpr day(unsigned d) noexcept; (2) (since C++20)</code></pre> 
Constructs a day object. 
1) Default constructor leaves the day value uninitialized. 
2) If d &lt;= 255, constructs a day object holding the day value d. Otherwise the value held is unspecified. 
