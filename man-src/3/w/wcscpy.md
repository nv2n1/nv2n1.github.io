---
title: "wcscpy(3)"
name: "wcscpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcscpy/"
description: "wcscpy – copy a wide-character string"
---

<p>wcscpy &#8211; copy a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
wchar_t *wcscpy(wchar_t *dest, const wchar_t *src);</code></pre>
<h2>Description</h2>
<p>The <code>wcscpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3) function. It copies the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;\0&#8217;), to the array pointed to by <i>dest</i>. </p>
<p> The strings may not overlap. </p>
<p> The programmer must ensure that there is room for at least <i>wcslen(src)+1</i> wide characters at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> <code>wcscpy</code>() returns <i>dest</i>.  </p>
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
<td> <code>wcscpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-wcpcpy/">wcpcpy</a></code>(3), <code><a href="/docs/linux/man/3-wcscat/">wcscat</a></code>(3), <code><a href="/docs/linux/man/3-wcsdup/">wcsdup</a></code>(3), <code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
