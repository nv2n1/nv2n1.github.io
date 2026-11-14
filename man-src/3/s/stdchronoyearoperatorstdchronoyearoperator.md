---
title: "stdchronoyearoperatorstdchronoyearoperator(3)"
name: "stdchronoyearoperatorstdchronoyearoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearoperatorstdchronoyearoperator/"
description: "std::chrono::year::operator++,std::chrono::year::operator– – std::chrono::year::operator++,std::chrono::year::operator–"
---

<p>std::chrono::year::operator++,std::chrono::year::operator&#8211; &#8211; std::chrono::year::operator++,std::chrono::year::operator&#8211;</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::year&amp; operator++() noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::year operator++(int) noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr std::chrono::year&amp; operator&#8211;() noexcept; <code>(3)</code> <i>(since C++20)</i><br />
constexpr std::chrono::year operator&#8211;(int) noexcept; <code>(4)</code> <i>(since C++20)</i> </p>
<pre><code>Adds or subtracts 1 from the year value.

1-2) Performs *this += std::chrono::years{1};

3-4) Performs *this -= std::chrono::years{1};
</code></pre>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1,3) a reference to this year after modification<br />
2,4) a copy of the year made before modification </p>
<h2>Notes</h2>
<p>If the result would be outside the range [-32767, 32767], the actual stored value is unspecified. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<pre><code>adds or subtracts a number of years from a year

operator+= (public member function)

operator-=
performs arithmetic on years

operator+  (public member function)

operator-




</code></pre>
