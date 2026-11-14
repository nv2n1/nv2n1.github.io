---
title: "clog10l(3)"
name: "clog10l"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clog10l/"
description: "clog10, clog10f, clog10l – base-10 logarithm of a complex number"
---

<h2 class="name">NAME</h2>
<p> clog10, clog10f, clog10l &#8211; base-10 logarithm of a complex number </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex clog10(double complex </code><i>z</i><code>);</code><br />
 <code>float complex clog10f(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex clog10l(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> The call <i>clog10(z)</i> is equivalent to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clog(z)/log(10) </p>
<p> or equally: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;log10(cabs(c))&nbsp;+&nbsp;I&nbsp;*&nbsp;carg(c)&nbsp;/&nbsp;log(10) </p>
<p> The other functions perform the same task for <i>float</i> and <i>long double</i>. </p>
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
<td> <code>clog10</code>(), <code>clog10f</code>(), <code>clog10l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions. The identifiers are reserved for future use in C99 and C11.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/3-clog2/">clog2</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
