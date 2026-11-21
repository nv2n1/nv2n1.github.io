---
title: "fputws(3)"
name: "fputws"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fputws/"
description: "fputws – write a wide-character string to a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fputws &#8211; write a wide-character string to a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
int fputws(const wchar_t *ws, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fputws</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fputs/">fputs</a></code>(3) function. It writes the wide-character string starting at <i>ws</i>, up to but not including the terminating null wide character (L&#8217;\0&#8217;), to <i>stream</i>. </p>
<p> For a nonlocking counterpart, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).  </p>
<h2>RETURN VALUE</h2>
<p> The <code>fputws</code>() function returns a nonnegative integer if the operation was successful, or -1 to indicate an error.  </p>
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
<td> <code>fputws</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>fputws</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> In the absence of additional information passed to the <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) call, it is reasonable to expect that <code>fputws</code>() will actually write the multibyte string corresponding to the wide-character string <i>ws</i>.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fputwc/">fputwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
