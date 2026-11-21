---
title: "wcslen(3)"
name: "wcslen"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcslen/"
description: "wcslen – determine the length of a wide-character string"
---

<p>wcslen &#8211; determine the length of a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
size_t wcslen(const wchar_t *s);</code></pre>
<h2>Description</h2>
<p>The <code>wcslen</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3) function. It determines the length of the wide-character string pointed to by <i>s</i>, excluding the terminating null wide character (L&#8217;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcslen</code>() function returns the number of wide characters in <i>s</i>.  </p>
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
<td> <code>wcslen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
