---
title: "fgetws(3)"
name: "fgetws"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetws/"
description: "fgetws – read a wide-character string from a FILE stream"
---

<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
wchar_t *fgetws(wchar_t *ws, int n, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fgetws</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3) function. It reads a string of at most <i>n-1</i> wide characters into the wide-character array pointed to by <i>ws</i>, and adds a terminating null wide character (L&#8217;\0&#8217;). It stops reading wide characters after it has encountered and stored a newline wide character. It also stops when end of stream is reached. </p>
<p> The programmer must ensure that there is room for at least <i>n</i> wide characters at <i>ws</i>. </p>
<p> For a nonlocking counterpart, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).  </p>
<h2>RETURN VALUE</h2>
<p> The <code>fgetws</code>() function, if successful, returns <i>ws</i>. If end of stream was already reached or if an error occurred, it returns NULL.  </p>
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
<td> <code>fgetws</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>fgetws</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> In the absence of additional information passed to the <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) call, it is reasonable to expect that <code>fgetws</code>() will actually read a multibyte string from the stream and then convert it to a wide-character string. </p>
<p> This function is unreliable, because it does not permit to deal properly with null wide characters that may be present in the input.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
