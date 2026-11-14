---
title: "bdflush(2)"
name: "bdflush"
section: "2"
letter: "b"
url: "/docs/linux/man/2-bdflush/"
description: "bdflush – start, flush, or tune buffer-dirty-flush daemon"
---

<h2 class="name">NAME</h2>
<p> bdflush &#8211; start, flush, or tune buffer-dirty-flush daemon </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/kdaemon.h&gt;
int bdflush(int func, long *address);
int bdflush(int func, long data);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: Since Linux 2.6, this system call is deprecated and does nothing. It is likely to disappear altogether in a future kernel release. Nowadays, the task performed by <code>bdflush</code>() is handled by the kernel <i>pdflush</i> thread. </p>
<p> <code>bdflush</code>() starts, flushes, or tunes the buffer-dirty-flush daemon. Only a privileged process (one with the <code>CAP_SYS_ADMIN</code> capability) may call <code>bdflush</code>(). </p>
<p> If <i>func</i> is negative or 0, and no daemon has been started, then <code>bdflush</code>() enters the daemon code and never returns. </p>
<p> If <i>func</i> is 1, some dirty buffers are written to disk. </p>
<p> If <i>func</i> is 2 or more and is even (low bit is 0), then <i>address</i> is the address of a long word, and the tuning parameter numbered (<i>func</i>-2)/2 is returned to the caller in that address. </p>
<p> If <i>func</i> is 3 or more and is odd (low bit is 1), then <i>data</i> is a long word, and the kernel sets tuning parameter numbered (<i>func</i>-3)/2 to that value. </p>
<p> The set of parameters, their values, and their valid ranges are defined in the Linux kernel source file <i>fs/buffer.c</i>.</p>
<h2>RETURN VALUE</h2>
<p> If <i>func</i> is negative or 0 and the daemon successfully starts, <code>bdflush</code>() never returns. Otherwise, the return value is 0 on success and -1 on failure, with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBUSY</code></p>
<dd> An attempt was made to enter the daemon code after another process has already entered.</p>
<dt><code>EFAULT</code></p>
<dd> <i>address</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> An attempt was made to read or write an invalid parameter number, or to write an invalid value to a parameter.</p>
<dt><code>EPERM</code></p>
<dd> Caller does not have the <code>CAP_SYS_ADMIN</code> capability.</dl>
<h2>VERSIONS</h2>
<p> Since version 2.23, glibc no longer supports this obsolete system call.</p>
<h2>CONFORMING TO</h2>
<p> <code>bdflush</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
