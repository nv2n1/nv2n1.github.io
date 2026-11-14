---
title: "stdio_ext(3)"
name: "stdio_ext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdio_ext/"
description: "__fbufsize, __flbf, __fpending, __fpurge, __freadable, __freading, __fsetlocking, __fwritable, __fwriting, _flushlbf – interfaces to stdio FILE structure"
---

<p>__fbufsize, __flbf, __fpending, __fpurge, __freadable, __freading, __fsetlocking, __fwritable, __fwriting, _flushlbf &#8211; interfaces to stdio FILE structure</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;stdio_ext.h&gt;

size_t __fbufsize(FILE *stream);
size_t __fpending(FILE *stream);
int __flbf(FILE *stream);
int __freadable(FILE *stream);
int __fwritable(FILE *stream);
int __freading(FILE *stream);
int __fwriting(FILE *stream);
int __fsetlocking(FILE *stream, int type);
void _flushlbf(void);
void __fpurge(FILE *stream);</code></pre>
<h2>Description</h2>
<p>Solaris introduced routines to allow portable access to the internals of the <i>FILE</i> structure, and glibc also implemented these. </p>
<p> The <code>__fbufsize</code>() function returns the size of the buffer currently used by the given stream. </p>
<p> The <code>__fpending</code>() function returns the number of bytes in the output buffer. For wide-oriented streams the unit is wide characters. This function is undefined on buffers in reading mode, or opened read-only. </p>
<p> The <code>__flbf</code>() function returns a nonzero value if the stream is line-buffered, and zero otherwise. </p>
<p> The <code>__freadable</code>() function returns a nonzero value if the stream allows reading, and zero otherwise. </p>
<p> The <code>__fwritable</code>() function returns a nonzero value if the stream allows writing, and zero otherwise. </p>
<p> The <code>__freading</code>() function returns a nonzero value if the stream is read-only, or if the last operation on the stream was a read operation, and zero otherwise. </p>
<p> The <code>__fwriting</code>() function returns a nonzero value if the stream is write-only (or append-only), or if the last operation on the stream was a write operation, and zero otherwise. </p>
<p> The <code>__fsetlocking</code>() function can be used to select the desired type of locking on the stream. It returns the current type. The <i>type</i> argument can take the following three values:</p>
<dl>
<dt><code>FSETLOCKING_INTERNAL</code></p>
<dd>Perform implicit locking around every operation on the given stream (except for the *_unlocked ones). This is the default.</p>
<dt><code>FSETLOCKING_BYCALLER</code></p>
<dd>The caller will take care of the locking (possibly using <code><a href="/docs/linux/man/3-flockfile/">flockfile</a></code>(3) in case there is more than one thread), and the stdio routines will not do locking until the state is reset to <code>FSETLOCKING_INTERNAL</code>.</p>
<dt><code>FSETLOCKING_QUERY</code></p>
<dd>Don&#8217;t change the type of locking. (Only return it.)</dl>
<p> The <code>_flushlbf</code>() function flushes all line-buffered streams. (Presumably so that output to a terminal is forced out, say before reading keyboard input.) </p>
<p> The <code>__fpurge</code>() function discards the contents of the stream&#8217;s buffer.</p>
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
<td> <code>__fbufsize</code>(), <code>__fpending</code>(),<br />
 <code>__fpurge</code>(), <code>__fsetlocking</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:stream
</td>
</tr>
<tr VALIGN=top>
<td> <code>__flbf</code>(), <code>__freadable</code>(),<br />
 <code>__freading</code>(), <code>__fwritable</code>(),<br />
 <code>__fwriting</code>(), <code>_flushlbf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-flockfile/">flockfile</a></code>(3), <code><a href="/docs/linux/man/3-fpurge/">fpurge</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
