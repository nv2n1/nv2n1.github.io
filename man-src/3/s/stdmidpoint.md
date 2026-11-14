---
title: "stdmidpoint(3)"
name: "stdmidpoint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmidpoint/"
description: "std::midpoint – std::midpoint"
---

<p>std::midpoint &#8211; std::midpoint</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;numeric&gt;

template&lt; class T &gt;                      (1) (since C++20)

constexpr T midpoint(T a, T b) noexcept;

template&lt; class T &gt;                      (2) (since C++20)

constexpr T* midpoint(T* a, T* b);</code></pre>
<p>Computes the midpoint of the integers, floating-points, or pointers a and b. </p>
<h2>Parameters</h2>
<p>a, b &#8211; intergers, floating-points, or pointer values</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
T must be an arithmetic type other than bool for overload <code>(1)</code><br />
&#8211;<br />
T must be a complete object type for overload <code>(2)</code></p>
<h2>Return value</h2>
<p>1) Half the sum of a and b. No overflow occurs. If a and b have integer type and the sum is odd, the result is rounded towards a. If a and b have floating-point type, at most one inexact operation occurs.<br />
2) If a and b point to, respectively, x[i] and x[j] of the same array object x (for the purpose of pointer_arithmetic), returns a pointer to x[i+(j-i)/2] where the division rounds towards zero. If a and b do not point to elements of the same array object, the behavior is undefined. </p>
<h2>Exceptions</h2>
<p>Throws no exceptions.</p>
<h2>Examples</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
