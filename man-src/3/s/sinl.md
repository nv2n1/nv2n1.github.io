---
title: "sinl(3)"
name: "sinl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sinl/"
description: "sin, sinf, sinl – sine function"
---

<p>sin, sinf, sinl &#8211; sine function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double sin(double x);
float sinf(float x);
long double sinl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sinf</code>(), <code>sinl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions return the sine of <i>x</i>, where <i>x</i> is given in radians.</p>
<h2>Return Value</h2>
<p>On success, these functions return the sine of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity or negative infinity, a domain error occurs, and a NaN is returned.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is an infinity</p>
<dd><i>errno</i> is set to <code>EDOM</code> (but see BUGS). An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sin</code>(), <code>sinf</code>(), <code>sinl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>Bugs</h2>
<p>Before version 2.10, the glibc implementation did not set <i>errno</i> to <code>EDOM</code> when a domain error occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-acos/">acos</a></code>(3), <code><a href="/docs/linux/man/3-asin/">asin</a></code>(3), <code><a href="/docs/linux/man/3-atan/">atan</a></code>(3), <code><a href="/docs/linux/man/3-atan2/">atan2</a></code>(3), <code><a href="/docs/linux/man/3-cos/">cos</a></code>(3), <code><a href="/docs/linux/man/3-csin/">csin</a></code>(3), <code><a href="/docs/linux/man/3-sincos/">sincos</a></code>(3), <code><a href="/docs/linux/man/3-tan/">tan</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
