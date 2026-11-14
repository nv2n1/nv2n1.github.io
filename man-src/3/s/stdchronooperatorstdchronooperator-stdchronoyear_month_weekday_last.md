---
title: "stdchronooperatorstdchronooperator-stdchronoyear_month_weekday_last(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear_month_weekday_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear_month_weekday_last/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_weekday_last) - std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_weekday_last)

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::year_month_weekday_last

operator+(const std::chrono::year_month_weekday_last &amp;ymwdl, (since C++ 20)

                                                                 const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_weekday_last

operator+(const std::chrono::months &amp;dm, (since C++ 20)

                                             const std::chrono::year_month_weekday_last &amp;ymwdl) noexcept;

constexpr std::chrono::year_month_weekday_last

operator+(const std::chrono::year_month_weekday_last &amp;ymwdl, (since C++ 20)

                                                                 const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month_weekday_last

operator+(const std::chrono::years &amp;dy, (since C++ 20)

                                            const std::chrono::year_month_weekday_last &amp;ymwdl) noexcept;

constexpr std::chrono::year_month_weekday_last

operator-(const std::chrono::year_month_weekday_last &amp;ymwdl, (since C++ 20)

                                                                 const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_weekday_last

operator-(const std::chrono::year_month_weekday_last &amp;ymwdl, (since C++ 20)

                                                                 const std::chrono::years &amp;dy) noexcept;</code></pre> 
1-2) Adds dm.count() months to the date represented by ymwdl. The result has the same year() and month() as std::chrono::year_month(ymwdl.year(), ymwdl.month()) + dm and the same weekday() as ymwdl. 
3-4) Adds dy.count() years to the date represented by ymwdl. The result is equivalent to std::chrono::year_month_weekday_last(ymwdl.year() + dy, ymwdl.month(), ymwd.weekday_last()). 
5) Subtracts dm.count() months from the date represented by ymwdl. Equivalent to ymwdl+ -dm. 
6) Subtracts dy.count() years from the date represented by ymwdl. Equivalent to ymwdl + -dy. 
