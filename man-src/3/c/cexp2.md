---
title: "cexp2(3)"
name: "cexp2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cexp2/"
description: "cexp2, cexp2f, cexp2l – base-2 exponent of a complex number"
---

<h2 class="name">NAME</h2>
<p> cexp2, cexp2f, cexp2l &#8211; base-2 exponent of a complex number </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cexp2(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cexp2f(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cexp2l(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> The function returns 2 raised to the power of <i>z</i>.</p>
<h2>CONFORMING TO</h2>
<p> These function names are reserved for future use in C99. </p>
<p> As at version 2.31, these functions are not provided in glibc.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/3-clog10/">clog10</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
