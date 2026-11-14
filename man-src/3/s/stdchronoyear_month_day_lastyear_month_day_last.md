---
title: "stdchronoyear_month_day_lastyear_month_day_last(3)"
name: "stdchronoyear_month_day_lastyear_month_day_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastyear_month_day_last/"
---

std::chrono::year_month_day_last::year_month_day_last - std::chrono::year_month_day_last::year_month_day_last

<h2>Synopsis</h2>

<pre><code>constexpr year_month_day_last(const std::chrono::year &amp;y, (since C++ 20)

                                                              const std::chrono::month_day_last &amp;mdl) noexcept;</code></pre> 
Constructs a year_month_day_last object storing the year y and the month mdl.month(). The constructed object represents the last day of that year and month. 

<h2>Notes</h2>

A year_month_day_last can also be created by combining a std::chrono::year_month with std::chrono::last using operator/. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
