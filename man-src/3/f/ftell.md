---
title: "ftell(3)"
name: "ftell"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ftell/"
description: "fgetpos, fseek, fsetpos, ftell, rewind – reposition a stream"
---

<h2 class="name">NAME</h2>
<p> fgetpos, fseek, fsetpos, ftell, rewind &#8211; reposition a stream </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>int fseek(FILE *</code><i>stream</i><code>, long </code><i>offset</i><code>, int </code><i>whence</i><code>);</code> </p>
<p> <code>long ftell(FILE *</code><i>stream</i><code>);</code> </p>
<p> <code>void rewind(FILE *</code><i>stream</i><code>);</code> </p>
<p> <code>int fgetpos(FILE *</code><i>stream</i><code>, fpos_t *</code><i>pos</i><code>);</code> </p>
<p> <code>int fsetpos(FILE *</code><i>stream</i><code>, const fpos_t *</code><i>pos</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>fseek</code>() function sets the file position indicator for the stream pointed to by <i>stream</i>. The new position, measured in bytes, is obtained by adding <i>offset</i> bytes to the position specified by <i>whence</i>. If <i>whence</i> is set to <code>SEEK_SET</code>, <code>SEEK_CUR</code>, or <code>SEEK_END</code>, the offset is relative to the start of the file, the current position indicator, or end-of-file, respectively. A successful call to the <code>fseek</code>() function clears the end-of-file indicator for the stream and undoes any effects of the <code><a href="/docs/linux/man/3-ungetc/">ungetc</a></code>(3) function on the same stream. </p>
<p> The <code>ftell</code>() function obtains the current value of the file position indicator for the stream pointed to by <i>stream</i>. </p>
<p> The <code>rewind</code>() function sets the file position indicator for the stream pointed to by <i>stream</i> to the beginning of the file. It is equivalent to: </p>
<dl>
<dt>
<dd> (void) fseek(stream, 0L, SEEK_SET)</dl>
<p> except that the error indicator for the stream is also cleared (see <code><a href="/docs/linux/man/3-clearerr/">clearerr</a></code>(3)). </p>
<p> The <code>fgetpos</code>() and <code>fsetpos</code>() functions are alternate interfaces equivalent to <code>ftell</code>() and <code>fseek</code>() (with <i>whence</i> set to <code>SEEK_SET</code>), setting and storing the current value of the file offset into or from the object referenced by <i>pos</i>. On some non-UNIX systems, an <i>fpos_t</i> object may be a complex object and these routines may be the only way to portably reposition a text stream.</p>
<h2>RETURN VALUE</h2>
<p> The <code>rewind</code>() function returns no value. Upon successful completion, <code>fgetpos</code>(), <code>fseek</code>(), <code>fsetpos</code>() return 0, and <code>ftell</code>() returns the current offset. Otherwise, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>whence</i> argument to <code>fseek</code>() was not <code>SEEK_SET</code>, <code>SEEK_END</code>, or <code>SEEK_CUR</code>. Or: the resulting file offset would be negative.</p>
<dt><code>ESPIPE</code></p>
<dd> The file descriptor underlying <i>stream</i> is not seekable (e.g., it refers to a pipe, FIFO, or socket).</dl>
<p> The functions <code>fgetpos</code>(), <code>fseek</code>(), <code>fsetpos</code>(), and <code>ftell</code>() may also fail and set <i>errno</i> for any of the errors specified for the routines <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), and <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3).</p>
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
<td> <code>fseek</code>(), <code>ftell</code>(), <code>rewind</code>(),<br />
 <code>fgetpos</code>(), <code>fsetpos</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/3-fseeko/">fseeko</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
