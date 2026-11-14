---
title: "stdchronomonth_day_lastmonth_day_last(3)"
name: "stdchronomonth_day_lastmonth_day_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_day_lastmonth_day_last/"
---

std::chrono::month_day_last::month_day_last - std::chrono::month_day_last::month_day_last

<h2>Synopsis</h2>

explicit constexpr month_day_last(const std::chrono::month&amp; m) noexcept; <i>(since C++20)</i> 
Constructs a month_day_last object that represents the last day of the month m. 

<h2>Notes</h2>

A more convenient way to construct a month_day_last is with operator/, e.g., std::chrono::April/std::chrono::last. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
