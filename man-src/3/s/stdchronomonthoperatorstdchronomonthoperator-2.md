---
title: "stdchronomonthoperatorstdchronomonthoperator-2(3)"
name: "stdchronomonthoperatorstdchronomonthoperator-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonthoperatorstdchronomonthoperator-2/"
---

std::chrono::month::operator+=,std::chrono::month::operator-= - std::chrono::month::operator+=,std::chrono::month::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::month &amp;operator+=(const std::chrono::months &amp;m) noexcept;
(1)(since C++ 20)

    constexpr std::chrono::month &amp;
    operator+=(const std::chrono::months &amp;m) noexcept; (2) (since C++20)
Adds or subtracts m.count() from the month value, reducing the result modulo 12 to an integer in the range [1, 12].

1) Performs *this = *this + m;

2) Performs *this = *this - m;
</code></pre>

<h2>Return value</h2>

A reference to this month after modification. 

<h2>Notes</h2>

After a call to one of these functions, ok() is always true if no overflow occurred during the operation. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

operator++ increments or decrements the month 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on months 
operator+ <i>(function)</i> 
operator- 
