---
title: "nextup(3)"
name: "nextup"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextup/"
description: "nextup, nextupf, nextupl, nextdown, nextdownf, nextdownl – return next floating-point number toward positive/negative infinity"
---

<p>nextup, nextupf, nextupl, nextdown, nextdownf, nextdownl &#8211; return next floating-point number toward positive/negative infinity</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE     /* See feature_test_macros(7) */
#include &lt;math.h&gt;

double nextup(double x);
float nextupf(float x);
long double nextupl(long double x);

double nextdown(double x);
float nextdownf(float x);
long double nextdownl(long double x);</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>Description</h2>
<p>The <code>nextup</code>(), <code>nextupf</code>(), and <code>nextupl</code>() functions return the next representable floating-point number greater than <i>x</i>. </p>
<p> If <i>x</i> is the smallest representable negative number in the corresponding type, these functions return -0. If <i>x</i> is 0, the returned value is the smallest representable positive number of the corresponding type. </p>
<p> If <i>x</i> is positive infinity, the returned value is positive infinity. If <i>x</i> is negative infinity, the returned value is the largest representable finite negative number of the corresponding type. </p>
<p> If <i>x</i> is Nan, the returned value is NaN. </p>
<p> The value returned by <i>nextdown(x)</i> is <i>-nextup(-x)</i>, and similarly for the other types.</p>
<h2>Return Value</h2>
<p>See DESCRIPTION.</p>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.24.</p>
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
<td> <code>nextup</code>(), <code>nextupf</code>(), <code>nextupl</code>(),<br />
 <code>nextdown</code>(), <code>nextdownf</code>(), <code>nextdownl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are described in <i>IEEE Std 754-2008 &#8211; Standard for Floating-Point Arithmetic</i> and <i>ISO/IEC TS 18661.</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-nextafter/">nextafter</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
