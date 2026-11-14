---
title: "expm1l(3)"
name: "expm1l"
section: "3"
letter: "e"
url: "/docs/linux/man/3-expm1l/"
description: "expm1, expm1f, expm1l – exponential minus 1"
---

<h2 class="name">NAME</h2>
<p> expm1, expm1f, expm1l &#8211; exponential minus 1 </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double expm1(double x);
float expm1f(float x);
long double expm1l(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>expm1</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>expm1f</code>(), <code>expm1l</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return a value equivalent to </p>
<pre>
    exp(x) - 1
</pre>
<p> The result is computed in a way that is accurate even if the value of <i>x</i> is near zero&#8212;a case where <i>exp(x) &#8211; 1</i> would be inaccurate due to subtraction of two numbers that are nearly equal.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return <i>exp(x)&nbsp;&#8211; 1</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is positive infinity, positive infinity is returned. </p>
<p> If <i>x</i> is negative infinity, -1 is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error, overflow</p>
<dd> <i>errno</i> is set to <code>ERANGE</code> (but see BUGS). An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>expm1</code>(), <code>expm1f</code>(), <code>expm1l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>BUGS</h2>
<p> Before glibc 2.17, on certain architectures (e.g., x86, but not x86_64) <code>expm1</code>() raised a bogus underflow floating-point exception for some large negative <i>x</i> values (where the function result approaches -1), </p>
<p> Before approximately glibc version 2.11, <code>expm1</code>() raised a bogus invalid floating-point exception in addition to the expected overflow exception, and returned a NaN instead of positive infinity. for some large positive <i>x</i> values, </p>
<p> Before version 2.11, the glibc implementation did not set <i>errno</i> to <code>ERANGE</code> when a range error occurred.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3), <code><a href="/docs/linux/man/3-log/">log</a></code>(3), <code><a href="/docs/linux/man/3-log1p/">log1p</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
