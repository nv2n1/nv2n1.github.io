---
title: "floor(3)"
name: "floor"
section: "3"
letter: "f"
url: "/docs/linux/man/3-floor/"
description: "floor, floorf, floorl – largest integral value not greater than argument"
---

<h2 class="name">NAME</h2>
<p> floor, floorf, floorl &#8211; largest integral value not greater than argument </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double floor(double x);
float floorf(float x);
long double floorl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>floorf</code>(), <code>floorl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the largest integral value that is not greater than <i>x</i>. </p>
<p> For example, <i>floor(0.5)</i> is 0.0, and <i>floor(-0.5)</i> is -1.0.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the floor of <i>x</i>. </p>
<p> If <i>x</i> is integral, +0, -0, NaN, or an infinity, <i>x</i> itself is returned.</p>
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
<td> <code>floor</code>(), <code>floorf</code>(), <code>floorl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>NOTES</h2>
<p> SUSv2 and POSIX.1-2001 contain text about overflow (which might set <i>errno</i> to <code>ERANGE</code>, or raise an <code>FE_OVERFLOW</code> exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3), <code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3), <code><a href="/docs/linux/man/3-round/">round</a></code>(3), <code><a href="/docs/linux/man/3-trunc/">trunc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
