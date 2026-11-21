---
title: "wcsstr(3)"
name: "wcsstr"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsstr/"
description: "wcsstr – locate a substring in a wide-character string"
---

<p>wcsstr &#8211; locate a substring in a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
wchar_t *wcsstr(const wchar_t *haystack, const wchar_t *needle);</code></pre>
<h2>Description</h2>
<p>The <code>wcsstr</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3) function. It searches for the first occurrence of the wide-character string <i>needle</i> (without its terminating null wide character (L&#8217;\0&#8217;)) as a substring in the wide-character string <i>haystack</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcsstr</code>() function returns a pointer to the first occurrence of <i>needle</i> in <i>haystack</i>. It returns NULL if <i>needle</i> does not occur as a substring in <i>haystack</i>. </p>
<p> Note the special case: If <i>needle</i> is the empty wide-character string, the return value is always <i>haystack</i> itself.  </p>
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
<td> <code>wcsstr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
