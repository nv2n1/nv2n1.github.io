---
title: "stdchronoyear_month_weekdayoperatorsys_days(3)"
name: "stdchronoyear_month_weekdayoperatorsys_days"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekdayoperatorsys_days/"
description: "std::chrono::year_month_weekday::operatorsys_days,std::chrono::year_month_weekday::operatorlocal_days – std::chrono::year_month_weekday::operatorsys_days,std::chrono::year_month_weekday::operatorlo..."
---

<p>std::chrono::year_month_weekday::operatorsys_days,std::chrono::year_month_weekday::operatorlocal_days &#8211; std::chrono::year_month_weekday::operatorsys_days,std::chrono::year_month_weekday::operatorlocal_days</p>
<h2>Synopsis</h2>
<p>constexpr operator std::chrono::sys_days() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
explicit constexpr operator std::chrono::local_days() const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
Converts *this to a std::chrono::time_point representing the same date as this year_month_weekday.<br />
1) If year().ok() &amp;&amp; month().ok() &amp;&amp; weekday().ok():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If index() == 0, returns a sys_days that represents the date 7 days prior to the first weekday() of the year and month.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Else, returns a sys_days that represents the date (index() &#8211; 1) * 7 days after the first weekday() of the year and month.<br />
Otherwise, the returned value is unspecified.<br />
2) Same as <code>(1)</code>, but returns local_days instead of sys_days. Equivalent to local_days(sys_days(*this).time_since_epoch()). </p>
