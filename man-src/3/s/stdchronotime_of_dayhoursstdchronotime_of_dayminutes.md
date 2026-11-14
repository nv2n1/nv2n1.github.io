---
title: "stdchronotime_of_dayhoursstdchronotime_of_dayminutes(3)"
name: "stdchronotime_of_dayhoursstdchronotime_of_dayminutes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_of_dayhoursstdchronotime_of_dayminutes/"
description: "std::chrono::time_of_day<Duration>::hours,std::chrono::time_of_day<Duration>::minutes, – std::chrono::time_of_day<Duration>::hours,std::chrono::time_of_day<Duration>::minutes,"
---

<p>std::chrono::time_of_day&lt;Duration&gt;::hours,std::chrono::time_of_day&lt;Duration&gt;::minutes, &#8211; std::chrono::time_of_day&lt;Duration&gt;::hours,std::chrono::time_of_day&lt;Duration&gt;::minutes,</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::chrono::time_of_day&lt;Duration&gt;::subseconds<br />
member of all specializations<br />
constexpr std::chrono::hours hours()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code><br />
member of all specializations except time_of_day&lt;std::chrono::hours&gt;<br />
constexpr std::chrono::minutes minutes()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code><br />
member only of the time_of_day&lt;std::chrono::seconds&gt;&nbsp;<wbr>and<br />
time_of_day&lt;std::chrono::duration&lt;Rep, Period&gt;&gt;&nbsp;<wbr>specializations<br />
constexpr std::chrono::seconds seconds()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(3)</code><br />
member only of the time_of_day&lt;std::chrono::duration&lt;Rep, Period&gt;&gt;&nbsp;<wbr>partial<br />
specialization<br />
constexpr precision subseconds()&nbsp;<wbr>const noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code><br />
Obtains the components of the stored&nbsp;<wbr>&quot;broken down&quot;&nbsp;<wbr>time. </p>
<h2>Return value</h2>
<p>Let since_midnight be the stored duration:<br />
1)&nbsp;<wbr>the integral number of hours since_midnight is after 00:00:00.<br />
2)&nbsp;<wbr>the integral number of minutes since_midnight is after&nbsp;<wbr>(00:00:00&nbsp;<wbr>+&nbsp;<wbr>hours()).<br />
3)&nbsp;<wbr>the integral number of seconds since_midnight is after&nbsp;<wbr>(00:00:00&nbsp;<wbr>+&nbsp;<wbr>hours()&nbsp;<wbr>+<br />
minutes()).<br />
4)&nbsp;<wbr>the integral number of fractional seconds since_midnight is after&nbsp;<wbr>(00:00:00&nbsp;<wbr>+<br />
hours()&nbsp;<wbr>+&nbsp;<wbr>minutes()&nbsp;<wbr>+&nbsp;<wbr>seconds()). </p>
