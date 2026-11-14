---
title: "cexpf(3)"
name: "cexpf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cexpf/"
description: "cexp, cexpf, cexpl – complex exponential function"
---

<h2 class="name">NAME</h2>
<p> cexp, cexpf, cexpl &#8211; complex exponential function </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cexp(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cexpf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cexpl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate e (2.71828&#8230;, the base of natural logarithms) raised to the power of <i>z</i>. </p>
<p> One has: </p>
<pre>
    cexp(I * z) = ccos(z) + I * csin(z)
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
<td> <code>cexp</code>(), <code>cexpf</code>(), <code>cexpl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp2/">cexp2</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/3-cpow/">cpow</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
