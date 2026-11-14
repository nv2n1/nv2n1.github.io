---
title: "fflush(3)"
name: "fflush"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fflush/"
description: "fflush – flush a stream"
---

<h2 class="name">NAME</h2>
<p> fflush &#8211; flush a stream </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>int fflush(FILE *</code><i>stream</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> For output streams, <code>fflush</code>() forces a write of all user-space buffered data for the given output or update <i>stream</i> via the stream&#8217;s underlying write function. </p>
<p> For input streams associated with seekable files (e.g., disk files, but not pipes or terminals), <code>fflush</code>() discards any buffered data that has been fetched from the underlying file, but has not been consumed by the application. </p>
<p> The open status of the stream is unaffected. </p>
<p> If the <i>stream</i> argument is NULL, <code>fflush</code>() flushes <i>all</i> open output streams. </p>
<p> For a nonlocking counterpart, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion 0 is returned. Otherwise, <code>EOF</code> is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>stream</i> is not an open stream, or is not open for writing.</dl>
<p> The function <code>fflush</code>() may also fail and set <i>errno</i> for any of the errors specified for <code><a href="/docs/linux/man/2-write/">write</a></code>(2).</p>
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
<td> <code>fflush</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C89, C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> POSIX.1-2001 did not specify the behavior for flushing of input streams, but the behavior is specified in POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Note that <code>fflush</code>() flushes only the user-space buffers provided by the C library. To ensure that the data is physically stored on disk the kernel buffers must be flushed too, for example, with <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) or <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
