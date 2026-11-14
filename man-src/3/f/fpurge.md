---
title: "fpurge(3)"
name: "fpurge"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fpurge/"
description: "fpurge, __fpurge – purge a stream"
---

<h2 class="name">NAME</h2>
<p> fpurge, __fpurge &#8211; purge a stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
/* unsupported */
#include &lt;stdio.h&gt;
int fpurge(FILE *stream);
/* supported */
#include &lt;stdio.h&gt;
#include &lt;stdio_ext.h&gt;
void __fpurge(FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The function <code>fpurge</code>() clears the buffers of the given stream. For output streams this discards any unwritten output. For input streams this discards any input read from the underlying object but not yet obtained via <code><a href="/docs/linux/man/3-getc/">getc</a></code>(3); this includes any text pushed back via <code><a href="/docs/linux/man/3-ungetc/">ungetc</a></code>(3). See also <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3). </p>
<p> The function <code>__fpurge</code>() does precisely the same, but without returning a value.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion <code>fpurge</code>() returns 0. On error, it returns -1 and sets <i>errno</i> appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>stream</i> is not an open stream.</dl>
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
<td> <code>__fpurge</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:stream
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard and not portable. The function <code>fpurge</code>() was introduced in 4.4BSD and is not available under Linux. The function <code>__fpurge</code>() was introduced in Solaris, and is present in glibc 2.1.95 and later.</p>
<h2>NOTES</h2>
<p> Usually it is a mistake to want to discard input buffers.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3), <code><a href="/docs/linux/man/3-stdio_ext/">stdio_ext</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
