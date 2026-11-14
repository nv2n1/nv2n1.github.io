---
title: "stdchronomonth_weekdaymonth_weekday(3)"
name: "stdchronomonth_weekdaymonth_weekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_weekdaymonth_weekday/"
---

std::chrono::month_weekday::month_weekday - std::chrono::month_weekday::month_weekday

<h2>Synopsis</h2>

<pre><code>constexpr month_weekday(const std::chrono::month &amp;m, (since C++ 20)

                                                         const std::chrono::weekday_indexed &amp;wdi) noexcept;</code></pre> 
Constructs a month_weekday object that stores the month m and the weekday_indexed wdi. 

<h2>Notes</h2>

A more convenient way to construct a month_weekday is with operator/, e.g., std::chrono::April/std::chrono::Sunday[2]. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
