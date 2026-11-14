---
title: "asinl(3)"
name: "asinl"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asinl/"
description: "asin, asinf, asinl – arc sine function"
---

<h2 class="name">NAME</h2>
<p> asin, asinf, asinl &#8211; arc sine function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double asin(double x);
float asinf(float x);
long double asinl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>asinf</code>(), <code>asinl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions calculate the principal value of the arc sine of <i>x</i>; that is the value whose sine is <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the principal value of the arc sine of <i>x</i> in radians; the return value is in the range [-pi/2, pi/2]. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is outside the range [-1, 1], a domain error occurs, and a NaN is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is outside the range [-1, 1]</p>
<dd> <i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
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
<td> <code>asin</code>(), <code>asinf</code>(), <code>asinl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-acos/">acos</a></code>(3), <code><a href="/docs/linux/man/3-atan/">atan</a></code>(3), <code><a href="/docs/linux/man/3-atan2/">atan2</a></code>(3), <code><a href="/docs/linux/man/3-casin/">casin</a></code>(3), <code><a href="/docs/linux/man/3-cos/">cos</a></code>(3), <code><a href="/docs/linux/man/3-sin/">sin</a></code>(3), <code><a href="/docs/linux/man/3-tan/">tan</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
