---
title: "hypot(3)"
name: "hypot"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hypot/"
description: "hypot, hypotf, hypotl – Euclidean distance function"
---

<h2 class="name">NAME</h2>
<p> hypot, hypotf, hypotl &#8211; Euclidean distance function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double hypot(double x, double y);
float hypotf(float x, float y);
long double hypotl(long double x, long double y);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>hypot</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>hypotf</code>(), <code>hypotl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return sqrt(<i>x</i>*<i>x</i>+<i>y</i>*<i>y</i>). This is the length of the hypotenuse of a right-angled triangle with sides of length <i>x</i> and <i>y</i>, or the distance of the point (<i>x</i>,<i>y</i>) from the origin. </p>
<p> The calculation is performed without undue overflow or underflow during the intermediate steps of the calculation.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the length of the hypotenuse of a right-angled triangle with sides of length <i>x</i> and <i>y</i>. </p>
<p> If <i>x</i> or <i>y</i> is an infinity, positive infinity is returned. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, and the other argument is not an infinity, a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively. </p>
<p> If both arguments are subnormal, and the result is subnormal, a range error occurs, and the correct result is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result overflow</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error: result underflow</p>
<dd> An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</p>
<dt>
<dd> These functions do not set <i>errno</i> for this case.</dl>
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
<td> <code>hypot</code>(), <code>hypotf</code>(), <code>hypotl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-sqrt/">sqrt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
