---
title: "strtoimax(3)"
name: "strtoimax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtoimax/"
description: "strtoimax, strtoumax – convert string to integer"
---

<p>strtoimax, strtoumax &#8211; convert string to integer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;inttypes.h&gt;

intmax_t strtoimax(const char *nptr, char **endptr, int base);
uintmax_t strtoumax(const char *nptr, char **endptr, int base);</code></pre>
<h2>Description</h2>
<p>These functions are just like <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3) and <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3), except that they return a value of type <i>intmax_t</i> and <i>uintmax_t</i>, respectively.</p>
<h2>Return Value</h2>
<p>On success, the converted value is returned. If nothing was found to convert, zero is returned. On overflow or underflow <code>INTMAX_MAX</code> or <code>INTMAX_MIN</code> or <code>UINTMAX_MAX</code> is returned, and <i>errno</i> is set to <code>ERANGE</code>.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>strtoimax</code>(), <code>strtoumax</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-imaxabs/">imaxabs</a></code>(3), <code><a href="/docs/linux/man/3-imaxdiv/">imaxdiv</a></code>(3), <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3), <code><a href="/docs/linux/man/3-wcstoimax/">wcstoimax</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
