---
title: "fseeko(3)"
name: "fseeko"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fseeko/"
description: "fseeko, ftello – seek to or report file position"
---

<h2 class="name">NAME</h2>
<p> fseeko, ftello &#8211; seek to or report file position </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
int fseeko(FILE *stream, off_t offset, int whence);
off_t ftello(FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fseeko</code>(), <code>ftello</code>(): </p>
<dl>
<dt>
<dd> _FILE_OFFSET_BITS&nbsp;==&nbsp;64 || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
 (defining the obsolete _LARGEFILE_SOURCE macro also works)</dl>
<h2>DESCRIPTION</h2>
<p> The <code>fseeko</code>() and <code>ftello</code>() functions are identical to <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) and <code><a href="/docs/linux/man/3-ftell/">ftell</a></code>(3) (see <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3)), respectively, except that the <i>offset</i> argument of <code>fseeko</code>() and the return value of <code>ftello</code>() is of type <i>off_t</i> instead of <i>long</i>. </p>
<p> On some architectures, both <i>off_t</i> and <i>long</i> are 32-bit types, but defining <code>_FILE_OFFSET_BITS</code> with the value 64 (before including <i>any</i> header files) will turn <i>off_t</i> into a 64-bit type.</p>
<h2>RETURN VALUE</h2>
<p> On successful completion, <code>fseeko</code>() returns 0, while <code>ftello</code>() returns the current offset. Otherwise, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> See the ERRORS in <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> These functions are available under glibc since version 2.1.</p>
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
<td> <code>fseeko</code>(), <code>ftello</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
