---
title: "fmaf(3)"
name: "fmaf"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmaf/"
description: "fma, fmaf, fmal – floating-point multiply and add"
---

<h2 class="name">NAME</h2>
<p> fma, fmaf, fmal &#8211; floating-point multiply and add </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double fma(double x, double y, double z);
float fmaf(float x, float y, float z);
long double fmal(long double x, long double y, long double z);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fma</code>(), <code>fmaf</code>(), <code>fmal</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> These functions compute <i>x</i> * <i>y</i> + <i>z</i>. The result is rounded as one ternary operation according to the current rounding mode (see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)).</p>
<h2>RETURN VALUE</h2>
<p> These functions return the value of <i>x</i> * <i>y</i> + <i>z</i>, rounded as one ternary operation. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> times <i>y</i> is an exact infinity, and <i>z</i> is an infinity with the opposite sign, a domain error occurs, and a NaN is returned. </p>
<p> If one of <i>x</i> or <i>y</i> is an infinity, the other is 0, and <i>z</i> is not a NaN, a domain error occurs, and a NaN is returned. </p>
<p> If one of <i>x</i> or <i>y</i> is an infinity, and the other is 0, and <i>z</i> is a NaN, a domain error occurs, and a NaN is returned. </p>
<p> If <i>x</i> times <i>y</i> is not an infinity times zero (or vice versa), and <i>z</i> is a NaN, a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and an infinity with the correct sign is returned. </p>
<p> If the result underflows, a range error occurs, and a signed 0 is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> * <i>y</i> + <i>z</i>, or <i>x</i> * <i>y</i> is invalid and <i>z</i> is not a NaN</p>
<dd> An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Range error: result overflow</p>
<dd> An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error: result underflow</p>
<dd> An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</dl>
<p> These functions do not set <i>errno</i>.</p>
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
<td> <code>fma</code>(), <code>fmaf</code>(), <code>fmal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3), <code><a href="/docs/linux/man/3-remquo/">remquo</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
