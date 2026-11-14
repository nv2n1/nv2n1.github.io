---
title: "stdchronomonth_daymonth_day(3)"
name: "stdchronomonth_daymonth_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_daymonth_day/"
---

std::chrono::month_day::month_day - std::chrono::month_day::month_day

<h2>Synopsis</h2>

<pre><code>month_day() = default;
(1)(since C++ 20)

    constexpr month_day(const std::chrono::month &amp;m, const std::chrono::day &amp;d) noexcept;
(2)(since C++ 20)</code></pre> 
Constructs a month_day. 
1) Default constructor leaves the stored month and day values uninitialized. 
2) Constructs a month_day that stores the month m and the day d. 

<h2>Notes</h2>

A more convenient way to construct a month_day is with operator/, e.g., std::chrono::April/1. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
