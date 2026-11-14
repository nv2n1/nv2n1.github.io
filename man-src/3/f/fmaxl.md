---
title: "fmaxl(3)"
name: "fmaxl"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmaxl/"
description: "fmax, fmaxf, fmaxl – determine maximum of two floating-point numbers"
---

<h2 class="name">NAME</h2>
<p> fmax, fmaxf, fmaxl &#8211; determine maximum of two floating-point numbers </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;math.h&gt;</code> </p>
<p> <code>double fmax(double </code><i>x</i><code>, double </code><i>y</i><code>);</code> <code>float fmaxf(float </code><i>x</i><code>, float </code><i>y</i><code>);</code> <code>long double fmaxl(long double </code><i>x</i><code>, long double </code><i>y</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fmax</code>(), <code>fmaxf</code>(), <code>fmaxl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the larger value of <i>x</i> and <i>y</i>.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the maximum of <i>x</i> and <i>y</i>. </p>
<p> If one argument is a NaN, the other argument is returned. </p>
<p> If both arguments are NaN, a NaN is returned.</p>
<h2>ERRORS</h2>
<p> No errors occur.</p>
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
<td> <code>fmax</code>(), <code>fmaxf</code>(), <code>fmaxl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fdim/">fdim</a></code>(3), <code><a href="/docs/linux/man/3-fmin/">fmin</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
