---
title: "lround(3)"
name: "lround"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lround/"
description: "lround, lroundf, lroundl, llround, llroundf, llroundl – round to nearest integer"
---

<h2 class="name">NAME</h2>
<p> lround, lroundf, lroundl, llround, llroundf, llroundl &#8211; round to nearest integer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
long lround(double x);
long lroundf(float x);
long lroundl(long double x);
long long llround(double x);
long long llroundf(float x);
long long llroundl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> All functions shown above:</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> These functions round their argument to the nearest integer value, rounding halfway cases away from zero, regardless of the current rounding direction (see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)). </p>
<p> Note that unlike the <code><a href="/docs/linux/man/3-round/">round</a></code>(3) and <code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), functions, the return type of these functions differs from that of their arguments.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the rounded integer value. </p>
<p> If <i>x</i> is a NaN or an infinity, or the rounded value is too large to be stored in a <i>long</i> (<i>long long</i> in the case of the <code>ll*</code> functions), then a domain error occurs, and the return value is unspecified.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is a NaN or infinite, or the rounded value is too large</p>
<dd> An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
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
<td> <code>lround</code>(), <code>lroundf</code>(), <code>lroundl</code>(),<br />
 <code>llround</code>(), <code>llroundf</code>(), <code>llroundl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3), <code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3), <code><a href="/docs/linux/man/3-round/">round</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
