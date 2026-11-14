---
title: "fclose(3)"
name: "fclose"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclose/"
description: "fclose – close a stream"
---

<h2 class="name">NAME</h2>
<p> fclose &#8211; close a stream </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>int fclose(FILE *</code><i>stream</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>fclose</code>() function flushes the stream pointed to by <i>stream</i> (writing any buffered output data using <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3)) and closes the underlying file descriptor. </p>
<p> The behaviour of <code>fclose</code>() is undefined if the <i>stream</i> parameter is an illegal pointer, or is a descriptor already passed to a previous invocation of <code>fclose</code>().</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, 0 is returned. Otherwise, <code>EOF</code> is returned and <i>errno</i> is set to indicate the error. In either case, any further access (including another call to <code>fclose</code>()) to the stream results in undefined behavior.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> The file descriptor underlying <i>stream</i> is not valid.</dl>
<p> The <code>fclose</code>() function may also fail and set <i>errno</i> for any of the errors specified for the routines <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), or <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3).</p>
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
<td> <code>fclose</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99.</p>
<h2>NOTES</h2>
<p> Note that <code>fclose</code>() flushes only the user-space buffers provided by the C library. To ensure that the data is physically stored on disk the kernel buffers must be flushed too, for example, with <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) or <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/3-fcloseall/">fcloseall</a></code>(3), <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
