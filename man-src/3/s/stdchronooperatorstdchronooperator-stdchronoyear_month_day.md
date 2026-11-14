---
title: "stdchronooperatorstdchronooperator-stdchronoyear_month_day(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear_month_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear_month_day/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_day) - std::chrono::operator+,std::chrono::operator-(std::chrono::year_month_day)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    constexpr std::chrono::year_month_day operator+(const std::chrono::year_month_day &amp;ymd, (since C++ 20)

                                                                                                const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_day operator+(const std::chrono::months &amp;dm, (since C++ 20)

                                                                                   const std::chrono::year_month_day &amp;ymd) noexcept;

constexpr std::chrono::year_month_day operator+(const std::chrono::year_month_day &amp;ymd, (since C++ 20)

                                                                                            const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month_day operator+(const std::chrono::years &amp;dy, (since C++ 20)

                                                                                  const std::chrono::year_month_day &amp;ymd) noexcept;

constexpr std::chrono::year_month_day operator-(const std::chrono::year_month_day &amp;ymd, (since C++ 20)

                                                                                            const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month_day operator-(const std::chrono::year_month_day &amp;ymd, (since C++ 20)

                                                                                            const std::chrono::years &amp;dy) noexcept;</code></pre> 
1-2) Adds dm.count() months to the date represented by ymd. The result has the same day() as ymd and the same year() and month() as std::chrono::year_month(ymd.year(), ymd.month()) + dm. 
3-4) Adds dy.count() years to the date represented by ymd. The result is equivalent to std::chrono::year_month_day(ymd.year() + dy, ymd.month(), ymd.day(). 
5) Subtracts dm.count() months from the date represented by ymd. Equivalent to ymd + -dm. 
6) Subtracts dy.count() years from the date represented by ymd. Equivalent to ymd + -dy. 

<h2>Notes</h2>

Even if ymd.ok() is true, the resulting year_month_day may not represent a valid date if ymd.day() is 29, 30, or 31. 
