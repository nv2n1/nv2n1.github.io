---
title: "raise(3)"
name: "raise"
section: "3"
letter: "r"
url: "/docs/linux/man/3-raise/"
description: "raise – send a signal to the caller"
---

<p>raise &#8211; send a signal to the caller</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int raise(int sig);</code></pre>
<h2>Description</h2>
<p>The <code>raise</code>() function sends a signal to the calling process or thread. In a single-threaded program it is equivalent to </p>
<p> kill(getpid(), sig); </p>
<p> In a multithreaded program it is equivalent to </p>
<p> pthread_kill(pthread_self(), sig); </p>
<p> If the signal causes a handler to be called, <code>raise</code>() will return only after the signal handler has returned.</p>
<h2>Return Value</h2>
<p><code>raise</code>() returns 0 on success, and nonzero for failure.</p>
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
<td> <code>raise</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99.</p>
<h2>Notes</h2>
<p>Since version 2.3.3, glibc implements <code>raise</code>() by calling <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), if the kernel supports that system call. Older glibc versions implemented <code>raise</code>() using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
