---
title: "abs(3)"
name: "abs"
section: "3"
letter: "a"
url: "/docs/linux/man/3-abs/"
description: "abs, labs, llabs, imaxabs – compute the absolute value of an integer"
---

<h2 class="name">NAME</h2>
<p> abs, labs, llabs, imaxabs &#8211; compute the absolute value of an integer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int abs(int j);
long labs(long j);
long long llabs(long long j);
#include &lt;inttypes.h&gt;
intmax_t imaxabs(intmax_t j);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>llabs</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> The <code>abs</code>() function computes the absolute value of the integer argument <i>j</i>. The <code>labs</code>(), <code>llabs</code>(), and <code>imaxabs</code>() functions compute the absolute value of the argument <i>j</i> of the appropriate integer type for the function.</p>
<h2>RETURN VALUE</h2>
<p> Returns the absolute value of the integer argument, of the appropriate integer type for the function.</p>
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
<td> <code>abs</code>(), <code>labs</code>(), <code>llabs</code>(), <code>imaxabs</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99, SVr4, 4.3BSD. C89 only includes the <code>abs</code>() and <code>labs</code>() functions; the functions <code>llabs</code>() and <code>imaxabs</code>() were added in C99.</p>
<h2>NOTES</h2>
<p> Trying to take the absolute value of the most negative integer is not defined. </p>
<p> The <code>llabs</code>() function is included in glibc since version 2.0. The <code>imaxabs</code>() function is included in glibc since version 2.1.1. </p>
<p> For <code>llabs</code>() to be declared, it may be necessary to define <code>_ISOC99_SOURCE</code> or <code>_ISOC9X_SOURCE</code> (depending on the version of glibc) before including any standard headers. </p>
<p> By default, GCC handles <code>abs</code>(), <code>labs</code>(), and (since GCC 3.0) <code>llabs</code>() and <code>imaxabs</code>() as built-in functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-fabs/">fabs</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-rint/">rint</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
