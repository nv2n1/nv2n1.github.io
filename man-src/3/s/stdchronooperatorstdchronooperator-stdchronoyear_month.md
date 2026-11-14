---
title: "stdchronooperatorstdchronooperator-stdchronoyear_month(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear_month"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear_month/"
description: "std::chrono::operator+,std::chrono::operator-(std::chrono::year_month) – std::chrono::operator+,std::chrono::operator-(std::chrono::year_month)"
---

<p>std::chrono::operator+,std::chrono::operator-(std::chrono::year_month) &#8211; std::chrono::operator+,std::chrono::operator-(std::chrono::year_month)</p>
<h2>Synopsis</h2>
<pre><code>constexpr std::chrono::year_month operator+(const std::chrono::year_month &amp;ym, (1)(since C++ 20)

                                                                                   const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month operator+(const std::chrono::years &amp;dy, (2)(since C++ 20)

                                                                              const std::chrono::year_month &amp;ym) noexcept;

constexpr std::chrono::year_month operator+(const std::chrono::year_month &amp;ym, (3)(since C++ 20)

                                                                                   const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::year_month operator+(const std::chrono::months &amp;dm, (4)(since C++ 20)

                                                                               const std::chrono::year_month &amp;ym) noexcept;

constexpr std::chrono::year_month operator-(const std::chrono::year_month &amp;ym, (5)(since C++ 20)

                                                                                   const std::chrono::years &amp;dy) noexcept;

constexpr std::chrono::year_month operator-(const std::chrono::year_month &amp;ym, (6)(since C++ 20)

                                                                                   const std::chrono::months &amp;dm) noexcept;

constexpr std::chrono::months operator-(const std::chrono::year_month &amp;ym1, (7)(since C++ 20)

                                                                                const std::chrono::year_month &amp;ym2) noexcept;</code></pre>
<p>1-2) Adds dy.count() years to ym.<br />
3-4) Adds dm.count() months to ym.<br />
5) Subtracts dy.count() years from ym.<br />
6) Subtracts dm.count() months from ym.<br />
7) Returns the difference in months between the two time points represented by ym1 and ym2. </p>
<h2>Return value</h2>
<p>1-2) std::chrono::year_month(ym.year() + dy, ym.month())<br />
3-4) A year_month value z such that z &#8211; ym == dm and z.ok() == true.<br />
5) ym + -dy<br />
5) ym + -dm<br />
7) ym1.year() &#8211; ym2.year() + std::chrono::months(int(unsigned(ym1.month())) &#8211; int(unsigned(ym2.month()))) </p>
<h2>Notes</h2>
<p>The result of subtracting two year_month values is a duration of type std::chrono::months. This duration unit represents the length of the average Gregorian month (30.436875 days), and the resulting duration bears no relationship to the actual number of days in the time period at issue. For example, the result of 2017y/3 &#8211; 2017y/2 is <a href="/docs/linux/man/1-std--chrono--months/">std::chrono::months</a><code>(1)</code>, even though February 2017 only contains 28 days.<br />
Durations that are convertible to std::chrono::months, but not std::chrono::years, can be directly added to or subtracted from a year_month. Durations convertible to std::chrono::years cannot because such durations are also convertible to std::chrono::months, resulting in an ambiguity: using namespace std::chrono;<br />
using decades = duration&lt;int, std::ratio_multiply&lt;std::ratio&lt;10&gt;, years::period&gt;&gt;;</p>
<p>using kilomonths = duration&lt;int, std::ratio_multiply&lt;std::kilo, months::period&gt;&gt;;<br />
auto ym = 2001y / April;</p>
<p>ym = ym + decades{1}; // error, ambiguous</p>
<p>ym = ym + kilomonths{1}; // OK</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<pre><code>modifies the year_month by some number of months or years

operator+= (public member function)

operator-=




</code></pre>
