---
title: "stdchronoyear_month_dayyear_month_day(3)"
name: "stdchronoyear_month_dayyear_month_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_dayyear_month_day/"
---

std::chrono::year_month_day::year_month_day - std::chrono::year_month_day::year_month_day

<h2>Synopsis</h2>

<pre><code>year_month_day() = default;
(1)(since C++ 20)

    constexpr year_month_day(const std::chrono::year &amp;y,

                             const std::chrono::month &amp;m, (2)(since C++ 20)

                                                              const std::chrono::day &amp;d) noexcept;

constexpr year_month_day(const std::chrono::year_month_day_last &amp;ymdl) noexcept;
(since C++ 20)

    constexpr year_month_day(const std::chrono::sys_days &amp;dp) noexcept;
(since C++ 20)

    explicit constexpr year_month_day(const std::chrono::local_days &amp;dp) noexcept;
(since C++ 20)</code></pre> 
Constructs a year_month_day object. 
1) Default constructor leaves the date uninitialized. 
2) Constructs a year_month_day object that stores the year y, month m and day d. 
3) Constructs a year_month_day object that stores the year ymdl.year(), month ymdl.month() and day ymdl.day(). 
4) Constructs a year_month_day object that represent the same date as the one represented by dp. 
5) Constructs a year_month_day object that represent the same date as the one represented by dp, as if by year_month_day(sys_days(dp.time_since_epoch())). 
Constructors (3-4) define implicit conversions from std::chrono::year_month_day_last and std::chrono::sys_days, respectively. 
For any year_month_day object ymd representing a valid date (ymd.ok() == true), converting ymd to sys_days and back yields the same value. 

<h2>Notes</h2>

A year_month_day can also be created by combining one of the partial-date types std::chrono::year_month and std::chrono::month_day with the missing component (day and year, respectively) using operator/. 

<h2>See also</h2>

operator/ conventional syntax for Gregorian calendar date creation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
