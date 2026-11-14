---
title: "stdchronomonth_weekday_lastmonth_weekday_last(3)"
name: "stdchronomonth_weekday_lastmonth_weekday_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_weekday_lastmonth_weekday_last/"
---

std::chrono::month_weekday_last::month_weekday_last - std::chrono::month_weekday_last::month_weekday_last

<h2>Synopsis</h2>

<pre><code>constexpr month_weekday_last(const std::chrono::month &amp;m, (since C++ 20)

                                                              const std::chrono::weekday_last &amp;wdl) noexcept;</code></pre> 
Constructs a month_weekday_last object that stores the month m and the weekday_last wdl. 

<h2>Notes</h2>

A more convenient way to construct a month_weekday_last is with operator/, e.g., std::chrono::April/std::chrono::Sunday[std::chrono::last]. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
