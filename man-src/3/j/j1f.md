---
title: "j1f(3)"
name: "j1f"
section: "3"
letter: "j"
url: "/docs/linux/man/3-j1f/"
description: "j0, j0f, j0l, j1, j1f, j1l, jn, jnf, jnl – Bessel functions of the first kind"
---

<h2 class="name">NAME</h2>
<p> j0, j0f, j0l, j1, j1f, j1l, jn, jnf, jnl &#8211; Bessel functions of the first kind </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double j0(double x);
double j1(double x);
double jn(int n, double x);
float j0f(float x);
float j1f(float x);
float jnf(int n, float x);
long double j0l(long double x);
long double j1l(long double x);
long double jnl(int n, long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>j0</code>(), <code>j1</code>(), <code>jn</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<p> <code>j0f</code>(), <code>j0l</code>(), <code>j1f</code>(), <code>j1l</code>(), <code>jnf</code>(), <code>jnl</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE &nbsp;&gt;=&nbsp;600<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;(_ISOC99_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>j0</code>() and <code>j1</code>() functions return Bessel functions of <i>x</i> of the first kind of orders 0 and 1, respectively. The <code>jn</code>() function returns the Bessel function of <i>x</i> of the first kind of order <i>n</i>. </p>
<p> The <code>j0f</code>(), <code>j1f</code>(), and <code>jnf</code>(), functions are versions that take and return <i>float</i> values. The <code>j0l</code>(), <code>j1l</code>(), and <code>jnl</code>() functions are versions that take and return <i>long double</i> values.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the appropriate Bessel value of the first kind for <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is too large in magnitude, or the result underflows, a range error occurs, and the return value is 0.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result underflow, or <i>x</i> is too large in magnitude</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>.</dl>
<p> These functions do not raise exceptions for <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3).</p>
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
<td> <code>j0</code>(), <code>j0f</code>(), <code>j0l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>j1</code>(), <code>j1f</code>(), <code>j1l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>jn</code>(), <code>jnf</code>(), <code>jnl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The functions returning <i>double</i> conform to SVr4, 4.3BSD, POSIX.1-2001, and POSIX.1-2008. The others are nonstandard functions that also exist on the BSDs.</p>
<h2>BUGS</h2>
<p> There are errors of up to 2e-16 in the values returned by <code>j0</code>(), <code>j1</code>(), and <code>jn</code>() for values of <i>x</i> between -8 and 8.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-y0/">y0</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
