---
title: "ceilf(3)"
name: "ceilf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ceilf/"
description: "ceil, ceilf, ceill – ceiling function: smallest integral value not less than argument"
---

<h2 class="name">NAME</h2>
<p> ceil, ceilf, ceill &#8211; ceiling function: smallest integral value not less than argument </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double ceil(double x);
float ceilf(float x);
long double ceill(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ceilf</code>(), <code>ceill</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the smallest integral value that is not less than <i>x</i>. </p>
<p> For example, <i>ceil(0.5)</i> is 1.0, and <i>ceil(-0.5)</i> is 0.0.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the ceiling of <i>x</i>. </p>
<p> If <i>x</i> is integral, +0, -0, NaN, or infinite, <i>x</i> itself is returned.</p>
<h2>ERRORS</h2>
<p> No errors occur. POSIX.1-2001 documents a range error for overflows, but see NOTES.</p>
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
<td> <code>ceil</code>(), <code>ceilf</code>(), <code>ceill</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>NOTES</h2>
<p> SUSv2 and POSIX.1-2001 contain text about overflow (which might set <i>errno</i> to <code>ERANGE</code>, or raise an <code>FE_OVERFLOW</code> exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).) </p>
<p> The integral value returned by these functions may be too large to store in an integer type (<i>int</i>, <i>long</i>, etc.). To avoid an overflow, which will produce undefined results, an application should perform a range check on the returned value before assigning it to an integer type.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3), <code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3), <code><a href="/docs/linux/man/3-round/">round</a></code>(3), <code><a href="/docs/linux/man/3-trunc/">trunc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
