---
title: "fileno(3)"
name: "fileno"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fileno/"
description: "clearerr, feof, ferror, fileno – check and reset stream status"
---

<h2 class="name">NAME</h2>
<p> clearerr, feof, ferror, fileno &#8211; check and reset stream status </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>void clearerr(FILE *</code><i>stream</i><code>);</code> </p>
<p> <code>int feof(FILE *</code><i>stream</i><code>);</code> </p>
<p> <code>int ferror(FILE *</code><i>stream</i><code>);</code> </p>
<p> <code>int fileno(FILE *</code><i>stream</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fileno</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The function <code>clearerr</code>() clears the end-of-file and error indicators for the stream pointed to by <i>stream</i>. </p>
<p> The function <code>feof</code>() tests the end-of-file indicator for the stream pointed to by <i>stream</i>, returning nonzero if it is set. The end-of-file indicator can be cleared only by the function <code>clearerr</code>(). </p>
<p> The function <code>ferror</code>() tests the error indicator for the stream pointed to by <i>stream</i>, returning nonzero if it is set. The error indicator can be reset only by the <code>clearerr</code>() function. </p>
<p> The function <code>fileno</code>() examines the argument <i>stream</i> and returns the integer file descriptor used to implement this stream. The file descriptor is still owned by <i>stream</i> and will be closed when <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3) is called. Duplicate the file descriptor with <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) before passing it to code that might close it. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>ERRORS</h2>
<p> These functions should not fail and do not set the external variable <i>errno</i>. (However, in case <code>fileno</code>() detects that its argument is not a valid stream, it must return -1 and set <i>errno</i> to <code>EBADF</code>.)</p>
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
<td> <code>clearerr</code>(), <code>feof</code>(),<br />
 <code>ferror</code>(), <code>fileno</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The functions <code>clearerr</code>(), <code>feof</code>(), and <code>ferror</code>() conform to C89, C99, POSIX.1-2001, and POSIX.1-2008. </p>
<p> The function <code>fileno</code>() conforms to POSIX.1-2001 and POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3), <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
