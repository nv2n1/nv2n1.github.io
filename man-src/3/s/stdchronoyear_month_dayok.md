---
title: "stdchronoyear_month_dayok(3)"
name: "stdchronoyear_month_dayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_dayok/"
---

std::chrono::year_month_day::ok - std::chrono::year_month_day::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if this year_month_day object represents a valid calendar date. 

<h2>Return value</h2>

true if this year_month_day object represents a valid calendar date, that is, the stored year, month, and day values are all valid and the stored day value is within the number of days in the given year and month. Otherwise false. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;constexpr bool std::chrono::year_month_day::ok() const noexcept { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return year().ok() &amp;&amp; month().ok() &amp;&amp; day().ok() &amp;&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;day() &lt;= (year()/month()/std::chrono::last).day(); 
&nbsp;<wbr>&nbsp;}
