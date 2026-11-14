---
title: "iconv_open(3)"
name: "iconv_open"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iconv_open/"
description: "iconv_open – allocate descriptor for character set conversion"
---

<h2 class="name">NAME</h2>
<p> iconv_open &#8211; allocate descriptor for character set conversion </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;iconv.h&gt;
iconv_t iconv_open(const char *tocode, const char *fromcode);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iconv_open</code>() function allocates a conversion descriptor suitable for converting byte sequences from character encoding <i>fromcode</i> to character encoding <i>tocode</i>. </p>
<p> The values permitted for <i>fromcode</i> and <i>tocode</i> and the supported combinations are system-dependent. For the GNU C library, the permitted values are listed by the <i>iconv &#8211;list</i> command, and all combinations of the listed values are supported. Furthermore the GNU C library and the GNU libiconv library support the following two suffixes:</p>
<dl>
<dt>//TRANSLIT</p>
<dd> When the string &quot;//TRANSLIT&quot; is appended to <i>tocode</i>, transliteration is activated. This means that when a character cannot be represented in the target character set, it can be approximated through one or several similarly looking characters.</p>
<dt>//IGNORE</p>
<dd> When the string &quot;//IGNORE&quot; is appended to <i>tocode</i>, characters that cannot be represented in the target character set will be silently discarded.</dl>
<p> The resulting conversion descriptor can be used with <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) any number of times. It remains valid until deallocated using <code><a href="/docs/linux/man/3-iconv_close/">iconv_close</a></code>(3). </p>
<p> A conversion descriptor contains a conversion state. After creation using <code>iconv_open</code>(), the state is in the initial state. Using <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) modifies the descriptor&#8217;s conversion state. To bring the state back to the initial state, use <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) with NULL as <i>inbuf</i> argument.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iconv_open</code>() function returns a freshly allocated conversion descriptor. In case of error, it sets <i>errno</i> and returns <i>(iconv_t)&nbsp;-1</i>.</p>
<h2>ERRORS</h2>
<p> The following error can occur, among others:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> The conversion from <i>fromcode</i> to <i>tocode</i> is not supported by the implementation.</dl>
<h2>VERSIONS</h2>
<p> This function is available in glibc since version 2.1.</p>
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
<td> <code>iconv_open</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-iconv_close/">iconv_close</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
