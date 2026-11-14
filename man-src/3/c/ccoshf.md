---
title: "ccoshf(3)"
name: "ccoshf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ccoshf/"
description: "ccosh, ccoshf, ccoshl – complex hyperbolic cosine"
---

<h2 class="name">NAME</h2>
<p> ccosh, ccoshf, ccoshl &#8211; complex hyperbolic cosine </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex ccosh(double complex </code><i>z</i><code>);</code><br />
 <code>float complex ccoshf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex ccoshl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex hyperbolic cosine of <i>z</i>. </p>
<p> The complex hyperbolic cosine function is defined as: </p>
<pre>
    ccosh(z) = (exp(z)+exp(-z))/2
</pre>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.</p>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cacosh/">cacosh</a></code>(3), <code><a href="/docs/linux/man/3-csinh/">csinh</a></code>(3), <code><a href="/docs/linux/man/3-ctanh/">ctanh</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
