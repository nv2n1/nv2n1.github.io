---
title: "iopl(2)"
name: "iopl"
section: "2"
letter: "i"
url: "/docs/linux/man/2-iopl/"
description: "iopl – change I/O privilege level"
---

<h2 class="name">NAME</h2>
<p> iopl &#8211; change I/O privilege level </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/io.h&gt;</code> </p>
<p> <code>int iopl(int </code><i>level</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>iopl</code>() changes the I/O privilege level of the calling thread, as specified by the two least significant bits in <i>level</i>. </p>
<p> The I/O privilege level for a normal thread is 0. Permissions are inherited from parents to children. </p>
<p> This call is deprecated, is significantly slower than <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), and is only provided for older X servers which require access to all 65536 I/O ports. It is mostly for the i386 architecture. On many other architectures it does not exist or will always return an error.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>level</i> is greater than 3.</p>
<dt><code>ENOSYS</code></p>
<dd> This call is unimplemented.</p>
<dt><code>EPERM</code></p>
<dd> The calling thread has insufficient privilege to call <code>iopl</code>(); the <code>CAP_SYS_RAWIO</code> capability is required to raise the I/O privilege level above its current value.</dl>
<h2>CONFORMING TO</h2>
<p> <code>iopl</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc2 has a prototype both in <i>&lt;sys/io.h&gt;</i> and in <i>&lt;sys/perm.h&gt;</i>. Avoid the latter, it is available on i386 only. </p>
<p> Prior to Linux 5.5 <code>iopl</code>() allowed the thread to disable interrupts while running at a higher I/O privilege level. This will probably crash the system, and is not recommended. </p>
<p> Prior to Linux 3.7, on some architectures (such as i386), permissions <i>were</i> inherited by the child produced by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and were preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). This behavior was inadvertently changed in Linux 3.7, and won&#8217;t be reinstated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), <code><a href="/docs/linux/man/2-outb/">outb</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
