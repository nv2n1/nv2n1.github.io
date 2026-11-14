---
title: "stdchronomonth_weekdayok(3)"
name: "stdchronomonth_weekdayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_weekdayok/"
---

std::chrono::month_weekday::ok - std::chrono::month_weekday::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the contained month and weekday_indexed objects are valid. 

<h2>Return value</h2>

month().ok() &amp;&amp; weekday_indexed().ok() 
