---
title: "iconv_close(3)"
name: "iconv_close"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iconv_close/"
description: "iconv_close – deallocate descriptor for character set conversion"
---

<h2 class="name">NAME</h2>
<p> iconv_close &#8211; deallocate descriptor for character set conversion </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;iconv.h&gt;
int iconv_close(iconv_t cd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iconv_close</code>() function deallocates a conversion descriptor <i>cd</i> previously allocated using <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> When successful, the <code>iconv_close</code>() function returns 0. In case of error, it sets <i>errno</i> and returns -1.</p>
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
<td> <code>iconv_close</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
