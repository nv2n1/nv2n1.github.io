---
title: "atan(3)"
name: "atan"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atan/"
description: "atan, atanf, atanl – arc tangent function"
---

<h2 class="name">NAME</h2>
<p> atan, atanf, atanl &#8211; arc tangent function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double atan(double x);
float atanf(float x);
long double atanl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>atanf</code>(), <code>atanl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions calculate the principal value of the arc tangent of <i>x</i>; that is the value whose tangent is <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the principal value of the arc tangent of <i>x</i> in radians; the return value is in the range [-pi/2, pi/2]. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), +pi/2 (-pi/2) is returned.</p>
<h2>ERRORS</h2>
<p> No errors occur.</p>
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
<td> <code>atan</code>(), <code>atanf</code>(), <code>atanl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-acos/">acos</a></code>(3), <code><a href="/docs/linux/man/3-asin/">asin</a></code>(3), <code><a href="/docs/linux/man/3-atan2/">atan2</a></code>(3), <code><a href="/docs/linux/man/3-carg/">carg</a></code>(3), <code><a href="/docs/linux/man/3-catan/">catan</a></code>(3), <code><a href="/docs/linux/man/3-cos/">cos</a></code>(3), <code><a href="/docs/linux/man/3-sin/">sin</a></code>(3), <code><a href="/docs/linux/man/3-tan/">tan</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
