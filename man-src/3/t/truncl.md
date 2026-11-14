---
title: "truncl(3)"
name: "truncl"
section: "3"
letter: "t"
url: "/docs/linux/man/3-truncl/"
description: "trunc, truncf, truncl – round to integer, toward zero"
---

<p>trunc, truncf, truncl &#8211; round to integer, toward zero</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double trunc(double x);
float truncf(float x);
long double truncl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>trunc</code>(), <code>truncf</code>(), <code>truncl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>These functions round <i>x</i> to the nearest integer value that is not larger in magnitude than <i>x</i>.</p>
<h2>Return Value</h2>
<p>These functions return the rounded integer value, in floating format. </p>
<p> If <i>x</i> is integral, infinite, or NaN, <i>x</i> itself is returned.</p>
<h2>Errors</h2>
<p>No errors occur.</p>
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
<td> <code>trunc</code>(), <code>truncf</code>(), <code>truncl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The integral value returned by these functions may be too large to store in an integer type (<i>int</i>, <i>long</i>, etc.). To avoid an overflow, which will produce undefined results, an application should perform a range check on the returned value before assigning it to an integer type.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3), <code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3), <code><a href="/docs/linux/man/3-round/">round</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
