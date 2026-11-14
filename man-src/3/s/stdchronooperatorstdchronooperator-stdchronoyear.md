---
title: "stdchronooperatorstdchronooperator-stdchronoyear(3)"
name: "stdchronooperatorstdchronooperator-stdchronoyear"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoyear/"
description: "std::chrono::operator+,std::chrono::operator-(std::chrono::year) – std::chrono::operator+,std::chrono::operator-(std::chrono::year)"
---

<p>std::chrono::operator+,std::chrono::operator-(std::chrono::year) &#8211; std::chrono::operator+,std::chrono::operator-(std::chrono::year)</p>
<h2>Synopsis</h2>
<pre><code>constexpr std::chrono::year operator+(const std::chrono::year &amp;y, (1)(since C++ 20)

                                                                      const std::chrono::years &amp;ys) noexcept;

constexpr std::chrono::year operator+(const std::chrono::years &amp;ys, (2)(since C++ 20)

                                                                        const std::chrono::year &amp;y) noexcept;

constexpr std::chrono::year operator-(const std::chrono::year &amp;y, (3)(since C++ 20)

                                                                      const std::chrono::years &amp;ys) noexcept;

constexpr std::chrono::years operator-(const std::chrono::year &amp;y1, (4)(since C++ 20)

                                                                        const std::chrono::year &amp;y2) noexcept;</code></pre>
<p>1-2) Adds ys.count() years to y.<br />
3) Subtracts ys.count() years from y.<br />
4) Returns the difference in years between y1 and y2. </p>
<h2>Return value</h2>
<p>1-2) std::chrono::year(int(y) + ys.count())<br />
3) std::chrono::year(int(y) &#8211; ys.count())<br />
4) std::chrono::years(int(y1) &#8211; int(y2)) </p>
<h2>Notes</h2>
<p>If the resulting year value for (1-3) is outside the range [-32767,32767], the actual value stored is unspecified.<br />
The result of subtracting two year values is a duration of type std::chrono::years. This duration unit represents the length of the average Gregorian year, and the resulting duration bears no relationship to the number of days in the particular years represented by the operands. For example, the result of 2018y &#8211; 2017y is <a href="/docs/linux/man/1-std--chrono--years/">std::chrono::years</a><code>(1)</code>, which represents 365.2425 days, not 365 days. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<pre><code>operator++      increments or decrements the month

operator++(int) (public member function of std::chrono::month)

operator--

operator--(int)
adds or subtracts a number of months

operator+=      (public member function of std::chrono::month)

operator-=




</code></pre>
