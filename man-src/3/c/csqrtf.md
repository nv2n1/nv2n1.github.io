---
title: "csqrtf(3)"
name: "csqrtf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csqrtf/"
description: "csqrt, csqrtf, csqrtl – complex square root"
---

<h2 class="name">NAME</h2>
<p> csqrt, csqrtf, csqrtl &#8211; complex square root </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex csqrt(double complex </code><i>z</i><code>);</code><br />
 <code>float complex csqrtf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex csqrtl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex square root of <i>z</i>, with a branch cut along the negative real axis. (That means that <i>csqrt(-1+eps*I)</i> will be close to I while <i>csqrt(-1-eps*I)</i> will be close to -I, <i>if eps</i> is a small positive real number.)</p>
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
<td> <code>csqrt</code>(), <code>csqrtf</code>(), <code>csqrtl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
