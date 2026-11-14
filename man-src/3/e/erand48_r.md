---
title: "erand48_r(3)"
name: "erand48_r"
section: "3"
letter: "e"
url: "/docs/linux/man/3-erand48_r/"
description: "drand48_r, erand48_r, lrand48_r, nrand48_r, mrand48_r, jrand48_r, srand48_r, seed48_r, lcong48_r – generate uniformly distributed pseudo-random numbers reentrantly"
---

<h2 class="name">NAME</h2>
<p> drand48_r, erand48_r, lrand48_r, nrand48_r, mrand48_r, jrand48_r, srand48_r, seed48_r, lcong48_r &#8211; generate uniformly distributed pseudo-random numbers reentrantly </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int drand48_r(struct drand48_data *buffer, double *result);
int erand48_r(unsigned short xsubi[3],
              struct drand48_data *buffer, double *result);
int lrand48_r(struct drand48_data *buffer, long *result);
int nrand48_r(unsigned short xsubi[3],
              struct drand48_data *buffer, long *result);
int mrand48_r(struct drand48_data *buffer, long *result);
int jrand48_r(unsigned short xsubi[3],
              struct drand48_data *buffer, long *result);
int srand48_r(long int seedval, struct drand48_data *buffer);
int seed48_r(unsigned short seed16v[3],
             struct drand48_data *buffer);
int lcong48_r(unsigned short param[7],
              struct drand48_data *buffer);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> All functions shown above:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> These functions are the reentrant analogs of the functions described in <code><a href="/docs/linux/man/3-drand48/">drand48</a></code>(3). Instead of modifying the global random generator state, they use the supplied data <i>buffer</i>. </p>
<p> Before the first use, this struct must be initialized, for example, by filling it with zeros, or by calling one of the functions <code>srand48_r</code>(), <code>seed48_r</code>(), or <code>lcong48_r</code>().</p>
<h2>RETURN VALUE</h2>
<p> The return value is 0.</p>
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
<td> <code>drand48_r</code>(), <code>erand48_r</code>(), <code>lrand48_r</code>(), <code>nrand48_r</code>(), <code>mrand48_r</code>(), <code>jrand48_r</code>(), <code>srand48_r</code>(), <code>seed48_r</code>(), <code>lcong48_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:buffer
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions and are not portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-drand48/">drand48</a></code>(3), <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3), <code><a href="/docs/linux/man/3-random/">random</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
