---
title: "erfcf(3)"
name: "erfcf"
section: "3"
letter: "e"
url: "/docs/linux/man/3-erfcf/"
description: "erfc, erfcf, erfcl – complementary error function"
---

<h2 class="name">NAME</h2>
<p> erfc, erfcf, erfcl &#8211; complementary error function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double erfc(double x);
float erfcf(float x);
long double erfcl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>erfc</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L || _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>erfcf</code>(), <code>erfcl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the complementary error function of <i>x</i>, that is, 1.0 &#8211; erf(x).</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the complementary error function of <i>x</i>, a value in the range [0,2]. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 or -0, 1 is returned. </p>
<p> If <i>x</i> is positive infinity, +0 is returned. </p>
<p> If <i>x</i> is negative infinity, +2 is returned. </p>
<p> If the function result underflows and produces an unrepresentable value, the return value is 0.0. </p>
<p> If the function result underflows but produces a representable (i.e., subnormal) value, that value is returned, and a range error occurs.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result underflow (result is subnormal)</p>
<dd> An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</dl>
<p> These functions do not set <i>errno</i>.</p>
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
<td> <code>erfc</code>(), <code>erfcf</code>(), <code>erfcl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The <code>erfc</code>(), <code>erfcf</code>(), and <code>erfcl</code>() functions are provided to avoid the loss accuracy that would occur for the calculation 1-erf(x) for large values of <i>x</i> (for which the value of erf(x) approaches 1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cerf/">cerf</a></code>(3), <code><a href="/docs/linux/man/3-erf/">erf</a></code>(3), <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
