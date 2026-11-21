---
title: "strlen(3)"
name: "strlen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strlen/"
description: "strlen – calculate the length of a string"
---

<p>strlen &#8211; calculate the length of a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
size_t strlen(const char *s);</code></pre>
<h2>Description</h2>
<p>The <code>strlen</code>() function calculates the length of the string pointed to by <i>s</i>, excluding the terminating null byte (&#8216;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strlen</code>() function returns the number of bytes in the string pointed to by <i>s</i>.  </p>
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
<td> <code>strlen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, C11, SVr4, 4.3BSD.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strnlen/">strnlen</a></code>(3), <code><a href="/docs/linux/man/3-wcslen/">wcslen</a></code>(3), <code><a href="/docs/linux/man/3-wcsnlen/">wcsnlen</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
