---
title: "stdchronooperatorstdchronooperator-stdchronoyear_month_weekday(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear_month_weekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear_month_weekday/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_weekday) - std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_weekday)

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::year_month_weekday(1)(since C++ 20)

operator+(const std::chrono::year_month_weekday &amp;ymwd, const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_weekday(2)(since C++ 20)

operator+(const std::chrono::months &amp;dm, const std::chrono::year_month_weekday &amp;ymwd) noexcept;

constexpr std::chrono::year_month_weekday(3)(since C++ 20)

operator+(const std::chrono::year_month_weekday &amp;ymwd, const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month_weekday(4)(since C++ 20)

operator+(const std::chrono::years &amp;dy, const std::chrono::year_month_weekday &amp;ymwd) noexcept;

constexpr std::chrono::year_month_weekday(5)(since C++ 20)

operator-(const std::chrono::year_month_weekday &amp;ymwd, const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_weekday(6)(since C++ 20)

operator-(const std::chrono::year_month_weekday &amp;ymwd, const std::chrono::years &amp;dy) noexcept;</code></pre> 
1-2) Adds dm.count() months to the date represented by ymwd. The result has the same year() and month() as std::chrono::year_month(ymwd.year(), ymwd.month()) + dm and the same weekday() and index() as ymwd. 
3-4) Adds dy.count() years to the date represented by ymwd. The result is equivalent to std::chrono::year_month_weekday(ymwd.year() + dy, ymwd.month(), ymwd.weekday_indexed()). 
5) Subtracts dm.count() months from the date represented by ymwd. Equivalent to ymwd + -dm. 
6) Subtracts dy.count() years from the date represented by ymwd. Equivalent to ymwd + -dy. 

<h2>Notes</h2>

Even if ymwd.ok() is true, the resulting year_month_weekday may not represent a valid date if ymwd.index() is 5. 
