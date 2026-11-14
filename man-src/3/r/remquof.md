---
title: "remquof(3)"
name: "remquof"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remquof/"
description: "remquo, remquof, remquol – remainder and part of quotient"
---

<p>remquo, remquof, remquol &#8211; remainder and part of quotient</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double remquo(double x, double y, int *quo);
float remquof(float x, float y, int *quo);
long double remquol(long double x, long double y, int *quo);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>remquo</code>(), <code>remquof</code>(), <code>remquol</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>These functions compute the remainder and part of the quotient upon division of <i>x</i> by <i>y</i>. A few bits of the quotient are stored via the <i>quo</i> pointer. The remainder is returned as the function result. </p>
<p> The value of the remainder is the same as that computed by the <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3) function. </p>
<p> The value stored via the <i>quo</i> pointer has the sign of <i>x&nbsp;/&nbsp;y</i> and agrees with the quotient in at least the low order 3 bits. </p>
<p> For example, <i>remquo(29.0, 3.0)</i> returns -1.0 and might store 2. Note that the actual quotient might not fit in an integer.</p>
<h2>Return Value</h2>
<p>On success, these functions return the same value as the analogous functions described in <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3). </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is an infinity, and <i>y</i> is not a NaN, a domain error occurs, and a NaN is returned. </p>
<p> If <i>y</i> is zero, and <i>x</i> is not a NaN, a domain error occurs, and a NaN is returned.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is an infinity or <i>y</i> is 0, and the other argument is not a NaN</p>
<dd>An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
<p> These functions do not set <i>errno</i>.</p>
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
<td> <code>remquo</code>(), <code>remquof</code>(), <code>remquol</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fmod/">fmod</a></code>(3), <code><a href="/docs/linux/man/3-logb/">logb</a></code>(3), <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
