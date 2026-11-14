---
title: "cerff(3)"
name: "cerff"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cerff/"
description: "cerf, cerff, cerfl, cerfc, cerfcf, cerfcl – complex error function"
---

<h2>NAME</h2>
<p> cerf, cerff, cerfl, cerfc, cerfcf, cerfcl &#8211; complex error function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cerf(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cerff(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cerfl(long double complex </code><i>z</i><code>);</code> </p>
<p> <code>double complex cerfc(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cerfcf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cerfcl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> The (unimplemented) function <code>cerf</code>() is the complex version of the error function. erf(z) = 2/sqrt(pi) * integral from 0 to z of exp(-t*t) dt. The function <code>cerfc</code>() is defined as cerfc(z) = 1-cerf(z).</p>
<h2>CONFORMING TO</h2>
<p> The function names are reserved for future use in C99.</p>
<h2>AVAILABILITY</h2>
<p> Not yet in glibc, as at version 2.12.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-erf/">erf</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
