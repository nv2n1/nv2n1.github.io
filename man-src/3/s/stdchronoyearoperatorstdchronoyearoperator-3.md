---
title: "stdchronoyearoperatorstdchronoyearoperator-3(3)"
name: "stdchronoyearoperatorstdchronoyearoperator-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearoperatorstdchronoyearoperator-3/"
---

std::chrono::year::operator+=,std::chrono::year::operator-= - std::chrono::year::operator+=,std::chrono::year::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::year &amp;operator+=(const std::chrono::years &amp;y) noexcept;
(1)(since C++ 20)

    constexpr std::chrono::year &amp;
    operator-=(const std::chrono::years &amp;y) noexcept; (2) (since C++20)
Adds or subtracts y.count() years from the year value.

1) Equivalent to *this = *this + y;

2) Equivalent to *this = *this - y;
</code></pre>

<h2>Return value</h2>

A reference to this year after modification. 

<h2>Notes</h2>

If the result would be outside the range [-32767, 32767], the actual stored value is unspecified. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

operator++ increments or decrements the year 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on years 
operator+ <i>(public member function)</i> 
operator- 
