---
title: "ccosl(3)"
name: "ccosl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ccosl/"
description: "ccos, ccosf, ccosl – complex cosine function"
---

<h2 class="name">NAME</h2>
<p> ccos, ccosf, ccosl &#8211; complex cosine function </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex ccos(double complex </code><i>z</i><code>);</code><br />
 <code>float complex ccosf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex ccosl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex cosine of <i>z</i>. </p>
<p> The complex cosine function is defined as: </p>
<pre>
    ccos(z) = (exp(i * z) + exp(-i * z)) / 2
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
<td> <code>ccos</code>(), <code>ccosf</code>(), <code>ccosl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cacos/">cacos</a></code>(3), <code><a href="/docs/linux/man/3-csin/">csin</a></code>(3), <code><a href="/docs/linux/man/3-ctan/">ctan</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
