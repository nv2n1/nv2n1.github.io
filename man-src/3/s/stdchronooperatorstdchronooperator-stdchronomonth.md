---
title: "stdchronooperatorstdchronooperator-stdchronomonth(3)"
name: "stdchronooperatorstdchronooperator-stdchronomonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronomonth/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::month) - std::chrono::operator+,std::chrono::operator-(std::chrono::month)

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::month operator+(const std::chrono::month &amp;m, (1)(since C++ 20)

                                                                        const std::chrono::months &amp;ms) noexcept;

constexpr std::chrono::month operator+(const std::chrono::months &amp;ms, (2)(since C++ 20)

                                                                          const std::chrono::month &amp;m) noexcept;

constexpr std::chrono::month operator-(const std::chrono::month &amp;m, (3)(since C++ 20)

                                                                        const std::chrono::months &amp;ms) noexcept;

constexpr std::chrono::months operator-(const std::chrono::month &amp;m1, (4)(since C++ 20)

                                                                          const std::chrono::month &amp;m2) noexcept;
1-2) Adds ms.count() months to m. The month value held in the result is computed by first evaluating static_cast&lt;long long&gt;(unsigned(m)) + (ms.count() - 1), reducing it modulo 12 to an integer in the range [0, 11], and then adding 1.

3) Subtracts ms.count() months from m and returns the result. Equivalent to return m + -ms;

4) If m1.ok() and m2.ok() are both true, returns a std::chrono::months value m such that m.count() is in the range [0, 11] and m2 + m == m1. Otherwise the returned value is unspecified.
</code></pre>

<h2>Return value</h2>

1-3) A std::chrono::month holding a month value calculated as described above. 
4) A std::chrono::months representing the distance between m1 and m2. 

<h2>Notes</h2>

As long as the computation doesn't overflow, (1-3) always return a valid month even if m.ok() is false. 
The result of subtracting two month values is a duration of type std::chrono::months. That duration unit represents the length of the average Gregorian month, and the resulting duration bears no relationship to the number of days in the particular months represented by the operands. For example, std::chrono::seconds(std::chrono::April - std::chrono::March) is not the number of seconds in March (2678400s), but 2629746s (30.436875 days). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator++      increments or decrements the month

operator++(int) (public member function)

operator--

operator--(int)
adds or subtracts a number of months

operator+=      (public member function)

operator-=




</code></pre>
