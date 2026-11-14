---
title: "stdchronooperatorstdchronooperator-stdchronoyear_month_day_last(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear_month_day_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear_month_day_last/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_day_last) - std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_day_last)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    constexpr std::chrono::year_month_day_last(since C++ 20)

    operator+(const std::chrono::year_month_day_last &amp;ymdl, const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_day_last(since C++ 20)

operator+(const std::chrono::months &amp;dm, const std::chrono::year_month_day_last &amp;ymdl) noexcept;

constexpr std::chrono::year_month_day_last(since C++ 20)

operator+(const std::chrono::year_month_day_last &amp;ymdl, const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month_day_last(since C++ 20)

operator+(const std::chrono::years &amp;dy, const std::chrono::year_month_day_last &amp;ymdl) noexcept;

constexpr std::chrono::year_month_day_last(since C++ 20)

operator-(const std::chrono::year_month_day_last &amp;ymdl, const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_day_last(since C++ 20)

operator-(const std::chrono::year_month_day_last &amp;ymdl, const std::chrono::years &amp;dy) noexcept;</code></pre> 
1-2) Adds dm.count() months to the date represented by ymdl. The result has the same year() and month() as std::chrono::year_month(ymdl.year(), ymdl.month()) + dm. 
3-4) Adds dy.count() years to the date represented by ymdl. The result is equivalent to std::chrono::year_month_day_last(ymdl.year() + dy, ymdl.month_day_last()). 
5) Subtracts dm.count() months from the date represented by ymdl. Equivalent to ymdl + -dm. 
6) Subtracts dy.count() years from the date represented by ymdl. Equivalent to ymdl + -dy. 
