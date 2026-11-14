---
title: "wcsdup(3)"
name: "wcsdup"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsdup/"
description: "wcsdup – duplicate a wide-character string"
---

<p>wcsdup &#8211; duplicate a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcsdup(const wchar_t *s);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcsdup</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcsdup</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strdup/">strdup</a></code>(3) function. It allocates and returns a new wide-character string whose initial contents is a duplicate of the wide-character string pointed to by <i>s</i>. </p>
<p> Memory for the new wide-character string is obtained with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and should be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, <code>wcsdup</code>() returns a pointer to the new wide-character string. On error, it returns NULL, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory available to allocate duplicate string.</dl>
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
<td> <code>wcsdup</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2008. This function is not specified in POSIX.1-2001, and is not widely available on other systems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-strdup/">strdup</a></code>(3), <code><a href="/docs/linux/man/3-wcscpy/">wcscpy</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
