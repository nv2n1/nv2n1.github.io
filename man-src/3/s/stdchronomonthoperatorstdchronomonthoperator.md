---
title: "stdchronomonthoperatorstdchronomonthoperator(3)"
name: "stdchronomonthoperatorstdchronomonthoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonthoperatorstdchronomonthoperator/"
description: "std::chrono::month::operator++,std::chrono::month::operator– – std::chrono::month::operator++,std::chrono::month::operator–"
---

<p>std::chrono::month::operator++,std::chrono::month::operator&#8211; &#8211; std::chrono::month::operator++,std::chrono::month::operator&#8211;</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::month&amp; operator++() noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::month operator++(int) noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr std::chrono::month&amp; operator&#8211;() noexcept; <code>(3)</code> <i>(since C++20)</i><br />
constexpr std::chrono::month operator&#8211;(int) noexcept; <code>(4)</code> <i>(since C++20)</i> </p>
<pre><code>Adds or subtracts 1 from the month value, reducing the result modulo 12 to an integer in the range [1, 12].

1-2) Performs *this += std::chrono::months{1};

3-4) Performs *this -= std::chrono::months{1};
</code></pre>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1,3) a reference to this month after modification<br />
2,4) a copy of the month made before modification </p>
<h2>Notes</h2>
<p>After a call to one of these functions, ok() is always true. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<pre><code>adds or subtracts a number of months

operator+= (public member function)

operator-=
performs arithmetic on months

operator+  (function)

operator-




</code></pre>
