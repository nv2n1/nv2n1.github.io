---
title: "pow10(3)"
name: "pow10"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pow10/"
description: "pow10, pow10f, pow10l – base-10 power functions"
---

<p>pow10, pow10f, pow10l &#8211; base-10 power functions</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include &lt;math.h&gt;

double pow10(double x);
float pow10f(float x);
long double pow10l(long double x);</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>Description</h2>
<p>These functions return the value of 10 raised to the power <i>x</i>. </p>
<p> <code>Note well</code>: These functions perform exactly the same task as the functions described in <code><a href="/docs/linux/man/3-exp10/">exp10</a></code>(3), with the difference that the latter functions are now standardized in TS 18661-4:2015. Those latter functions should be used in preference to the functions described in this page.</p>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.1. Since glibc 2.27, the use of these functions in new programs is no longer supported.</p>
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
<td> <code>pow10</code>(), <code>pow10f</code>(), <code>pow10l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This functions are nonstandard GNU extensions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-exp10/">exp10</a></code>(3), <code><a href="/docs/linux/man/3-pow/">pow</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
