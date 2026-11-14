---
title: "stdchronomonth_dayok(3)"
name: "stdchronomonth_dayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_dayok/"
---

std::chrono::month_day::ok - std::chrono::month_day::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Determines whether this month_day stores a valid month-day combination. 
The combination is valid if month() represents a valid month (month().ok() == true), unsigned{day()} &gt;= 1, and unsigned{day()} &lt;= D, where D is the number of days in the month represented by month(). The number of days in February is considered to be 29. 

<h2>Return value</h2>

true if the month and day combination is valid, otherwise false. 
