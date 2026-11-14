---
title: "roundl(3)"
name: "roundl"
section: "3"
letter: "r"
url: "/docs/linux/man/3-roundl/"
description: "round, roundf, roundl – round to nearest integer, away from zero"
---

<p>round, roundf, roundl &#8211; round to nearest integer, away from zero</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double round(double x);
float roundf(float x);
long double roundl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>round</code>(), <code>roundf</code>(), <code>roundl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>These functions round <i>x</i> to the nearest integer, but round halfway cases away from zero (regardless of the current rounding direction, see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)), instead of to the nearest even integer like <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3). </p>
<p> For example, <i>round(0.5)</i> is 1.0, and <i>round(-0.5)</i> is -1.0.</p>
<h2>Return Value</h2>
<p>These functions return the rounded integer value. </p>
<p> If <i>x</i> is integral, +0, -0, NaN, or infinite, <i>x</i> itself is returned.</p>
<h2>Errors</h2>
<p>No errors occur. POSIX.1-2001 documents a range error for overflows, but see NOTES.</p>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>round</code>(), <code>roundf</code>(), <code>roundl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>POSIX.1-2001 contains text about overflow (which might set <i>errno</i> to <code>ERANGE</code>, or raise an <code>FE_OVERFLOW</code> exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).) </p>
<p> If you want to store the rounded value in an integer type, you probably want to use one of the functions described in <code><a href="/docs/linux/man/3-lround/">lround</a></code>(3) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-lround/">lround</a></code>(3), <code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3), <code><a href="/docs/linux/man/3-trunc/">trunc</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
