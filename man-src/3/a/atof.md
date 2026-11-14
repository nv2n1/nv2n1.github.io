---
title: "atof(3)"
name: "atof"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atof/"
description: "atof – convert a string to a double"
---

<h2 class="name">NAME</h2>
<p> atof &#8211; convert a string to a double </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
double atof(const char *nptr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>atof</code>() function converts the initial portion of the string pointed to by <i>nptr</i> to <i>double</i>. The behavior is the same as </p>
<p> strtod(nptr, NULL); </p>
<p> except that <code>atof</code>() does not detect errors.</p>
<h2>RETURN VALUE</h2>
<p> The converted value.</p>
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
<td> <code>atof</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atoi/">atoi</a></code>(3), <code><a href="/docs/linux/man/3-atol/">atol</a></code>(3), <code><a href="/docs/linux/man/3-strfromd/">strfromd</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3), <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
