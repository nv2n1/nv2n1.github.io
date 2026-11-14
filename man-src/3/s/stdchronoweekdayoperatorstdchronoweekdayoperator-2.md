---
title: "stdchronoweekdayoperatorstdchronoweekdayoperator-2(3)"
name: "stdchronoweekdayoperatorstdchronoweekdayoperator-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekdayoperatorstdchronoweekdayoperator-2/"
---

std::chrono::weekday::operator+=,std::chrono::weekday::operator-= - std::chrono::weekday::operator+=,std::chrono::weekday::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::weekday &amp;operator+=(const std::chrono::days &amp;d) noexcept;
(1)(since C++ 20)

    constexpr std::chrono::weekday &amp;
    operator-=(const std::chrono::days &amp;d) noexcept; (2) (since C++20)
Adds or subtracts d.count() from the weekday value, reducing the result modulo 7 to an integer in the range [0, 6].

1) Performs *this = *this + d;

2) Performs *this = *this - d;
</code></pre>

<h2>Return value</h2>

A reference to this weekday after modification. 

<h2>Notes</h2>

After a call to one of these functions, ok() is always true if no overflow occurred during the operation. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

operator++ increments or decrements the weekday 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on weekdays 
operator+ <i>(function)</i> 
operator- 
