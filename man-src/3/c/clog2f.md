---
title: "clog2f(3)"
name: "clog2f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clog2f/"
description: "clog2, clog2f, clog2l – base-2 logarithm of a complex number"
---

<h2 class="name">NAME</h2>
<p> clog2, clog2f, clog2l &#8211; base-2 logarithm of a complex number </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex clog2(double complex </code><i>z</i><code>);</code><br />
 <code>float complex clog2f(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex clog2l(long double complex </code><i>z</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The call <i>clog2(z)</i> is equivalent to <i>clog(z)/<a href="/docs/linux/man/2-log/">log</a>(2)</i>. </p>
<p> The other functions perform the same task for <i>float</i> and <i>long double</i>. </p>
<p> Note that <i>z</i> close to zero will cause an overflow.</p>
<h2>CONFORMING TO</h2>
<p> These function names are reserved for future use in C99. </p>
<p> Not yet in glibc, as at version 2.19.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/3-clog10/">clog10</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
