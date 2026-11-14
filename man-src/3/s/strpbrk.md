---
title: "strpbrk(3)"
name: "strpbrk"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strpbrk/"
description: "strpbrk – search a string for any of a set of bytes"
---

<p>strpbrk &#8211; search a string for any of a set of bytes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strpbrk(const char *s, const char *accept);</code></pre>
<h2>Description</h2>
<p>The <code>strpbrk</code>() function locates the first occurrence in the string <i>s</i> of any of the bytes in the string <i>accept</i>.</p>
<h2>Return Value</h2>
<p>The <code>strpbrk</code>() function returns a pointer to the byte in <i>s</i> that matches one of the bytes in <i>accept</i>, or NULL if no such byte is found.</p>
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
<td> <code>strpbrk</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), <code><a href="/docs/linux/man/3-wcspbrk/">wcspbrk</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
