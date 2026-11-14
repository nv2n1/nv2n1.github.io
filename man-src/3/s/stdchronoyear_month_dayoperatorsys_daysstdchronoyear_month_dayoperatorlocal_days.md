---
title: "stdchronoyear_month_dayoperatorsys_daysstdchronoyear_month_dayoperatorlocal_days(3)"
name: "stdchronoyear_month_dayoperatorsys_daysstdchronoyear_month_dayoperatorlocal_days"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_dayoperatorsys_daysstdchronoyear_month_dayoperatorlocal_days/"
description: "std::chrono::year_month_day::operatorsys_days,std::chrono::year_month_day::operatorlocal_days – std::chrono::year_month_day::operatorsys_days,std::chrono::year_month_day::operatorlocal_days"
---

<p>std::chrono::year_month_day::operatorsys_days,std::chrono::year_month_day::operatorlocal_days &#8211; std::chrono::year_month_day::operatorsys_days,std::chrono::year_month_day::operatorlocal_days</p>
<h2>Synopsis</h2>
<p>constexpr operator std::chrono::sys_days() const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
explicit constexpr operator std::chrono::local_days() const noexcept; <code>(2)</code> <i>(since C++20)</i> </p>
<pre><code>Converts *this to a std::chrono::time_point representing the same date as this year_month_day.

1) If ok() is true, the return value holds a count of days from the std::chrono::system_clock epoch (1970-01-01) to *this. The result is negative if *this represent a date prior to it.

Otherwise, if the stored year and month are valid (year().ok() &amp;&amp; month().ok() is true), then the returned value is sys_days(year()/month()/1d) + (day() - 1d).

Otherwise (if year().ok() &amp;&amp; month().ok() is false), the return value is unspecified.

A sys_days in the range [std::chrono::days{-12687428}, std::chrono::days{11248737}], when converted to year_month_day and back, yields the same value.

2) Same as (1) but returns local_days instead. Equivalent to return local_days(sys_days(*this).time_since_epoch());
.
</code></pre>
<h2>Notes</h2>
<p>Converting to sys_days and back can be used to normalize a year_month_day that contains an invalid day but a valid year and month: using namespace std::chrono;</p>
<p>constexpr year_month_day normalize(year_month_day ymd)<br />
{<br />
    ymd += months{0};     // normalizes year and month<br />
    return sys_days{ymd}; // normalizes day<br />
}</p>
<p>static_assert(normalize(2017y / 33 / 59) == 2019y / 10 / 29);</p>
<p>Normalizing the year and month can be done by adding (or subtracting) zero std::chrono::months: </p>
<pre><code>using namespace std::chrono;

constexpr year_month_day normalize(year_month_day ymd)
{
    ymd += months{0};     // normalizes year and month
    return sys_days{ymd}; // normalizes day
}

static_assert(normalize(2017y / 33 / 59) == 2019y / 10 / 29);
</code></pre>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
