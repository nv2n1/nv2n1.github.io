---
title: "wcpcpy(3)"
name: "wcpcpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcpcpy/"
description: "wcpcpy – copy a wide-character string, returning a pointer to its end"
---

<p>wcpcpy &#8211; copy a wide-character string, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
wchar_t *wcpcpy(wchar_t *dest, const wchar_t *src);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcpcpy</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>wcpcpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3) function. It copies the wide-character string pointed to by <i>src</i>, including the terminating null wide character (L&#8217;\0&#8217;), to the array pointed to by <i>dest</i>. </p>
<p> The strings may not overlap. </p>
<p> The programmer must ensure that there is room for at least <i>wcslen(src)+1</i> wide characters at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> <code>wcpcpy</code>() returns a pointer to the end of the wide-character string <i>dest</i>, that is, a pointer to the terminating null wide character.  </p>
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
<td> <code>wcpcpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-wcscpy/">wcscpy</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
