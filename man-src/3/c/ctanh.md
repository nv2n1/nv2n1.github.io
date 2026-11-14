---
title: "ctanh(3)"
name: "ctanh"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctanh/"
description: "ctanh, ctanhf, ctanhl – complex hyperbolic tangent"
---

<h2 class="name">NAME</h2>
<p> ctanh, ctanhf, ctanhl &#8211; complex hyperbolic tangent </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex ctanh(double complex </code><i>z</i><code>);</code><br />
 <code>float complex ctanhf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex ctanhl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex hyperbolic tangent of <i>z</i>. </p>
<p> The complex hyperbolic tangent function is defined mathematically as: </p>
<pre>
    ctanh(z) = csinh(z) / ccosh(z)
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
<td> <code>ctanh</code>(), <code>ctanhf</code>(), <code>ctanhl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-catanh/">catanh</a></code>(3), <code><a href="/docs/linux/man/3-ccosh/">ccosh</a></code>(3), <code><a href="/docs/linux/man/3-csinh/">csinh</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
