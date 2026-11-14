---
title: "stdchronoyear_month_weekday_lastyear_month_weekday_last(3)"
name: "stdchronoyear_month_weekday_lastyear_month_weekday_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekday_lastyear_month_weekday_last/"
---

std::chrono::year_month_weekday_last::year_month_weekday_last - std::chrono::year_month_weekday_last::year_month_weekday_last

<h2>Synopsis</h2>

<pre><code>constexpr year_month_weekday_last(const std::chrono::year &amp;y, const std::chrono::month &amp;m, (since C++ 20)

                                                                                               const chrono::weekday_last &amp;wdl) noexcept;</code></pre> 
Constructs a year_month_weekday_last object storing the year y, the month m, and the weekday wdl.weekday(). The constructed object represents the last weekday of that year and month. 

<h2>Notes</h2>

A year_month_weekday_last can also be created by combining one of the partial-date types std::chrono::year_month and std::chrono::month_weekday_last with the missing component (weekday_last and year, respectively) using operator/. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
