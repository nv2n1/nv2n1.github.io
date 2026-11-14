---
title: "stdchronotime_of_daytime_of_day(3)"
name: "stdchronotime_of_daytime_of_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_of_daytime_of_day/"
---

std::chrono::time_of_day&lt;Duration&gt;::time_of_day - std::chrono::time_of_day&lt;Duration&gt;::time_of_day

<h2>Synopsis</h2>

<pre><code>time_of_day() = default;                                           (1)

explicit constexpr time_of_day(precision since_midnight) noexcept; (2)</code></pre> 
Constructs a time_of_day object. 
1) Default constructor leaves the object uninitialized. 
2) Constructs a time_of_day object in 24 hour format corresponding to since_midnight after 00:00:00. As applicable: 
* hours() returns the integral number of hours since_midnight is after 00:00:00. 
* minutes() returns the integral number of minutes since_midnight is after (00:00:00 + hours()). 
* seconds() returns the integral number of seconds since_midnight is after (00:00:00 + hours() + minutes()). 
* subseconds() returns the integral number of fractional seconds since_midnight is after (00:00:00 + hours() + minutes() + seconds()). 
