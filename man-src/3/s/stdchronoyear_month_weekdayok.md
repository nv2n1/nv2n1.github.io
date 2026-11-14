---
title: "stdchronoyear_month_weekdayok(3)"
name: "stdchronoyear_month_weekdayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekdayok/"
---

std::chrono::year_month_weekday::ok - std::chrono::year_month_weekday::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if this year_month_weekday object represents a valid date. 

<h2>Return value</h2>

true if this year_month_weekday object represents a valid date, that is, year().ok() &amp;&amp; month().ok() &amp;&amp; weekday_indexed().ok() is true and there are at least index() weekday()s in the specified year and month. Otherwise false. 
