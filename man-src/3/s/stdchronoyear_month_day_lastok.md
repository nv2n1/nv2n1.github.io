---
title: "stdchronoyear_month_day_lastok(3)"
name: "stdchronoyear_month_day_lastok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastok/"
---

std::chrono::year_month_day_last::ok - std::chrono::year_month_day_last::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if *this represents a valid date. Because a year_month_day_last represents the last day of a particular month, it represents a valid date as long as the year and month are valid. 

<h2>Return value</h2>

year().ok() &amp;&amp; month().ok() 
