---
title: "stdchronooperatorstdchronooperator-stdchronoweekday(3)"
name: "stdchronooperatorstdchronooperator-stdchronoweekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoweekday/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::weekday) - std::chrono::operator+,std::chrono::operator-(std::chrono::weekday)

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::weekday operator+(const std::chrono::weekday &amp;wd, (1)(since C++ 20)

                                                                             const std::chrono::days &amp;d) noexcept;

constexpr std::chrono::weekday operator+(const std::chrono::days &amp;d, (2)(since C++ 20)

                                                                         const std::chrono::weekday &amp;wd) noexcept;

constexpr std::chrono::weekday operator-(const std::chrono::weekday &amp;wd, (3)(since C++ 20)

                                                                             const std::chrono::days &amp;d) noexcept;

constexpr std::chrono::days operator-(const std::chrono::weekday &amp;wd1, (4)(since C++ 20)

                                                                           const std::chrono::weekday &amp;wd2) noexcept;
1-2) Adds d.count() days to wd. The weekday value held in the result is computed by first evaluating static_cast&lt;long long&gt;(unsigned(wd)) + d.count() and reducing it modulo 7 to an integer in the range [0, 6].

3) Subtracts d.count() days from wd. Equivalent to return wd + -d;

4) If wd1.ok() and wd2.ok() are both true, returns a std::chrono::days value d such that d.count() is in the range [0, 6] and wd2 + d == wd1. Otherwise the returned value is unspecified.
</code></pre>

<h2>Return value</h2>

1-3) A std::chrono::weekday holding a weekday value calculated as described above. 
4) A std::chrono::days representing the distance between wd1 and wd2. 

<h2>Notes</h2>

As long as the computation doesn't overflow, (1-3) always return a valid weekday even if wd.ok() is false. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator++      increments or decrements the weekday

operator++(int) (public member function)

operator--

operator--(int)
adds or subtracts a number of days

operator+=      (public member function)

operator-=




</code></pre>
