---
title: "stdchronoyear_month_weekdayyear_month_weekday(3)"
name: "stdchronoyear_month_weekdayyear_month_weekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekdayyear_month_weekday/"
---

std::chrono::year_month_weekday::year_month_weekday - std::chrono::year_month_weekday::year_month_weekday

<h2>Synopsis</h2>

<pre><code>year_month_weekday() = default;
(1)(since C++ 20)

    constexpr year_month_weekday(const std::chrono::year &amp;y, const std::chrono::month &amp;m, (2)(since C++ 20)

                                                                                              const std::chrono::weekday_indexed &amp;wdi) noexcept;

constexpr year_month_weekday(const std::chrono::sys_days &amp;dp) noexcept;
(3)(since C++ 20)

    explicit constexpr year_month_weekday(const std::chrono::local_days &amp;dp) noexcept;
(4)(since C++ 20)</code></pre> 
Constructs a year_month_weekday object. 
1) Default constructor leaves the fields uninitialized. 
2) Constructs a year_month_weekday object storing the year y, the month m, the weekday wdi.weekday() and the weekday index wdi.index(). 
3) Constructs a year_month_weekday object corresponding to the date represented by dp. For any year_month_weekday object storing a valid date, converting it to sys_days and back yields the same value. This constructor defines an implicit conversion from sys_days to year_month_weekday. 
4) Constructs a year_month_weekday object corresponding to the date represented by dp. Equivalent to year_month_weekday(sys_days(dp.time_since_epoch())). 

<h2>Notes</h2>

A year_month_weekday can also be created by combining one of the partial-date types std::chrono::year_month and std::chrono::month_weekday with the missing component (indexed weekday and year, respectively) using operator/. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
