---
title: "stdchronoyear_monthoperatorstdchronoyear_monthoperator(3)"
name: "stdchronoyear_monthoperatorstdchronoyear_monthoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_monthoperatorstdchronoyear_monthoperator/"
---

std::chrono::year_month::operator+=,std::chrono::year_month::operator-= - std::chrono::year_month::operator+=,std::chrono::year_month::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::year_month &amp;operator+=(const std::chrono::years &amp;dy) const noexcept;
(1)(since C++ 20)

    constexpr std::chrono::year_month &amp;
    operator+=(const std::chrono::months &amp;dm) const noexcept;
(2)(since C++ 20)

    constexpr std::chrono::year_month &amp;
    operator-=(const std::chrono::years &amp;dy) const noexcept;
(3)(since C++ 20)

    constexpr std::chrono::year_month &amp;
    operator-=(const std::chrono::months &amp;dm) const noexcept; (4) (since C++20)
Modifies the time point *this represents by the duration dy or dm.

1) Equivalent to *this = *this + dy;

2) Equivalent to *this = *this + dm;

3) Equivalent to *this = *this - dy;

4) Equivalent to *this = *this - dm;
</code></pre>

<h2>Notes</h2>

Durations that are convertible to std::chrono::months, but not std::chrono::years, can be directly added to or subtracted from a year_month. Durations convertible to std::chrono::years cannot because such durations are also convertible to std::chrono::months, resulting in an ambiguity: <pre><code>using namespace std::chrono;
using decades = duration&lt;int, std::ratio_multiply&lt;std::ratio&lt;10&gt;, years::period&gt;&gt;;

using kilomonths = duration&lt;int, std::ratio_multiply&lt;std::kilo, months::period&gt;&gt;;
auto ym = 2001y / April;

ym += decades{1}; // error, ambiguous

ym += kilomonths{1}; // OK
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on year_month 
operator+ <i>(function)</i> 
operator- 
