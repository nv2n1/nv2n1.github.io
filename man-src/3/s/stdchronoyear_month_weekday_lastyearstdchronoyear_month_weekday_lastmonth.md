---
title: "stdchronoyear_month_weekday_lastyearstdchronoyear_month_weekday_lastmonth(3)"
name: "stdchronoyear_month_weekday_lastyearstdchronoyear_month_weekday_lastmonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekday_lastyearstdchronoyear_month_weekday_lastmonth/"
---

std::chrono::year_month_weekday_last::year,std::chrono::year_month_weekday_last::month, - std::chrono::year_month_weekday_last::year,std::chrono::year_month_weekday_last::month,

<h2>Synopsis</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::chrono::year_month_weekday_last::weekday_last 
constexpr std::chrono::year year()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i> 
constexpr std::chrono::month month()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i> 
constexpr std::chrono::weekday weekday()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i> 
constexpr std::chrono::weekday_last weekday_last()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i> 
Retrieves the field values stored in this year_month_weekday_last object. 

<h2>Return values</h2>

1)&nbsp;<wbr>Returns the stored std::chrono::year value. 
2)&nbsp;<wbr>Returns the stored std::chrono::month value. 
3)&nbsp;<wbr>Returns the stored std::chrono::weekday value. 
4)&nbsp;<wbr>std::chrono::weekday_last(weekday()).
