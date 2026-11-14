---
title: "stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonthstdchronoyear_month_day_lastdaystdchronoyear_month_day_lastmonth_day_last(3)"
name: "stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonthstdchronoyear_month_day_lastdaystdchronoyear_month_day_lastmonth_day_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonthstdchronoyear_month_day_lastdaystdchronoyear_month_day_lastmonth_day_last/"
description: "std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month,std::chrono::year_month_day_last::day,std::chrono::year_month_day_last::month_day_last – std::chrono::year_month_day_l..."
---

<p>std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month,std::chrono::year_month_day_last::day,std::chrono::year_month_day_last::month_day_last &#8211; std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month,std::chrono::year_month_day_last::day,std::chrono::year_month_day_last::month_day_last</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::year year() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::month month() const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr std::chrono::day day() const noexcept; <code>(3)</code> <i>(since C++20)</i><br />
constexpr std::chrono::month_day_last month_day_last() const noexcept; <code>(4)</code> <i>(since C++20)</i><br />
Retrieves the field values stored in this year_month_day_last object. </p>
<h2>Return values</h2>
<p>1) Returns the stored std::chrono::year value.<br />
2) Returns the stored std::chrono::month value.<br />
3) A std::chrono::day value corresponding to the last day of the stored year and month.<br />
4) A std::chrono::month_day_last constructed from month().</p>
<h2>Notes</h2>
<p>The behavior of <code>(3)</code> when !this-&gt;ok() is not currently defined. It likely will be defined to return some invalid day in that case (such as std::chrono::day<code>(0)</code>). </p>
