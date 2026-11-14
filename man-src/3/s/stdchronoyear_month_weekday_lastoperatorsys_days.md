---
title: "stdchronoyear_month_weekday_lastoperatorsys_days(3)"
name: "stdchronoyear_month_weekday_lastoperatorsys_days"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekday_lastoperatorsys_days/"
description: "std::chrono::year_month_weekday_last::operatorsys_days,std::chrono::year_month_weekday_last::operatorlocal_days – std::chrono::year_month_weekday_last::operatorsys_days,std::chrono::year_month_week..."
---

<p>std::chrono::year_month_weekday_last::operatorsys_days,std::chrono::year_month_weekday_last::operatorlocal_days &#8211; std::chrono::year_month_weekday_last::operatorsys_days,std::chrono::year_month_weekday_last::operatorlocal_days</p>
<h2>Synopsis</h2>
<p>constexpr operator std::chrono::sys_days() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
explicit constexpr operator std::chrono::local_days() const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
Converts *this to a std::chrono::time_point representing the same date as this year_month_weekday_last.<br />
1) If ok() is true, returns a sys_days that represents the last weekday() of the year() and month(). Otherwise, the returned value is unspecified.<br />
2) Same as <code>(1)</code>, but returns local_days instead of sys_days. Equivalent to local_days(sys_days(*this).time_since_epoch()). </p>
