---
title: "stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonth(3)"
name: "stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastyearstdchronoyear_month_day_lastmonth/"
description: "std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month, – std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month,"
---

<p>std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month, &#8211; std::chrono::year_month_day_last::year,std::chrono::year_month_day_last::month,</p>
<h2>Synopsis</h2>
<pre><code>constexpr std::chrono::year year() const noexcept;
(1)(since C++ 20)

    constexpr std::chrono::month month() const noexcept;
(2)(since C++ 20)

    constexpr std::chrono::day day() const noexcept;
(3)(since C++ 20)

    constexpr std::chrono::month_day_last month_day_last() const(4)(since C++ 20)

        noexcept;</code></pre>
<p>Retrieves the field values stored in this year_month_day_last object. </p>
<h2>Return values</h2>
<p>1)&nbsp;<wbr>Returns the stored std::chrono::year value.<br />
2)&nbsp;<wbr>Returns the stored std::chrono::month value.<br />
3)&nbsp;<wbr>A std::chrono::day value corresponding to the last day of the stored year and<br />
month.<br />
4)&nbsp;<wbr>A std::chrono::month_day_last constructed from month().</p>
<h2>Notes</h2>
<p>The behavior of&nbsp;<wbr><code>(3)</code>&nbsp;<wbr>when&nbsp;<wbr>!this-&gt;ok()&nbsp;<wbr>is not currently defined. It likely will be<br />
defined to return some invalid day in that case&nbsp;<wbr>(such as std::chrono::day<code>(0)</code>). </p>
