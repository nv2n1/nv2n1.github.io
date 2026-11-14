---
title: "stdchronomonth_weekday_lastok(3)"
name: "stdchronomonth_weekday_lastok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_weekday_lastok/"
---

std::chrono::month_weekday_last::ok - std::chrono::month_weekday_last::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the contained month and weekday_last objects are valid. 

<h2>Return value</h2>

month().ok() &amp;&amp; weekday_last().ok() 
