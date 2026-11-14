---
title: "ctan(3)"
name: "ctan"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctan/"
description: "ctan, ctanf, ctanl – complex tangent function"
---

<h2 class="name">NAME</h2>
<p> ctan, ctanf, ctanl &#8211; complex tangent function </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex ctan(double complex </code><i>z</i><code>);</code><br />
 <code>float complex ctanf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex ctanl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex tangent of <i>z</i>. </p>
<p> The complex tangent function is defined as: </p>
<pre>
    ctan(z) = csin(z) / ccos(z)
</pre>
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
<td> <code>ctan</code>(), <code>ctanf</code>(), <code>ctanl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-catan/">catan</a></code>(3), <code><a href="/docs/linux/man/3-ccos/">ccos</a></code>(3), <code><a href="/docs/linux/man/3-csin/">csin</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
