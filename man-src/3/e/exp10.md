---
title: "exp10(3)"
name: "exp10"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exp10/"
description: "exp10, exp10f, exp10l – base-10 exponential function"
---

<h2 class="name">NAME</h2>
<p> exp10, exp10f, exp10l &#8211; base-10 exponential function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;math.h&gt;
double exp10(double x);
float exp10f(float x);
long double exp10l(long double x);
</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions return the value of 10 raised to the power of <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the base-10 exponential value of <i>x</i>. </p>
<p> For various special cases, including the handling of infinity and NaN, as well as overflows and underflows, see <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3).</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> For a discussion of the errors that can occur for these functions, see <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>exp10</code>(), <code>exp10f</code>(), <code>exp10l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>BUGS</h2>
<p> Prior to version 2.19, the glibc implementation of these functions did not set <i>errno</i> to <code>ERANGE</code> when an underflow error occurred.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cbrt/">cbrt</a></code>(3), <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3), <code><a href="/docs/linux/man/3-exp2/">exp2</a></code>(3), <code><a href="/docs/linux/man/3-log10/">log10</a></code>(3), <code><a href="/docs/linux/man/3-sqrt/">sqrt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
