---
title: "cpowf(3)"
name: "cpowf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpowf/"
description: "cpow, cpowf, cpowl – complex power function"
---

<h2 class="name">NAME</h2>
<p> cpow, cpowf, cpowl &#8211; complex power function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;complex.h&gt;
double complex cpow(double complex x, complex double z);
float complex cpowf(float complex x, complex float z);
long double complex cpowl(long double complex x,
                          complex long double z);
Link with - lm.
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions calculate <i>x</i> raised to the power <i>z</i> (with a branch cut for <i>x</i> along the negative real axis.)</p>
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
<td> <code>cpow</code>(), <code>cpowf</code>(), <code>cpowl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-pow/">pow</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
