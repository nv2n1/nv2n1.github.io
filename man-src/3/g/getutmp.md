---
title: "getutmp(3)"
name: "getutmp"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getutmp/"
description: "getutmp, getutmpx – copy utmp structure to utmpx, and vice versa"
---

<h2 class="name">NAME</h2>
<p> getutmp, getutmpx &#8211; copy utmp structure to utmpx, and vice versa </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;utmpx.h&gt;
void getutmp(const struct utmpx *ux, struct utmp *u);
void getutmpx(const struct utmp *u, struct utmpx *ux);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getutmp</code>() function copies the fields of the <i>utmpx</i> structure pointed to by <i>ux</i> to the corresponding fields of the <i>utmp</i> structure pointed to by <i>u</i>. The <code>getutmpx</code>() function performs the converse operation.</p>
<h2>RETURN VALUE</h2>
<p> These functions do not return a value.</p>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.1.</p>
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
<td> <code>getutmp</code>(), <code>getutmpx</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard, but appear on a few other systems, such as Solaris and NetBSD.</p>
<h2>NOTES</h2>
<p> These functions exist primarily for compatibility with other systems where the <i>utmp</i> and <i>utmpx</i> structures contain different fields, or the size of corresponding fields differs. On Linux, the two structures contain the same fields, and the fields have the same sizes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-utmpdump/">utmpdump</a></code>(1), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
