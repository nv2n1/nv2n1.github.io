---
title: "ldexpl(3)"
name: "ldexpl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldexpl/"
description: "ldexp, ldexpf, ldexpl – multiply floating-point number by integral power of 2"
---

<h2 class="name">NAME</h2>
<p> ldexp, ldexpf, ldexpl &#8211; multiply floating-point number by integral power of 2 </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double ldexp(double x, int exp);
float ldexpf(float x, int exp);
long double ldexpl(long double x, int exp);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ldexpf</code>(), <code>ldexpl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the result of multiplying the floating-point number <i>x</i> by 2 raised to the power <i>exp</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return <i>x * (2^exp)</i>. </p>
<p> If <i>exp</i> is zero, then <i>x</i> is returned. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), positive infinity (negative infinity) is returned. </p>
<p> If the result underflows, a range error occurs, and zero is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with a sign the same as <i>x</i>.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error, overflow</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error, underflow</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>. An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</dl>
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
<td> <code>ldexp</code>(), <code>ldexpf</code>(), <code>ldexpl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-frexp/">frexp</a></code>(3), <code><a href="/docs/linux/man/3-modf/">modf</a></code>(3), <code><a href="/docs/linux/man/3-scalbln/">scalbln</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
