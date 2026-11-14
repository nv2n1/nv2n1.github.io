---
title: "log10f(3)"
name: "log10f"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log10f/"
description: "log10, log10f, log10l – base-10 logarithmic function"
---

<h2 class="name">NAME</h2>
<p> log10, log10f, log10l &#8211; base-10 logarithmic function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double log10(double x);
float log10f(float x);
long double log10l(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>log10f</code>(), <code>log10l</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the base 10 logarithm of <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the base 10 logarithm of <i>x</i>. </p>
<p> For special cases, including where <i>x</i> is 0, 1, negative, infinity, or NaN, see <code><a href="/docs/linux/man/3-log/">log</a></code>(3).</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> For a discussion of the errors that can occur for these functions, see <code><a href="/docs/linux/man/3-log/">log</a></code>(3).</p>
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
<td> <code>log10</code>(), <code>log10f</code>(), <code>log10l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cbrt/">cbrt</a></code>(3), <code><a href="/docs/linux/man/3-clog10/">clog10</a></code>(3), <code><a href="/docs/linux/man/3-exp10/">exp10</a></code>(3), <code><a href="/docs/linux/man/3-log/">log</a></code>(3), <code><a href="/docs/linux/man/3-log2/">log2</a></code>(3), <code><a href="/docs/linux/man/3-sqrt/">sqrt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
