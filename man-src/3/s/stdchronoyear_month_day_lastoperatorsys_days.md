---
title: "stdchronoyear_month_day_lastoperatorsys_days(3)"
name: "stdchronoyear_month_day_lastoperatorsys_days"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastoperatorsys_days/"
description: "std::chrono::year_month_day_last::operatorsys_days,std::chrono::year_month_day_last::operatorlocal_days – std::chrono::year_month_day_last::operatorsys_days,std::chrono::year_month_day_last::operat..."
---

<p>std::chrono::year_month_day_last::operatorsys_days,std::chrono::year_month_day_last::operatorlocal_days &#8211; std::chrono::year_month_day_last::operatorsys_days,std::chrono::year_month_day_last::operatorlocal_days</p>
<h2>Synopsis</h2>
<p>constexpr operator std::chrono::sys_days() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
explicit constexpr operator std::chrono::local_days() const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
Converts *this to a std::chrono::time_point representing the same date as this year_month_day_last. This is equivalent to composing a year_month_day from year(), month() and day() and converting that year_month_day to the destination type.<br />
1) Equivalent to std::chrono::sys_days(year()/month()/day())<br />
2) Equivalent to std::chrono::local_days(year()/month()/day()) </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts to a std::chrono::time_point<br />
operator_sys_days <i>(public member function of std::chrono::year_month_day)</i><br />
operator_local_days </p>
