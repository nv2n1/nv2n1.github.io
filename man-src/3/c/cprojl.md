---
title: "cprojl(3)"
name: "cprojl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cprojl/"
description: "cproj, cprojf, cprojl – project into Riemann Sphere"
---

<h2 class="name">NAME</h2>
<p> cproj, cprojf, cprojl &#8211; project into Riemann Sphere </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cproj(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cprojf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cprojl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions project a point in the plane onto the surface of a Riemann Sphere, the one-point compactification of the complex plane. Each finite point <i>z</i> projects to <i>z</i> itself. Every complex infinite value is projected to a single infinite value, namely to positive infinity on the real axis.</p>
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
<td> <code>cproj</code>(), <code>cprojf</code>(), <code>cprojl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> In glibc 2.11 and earlier, the implementation does something different (a <i>stereographic</i> projection onto a Riemann Sphere).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
