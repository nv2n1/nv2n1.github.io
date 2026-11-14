---
title: "atanhf(3)"
name: "atanhf"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atanhf/"
description: "atanh, atanhf, atanhl – inverse hyperbolic tangent function"
---

<h2 class="name">NAME</h2>
<p> atanh, atanhf, atanhl &#8211; inverse hyperbolic tangent function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double atanh(double x);
float atanhf(float x);
long double atanhl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>atanh</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>atanhf</code>(), <code>atanhl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions calculate the inverse hyperbolic tangent of <i>x</i>; that is the value whose hyperbolic tangent is <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the inverse hyperbolic tangent of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is +1 or -1, a pole error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the mathematically correct sign. </p>
<p> If the absolute value of <i>x</i> is greater than 1, a domain error occurs, and a NaN is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> less than -1 or greater than +1</p>
<dd> <i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Pole error: <i>x</i> is +1 or -1</p>
<dd> <i>errno</i> is set to <code>ERANGE</code> (but see BUGS). A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</dl>
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
<td> <code>atanh</code>(), <code>atanhf</code>(), <code>atanhl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD.</p>
<h2>BUGS</h2>
<p> In glibc 2.9 and earlier, when a pole error occurs, <i>errno</i> as set to <code>EDOM</code> instead of the POSIX-mandated <code>ERANGE</code>. Since version 2.10, glibc does the right thing.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-acosh/">acosh</a></code>(3), <code><a href="/docs/linux/man/3-asinh/">asinh</a></code>(3), <code><a href="/docs/linux/man/3-catanh/">catanh</a></code>(3), <code><a href="/docs/linux/man/3-cosh/">cosh</a></code>(3), <code><a href="/docs/linux/man/3-sinh/">sinh</a></code>(3), <code><a href="/docs/linux/man/3-tanh/">tanh</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
