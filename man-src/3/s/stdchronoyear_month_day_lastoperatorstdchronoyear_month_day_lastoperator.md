---
title: "stdchronoyear_month_day_lastoperatorstdchronoyear_month_day_lastoperator(3)"
name: "stdchronoyear_month_day_lastoperatorstdchronoyear_month_day_lastoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_lastoperatorstdchronoyear_month_day_lastoperator/"
---

std::chrono::year_month_day_last::operator+=,std::chrono::year_month_day_last::operator-= - std::chrono::year_month_day_last::operator+=,std::chrono::year_month_day_last::operator-=

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::year_month_day_last &amp;operator+=(const std::chrono::years &amp;dy) const noexcept;
(1)(since C++ 20)

    constexpr std::chrono::year_month_day_last &amp;
    operator+=(const std::chrono::months &amp;dm) const noexcept;
(2)(since C++ 20)

    constexpr std::chrono::year_month_day_last &amp;
    operator-=(const std::chrono::years &amp;dy) const noexcept;
(3)(since C++ 20)

    constexpr std::chrono::year_month_day_last &amp;
    operator-=(const std::chrono::months &amp;dm) const noexcept; (4) (since C++20)
Modifies the time point *this represents by the duration dy or dm.

1) Equivalent to *this = *this + dy;

2) Equivalent to *this = *this + dm;

3) Equivalent to *this = *this - dy;

4) Equivalent to *this = *this - dm;
</code></pre>

<h2>Notes</h2>

Durations that are convertible to std::chrono::months, but not std::chrono::years, can be directly added to or subtracted from a year_month_day_last. Durations convertible to std::chrono::years cannot because such durations are also convertible to std::chrono::months, resulting in an ambiguity: <pre><code>using namespace std::chrono;
using decades = duration&lt;int, std::ratio_multiply&lt;std::ratio&lt;10&gt;, years::period&gt;&gt;;

using kilomonths = duration&lt;int, std::ratio_multiply&lt;std::kilo, months::period&gt;&gt;;
auto ymdl = 2001y / April / last;

ymdl += decades{1}; // error, ambiguous

ymdl += kilomonths{1}; // OK
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a year_month_day_last and some number of years or months 
operator+ <i>(public member function)</i> 
operator- 
