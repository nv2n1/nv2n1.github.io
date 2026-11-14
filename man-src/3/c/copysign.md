---
title: "copysign(3)"
name: "copysign"
section: "3"
letter: "c"
url: "/docs/linux/man/3-copysign/"
description: "copysign, copysignf, copysignl – copy sign of a number"
---

<h2 class="name">NAME</h2>
<p> copysign, copysignf, copysignl &#8211; copy sign of a number </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double copysign(double x, double y);
float copysignf(float x, float y);
long double copysignl(long double x, long double y);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>copysign</code>(), <code>copysignf</code>(), <code>copysignl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return a value whose absolute value matches that of <i>x</i>, but whose sign bit matches that of <i>y</i>. </p>
<p> For example, <i>copysign(42.0, -1.0)</i> and <i>copysign(-42.0, -1.0)</i> both return -42.0.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return a value whose magnitude is taken from <i>x</i> and whose sign is taken from <i>y</i>. </p>
<p> If <i>x</i> is a NaN, a NaN with the sign bit of <i>y</i> is returned.</p>
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
<td> <code>copysign</code>(), <code>copysignf</code>(), <code>copysignl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. This function is defined in IEC 559 (and the appendix with recommended functions in IEEE 754/IEEE 854).</p>
<h2>NOTES</h2>
<p> On architectures where the floating-point formats are not IEEE 754 compliant, these functions may treat a negative zero as positive.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-signbit/">signbit</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
