---
title: "stdchronodayoperatorstdchronodayoperator(3)"
name: "stdchronodayoperatorstdchronodayoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronodayoperatorstdchronodayoperator/"
description: "std::chrono::day::operator++,std::chrono::day::operator– – std::chrono::day::operator++,std::chrono::day::operator–"
---

<p>std::chrono::day::operator++,std::chrono::day::operator&#8211; &#8211; std::chrono::day::operator++,std::chrono::day::operator&#8211;</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::day&amp; operator++() noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::day operator++(int) noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr std::chrono::day&amp; operator&#8211;() noexcept; <code>(3)</code> <i>(since C++20)</i><br />
constexpr std::chrono::day operator&#8211;(int) noexcept; <code>(4)</code> <i>(since C++20)</i> </p>
<pre><code>Adds or subtracts 1 from the day value.

1-2) Performs *this += std::chrono::days{1};

3-4) Performs *this -= std::chrono::days{1};
</code></pre>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1,3) a reference to this day after modification<br />
2,4) a copy of the day made before modification </p>
<h2>Notes</h2>
<p>If the result would be outside the range [0, 255], the actual stored value is unspecified. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<pre><code>adds or subtracts a number of days

operator+= (public member function)

operator-=
adds or subtracts a number of days and a day, or find the difference between two days

operator+  (function)

operator-




</code></pre>
