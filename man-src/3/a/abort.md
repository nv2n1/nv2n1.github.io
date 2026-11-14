---
title: "abort(3)"
name: "abort"
section: "3"
letter: "a"
url: "/docs/linux/man/3-abort/"
description: "abort – cause abnormal process termination"
---

<h2 class="name">NAME</h2>
<p> abort &#8211; cause abnormal process termination </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
void abort(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>abort</code>() function first unblocks the <code>SIGABRT</code> signal, and then raises that signal for the calling process (as though <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3) was called). This results in the abnormal termination of the process unless the <code>SIGABRT</code> signal is caught and the signal handler does not return (see <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3)). </p>
<p> If the <code>SIGABRT</code> signal is ignored, or caught by a handler that returns, the <code>abort</code>() function will still terminate the process. It does this by restoring the default disposition for <code>SIGABRT</code> and then raising the signal for a second time.</p>
<h2>RETURN VALUE</h2>
<p> The <code>abort</code>() function never returns.</p>
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
<td> <code>abort</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4, POSIX.1-2001, POSIX.1-2008, 4.3BSD, C89, C99.</p>
<h2>NOTES</h2>
<p> Up until glibc 2.26, if the <code>abort</code>() function caused process termination, all open streams were closed and flushed (as with <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3)). However, in some cases this could result in deadlocks and data corruption. Therefore, starting with glibc 2.27, <code>abort</code>() terminates the process without flushing streams. POSIX.1 permits either possible behavior, saying that <code>abort</code>() &quot;may include an attempt to effect fclose() on all open streams&quot;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/3-assert/">assert</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
