---
title: "tmpfile(3)"
name: "tmpfile"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tmpfile/"
description: "tmpfile – create a temporary file"
---

<p>tmpfile &#8211; create a temporary file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

FILE *tmpfile(void);</code></pre>
<h2>Description</h2>
<p>The <code>tmpfile</code>() function opens a unique temporary file in binary read/write (w+b) mode. The file will be automatically deleted when it is closed or the program terminates.</p>
<h2>Return Value</h2>
<p>The <code>tmpfile</code>() function returns a stream descriptor, or NULL if a unique filename cannot be generated or the unique file cannot be opened. In the latter case, <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>Search permission denied for directory in file&#8217;s path prefix.</p>
<dt><code>EEXIST</code></p>
<dd>Unable to generate a unique filename.</p>
<dt><code>EINTR</code></p>
<dd>The call was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EMFILE</code></p>
<dd>The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd>The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOSPC</code></p>
<dd>There was no room in the directory to add the new filename.</p>
<dt><code>EROFS</code></p>
<dd>Read-only filesystem.</dl>
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
<td> <code>tmpfile</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD, SUSv2.</p>
<h2>Notes</h2>
<p>POSIX.1-2001 specifies: an error message may be written to <i>stdout</i> if the stream cannot be opened. </p>
<p> The standard does not specify the directory that <code>tmpfile</code>() will use. Glibc will try the path prefix <i>P_tmpdir</i> defined in <i>&lt;stdio.h&gt;</i>, and if that fails the directory <i>/tmp</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
