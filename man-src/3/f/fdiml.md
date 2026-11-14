---
title: "fdiml(3)"
name: "fdiml"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdiml/"
description: "fdim, fdimf, fdiml – positive difference"
---

<h2 class="name">NAME</h2>
<p> fdim, fdimf, fdiml &#8211; positive difference </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;math.h&gt;</code> </p>
<p> <code>double fdim(double </code><i>x</i><code>, double </code><i>y</i><code>);</code><br />
 <code>float fdimf(float </code><i>x</i><code>, float </code><i>y</i><code>);</code><br />
 <code>long double fdiml(long double </code><i>x</i><code>, long double </code><i>y</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fdimf</code>(), <code>fdiml</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the positive difference, max(<i>x</i>&#8211;<i>y</i>,0), between their arguments.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the positive difference. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result overflow</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
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
<td> <code>fdim</code>(), <code>fdimf</code>(), <code>fdiml</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>BUGS</h2>
<p> Before glibc version 2.24 on certain architectures (e.g., x86, but not x86_64) these functions did not set <i>errno</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fmax/">fmax</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
