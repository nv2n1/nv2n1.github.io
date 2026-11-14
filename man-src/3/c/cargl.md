---
title: "cargl(3)"
name: "cargl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cargl/"
description: "carg, cargf, cargl – calculate the complex argument"
---

<h2 class="name">NAME</h2>
<p> carg, cargf, cargl &#8211; calculate the complex argument </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double carg(double complex </code><i>z</i><code>);</code><br />
 <code>float cargf(float complex </code><i>z</i><code>);</code><br />
 <code>long double cargl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex argument (also called phase angle) of <i>z</i>, with a branch cut along the negative real axis. </p>
<p> A complex number can be described by two real coordinates. One may use rectangular coordinates and gets </p>
<pre>
    z = x + I * y
</pre>
<p> where <i>x&nbsp;=&nbsp;creal(z)</i> and <i>y&nbsp;=&nbsp;cimag(z)</i>. </p>
<p> Or one may use polar coordinates and gets </p>
<pre>
    z = r * cexp(I * a)
</pre>
<p> where <i>r&nbsp;=&nbsp;cabs(z)</i> is the &quot;radius&quot;, the &quot;modulus&quot;, the absolute value of <i>z</i>, and <i>a&nbsp;=&nbsp;carg(z)</i> is the &quot;phase angle&quot;, the argument of <i>z</i>. </p>
<p> One has: </p>
<pre>
    tan(carg(z)) = cimag(z) / creal(z)
</pre>
<h2>RETURN VALUE</h2>
<p> The return value is in the range of [-pi,pi].</p>
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
<td> <code>carg</code>(), <code>cargf</code>(), <code>cargl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
