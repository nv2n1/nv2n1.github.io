---
title: "fabs(3)"
name: "fabs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fabs/"
description: "fabs, fabsf, fabsl – absolute value of floating-point number"
---

<h2 class="name">NAME</h2>
<p> fabs, fabsf, fabsl &#8211; absolute value of floating-point number </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double fabs(double x);
float fabsf(float x);
long double fabsl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fabsf</code>(), <code>fabsl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the absolute value of the floating-point number <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the absolute value of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is -0, +0 is returned. </p>
<p> If <i>x</i> is negative infinity or positive infinity, positive infinity is returned.</p>
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
<td> <code>fabs</code>(), <code>fabsf</code>(), <code>fabsl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-abs/">abs</a></code>(3), <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-labs/">labs</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
