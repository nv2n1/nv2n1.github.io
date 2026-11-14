---
title: "clogl(3)"
name: "clogl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clogl/"
description: "clog, clogf, clogl – natural logarithm of a complex number"
---

<h2 class="name">NAME</h2>
<p> clog, clogf, clogl &#8211; natural logarithm of a complex number </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex clog(double complex </code><i>z</i><code>);</code><br />
 <code>float complex clogf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex clogl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex natural logarithm of <i>z</i>, with a branch cut along the negative real axis. </p>
<p> The logarithm <code>clog</code>() is the inverse function of the exponential <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3). Thus, if <i>y&nbsp;=&nbsp;clog(z)</i>, then <i>z&nbsp;=&nbsp;cexp(y)</i>. The imaginary part of <i>y</i> is chosen in the interval [-pi,pi]. </p>
<p> One has: </p>
<pre>
    clog(z) = log(cabs(z)) + I * carg(z)
</pre>
<p> Note that <i>z</i> close to zero will cause an overflow.</p>
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
<td> <code>clog</code>(), <code>clogf</code>(), <code>clogl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/3-clog10/">clog10</a></code>(3), <code><a href="/docs/linux/man/3-clog2/">clog2</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
