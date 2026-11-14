---
title: "bcopy(3)"
name: "bcopy"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bcopy/"
description: "bcopy – copy byte sequence"
---

<h2 class="name">NAME</h2>
<p> bcopy &#8211; copy byte sequence </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
void bcopy(const void *src, void *dest, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bcopy</code>() function copies <i>n</i> bytes from <i>src</i> to <i>dest</i>. The result is correct, even when both areas overlap.</p>
<h2>RETURN VALUE</h2>
<p> None.</p>
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
<td> <code>bcopy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD. This function is deprecated (marked as LEGACY in POSIX.1-2001): use <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3) or <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3) in new programs. Note that the first two arguments are interchanged for <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3) and <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3). POSIX.1-2008 removes the specification of <code>bcopy</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
