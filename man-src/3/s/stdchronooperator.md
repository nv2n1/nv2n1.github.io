---
title: "stdchronooperator(3)"
name: "stdchronooperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperator/"
---

std::chrono::operator==,!=,&lt;,&lt;=,&gt;,&gt;=(std::chrono::year_month_day_last) - std::chrono::operator==,!=,&lt;,&lt;=,&gt;,&gt;=(std::chrono::year_month_day_last)

<h2>Synopsis</h2>

<pre><code>constexpr bool operator==(const std::chrono::year_month_day_last &amp;x, (1)(since C++ 20)

                                                                         const std::chrono::year_month_day_last &amp;y) noexcept;

constexpr bool operator!=(const std::chrono::year_month_day_last &amp;x, (2)(since C++ 20)

                                                                         const std::chrono::year_month_day_last &amp;y) noexcept;

constexpr bool operator&lt;(const std::chrono::year_month_day_last &amp;x, (3)(since C++ 20)

                                                                        const std::chrono::year_month_day_last &amp;y) noexcept;

constexpr bool operator&gt;(const std::chrono::year_month_day_last &amp;x, (4)(since C++ 20)

                                                                        const std::chrono::year_month_day_last &amp;y) noexcept;

constexpr bool operator&lt;=(const std::chrono::year_month_day_last &amp;x, (5)(since C++ 20)

                                                                         const std::chrono::year_month_day_last &amp;y) noexcept;

constexpr bool operator&gt;=(const std::chrono::year_month_day_last &amp;x, (6)(since C++ 20)

                                                                         const std::chrono::year_month_day_last &amp;y) noexcept;</code></pre> 
Compares the two year_month_day_last objects x and y. This is a lexicographical comparison: the year() is compared first, then month(). 

<h2>Return value</h2>

1) x.year() == y.year() &amp;&amp; x.month() == y.month() 
2) !(x == y) 
3) If x.year() != y.year(), x.year() &lt; y.year(); otherwise, x.month() &lt; y.month(). 
4) y &lt; x 
5) !(y &lt; x) 
6) !(x &lt; y) 

<h2>Notes</h2>

If both x and y represent valid dates (x.ok() &amp;&amp; y.ok() == true), the result of the lexicographical comparison is consistent with the calendar order. 
