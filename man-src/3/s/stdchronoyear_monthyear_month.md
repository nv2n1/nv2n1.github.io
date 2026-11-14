---
title: "stdchronoyear_monthyear_month(3)"
name: "stdchronoyear_monthyear_month"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_monthyear_month/"
---

std::chrono::year_month::year_month - std::chrono::year_month::year_month

<h2>Synopsis</h2>

<pre><code>year_month() = default;
(1)(since C++ 20)

    constexpr year_month(const std::chrono::year &amp;y, const std::chrono::month &amp;m) noexcept;
(2)(since C++ 20)</code></pre> 
Constructs a year_month object. 
1) Default constructor leaves the year and month uninitialized. 
2) Constructs a year_month object storing the year y and the month m. 

<h2>Notes</h2>

A more convenient way to construct a year_month is with operator/, e.g., 2007y/std::chrono::April. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
