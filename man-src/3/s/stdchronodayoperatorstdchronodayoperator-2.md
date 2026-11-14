---
title: "stdchronodayoperatorstdchronodayoperator-2(3)"
name: "stdchronodayoperatorstdchronodayoperator-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronodayoperatorstdchronodayoperator-2/"
---

std::chrono::day::operator+=,std::chrono::day::operator-= - std::chrono::day::operator+=,std::chrono::day::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::day &amp;operator+=(const std::chrono::days &amp;d) noexcept;
(1)(since C++ 20)

    constexpr std::chrono::day &amp;
    operator-=(const std::chrono::days &amp;d) noexcept; (2) (since C++20)
Adds or subtracts d.count() days from the day value.

1) Equivalent to *this = *this + d;

2) Equivalent to *this = *this - d;
</code></pre>

<h2>Return value</h2>

A reference to this day after modification 

<h2>Notes</h2>

If the result would be outside the range [0, 255], the actual stored value is unspecified. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

operator++ increments or decrements the day 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a number of days and a day, or find the difference between two days 
operator+ <i>(function)</i> 
operator- 
