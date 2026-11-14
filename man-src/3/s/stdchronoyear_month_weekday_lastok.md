---
title: "stdchronoyear_month_weekday_lastok(3)"
name: "stdchronoyear_month_weekday_lastok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekday_lastok/"
---

std::chrono::year_month_weekday_last::ok - std::chrono::year_month_weekday_last::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if this object represents a valid date. Since a year_month_weekday_last represents the last weekday of a particular month, it is valid as long as the year, month and weekday are valid. 

<h2>Return value</h2>

year().ok() &amp;&amp; month().ok() &amp;&amp; weekday().ok() 
