---
title: "cabsl(3)"
name: "cabsl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cabsl/"
description: "cabs, cabsf, cabsl – absolute value of a complex number"
---

<h2 class="name">NAME</h2>
<p> cabs, cabsf, cabsl &#8211; absolute value of a complex number </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double cabs(double complex </code><i>z</i><code>);</code><br />
 <code>float cabsf(float complex </code><i>z</i><code>);</code><br />
 <code>long double cabsl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions return the absolute value of the complex number <i>z</i>. The result is a real number.</p>
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
<td> <code>cabs</code>(), <code>cabsf</code>(), <code>cabsl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> The function is actually an alias for <i>hypot(a, b)</i> (or, equivalently, <i>sqrt(a*a&nbsp;+&nbsp;b*b)</i>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-abs/">abs</a></code>(3), <code><a href="/docs/linux/man/3-cimag/">cimag</a></code>(3), <code><a href="/docs/linux/man/3-hypot/">hypot</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
