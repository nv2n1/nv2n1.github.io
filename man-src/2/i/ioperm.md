---
title: "ioperm(2)"
name: "ioperm"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioperm/"
description: "ioperm – set port input/output permissions"
---

<h2 class="name">NAME</h2>
<p> ioperm &#8211; set port input/output permissions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/io.h&gt;</code> /* for glibc */ </p>
<p> <code>int ioperm(unsigned long </code><i>from</i><code>, unsigned long </code><i>num</i><code>, int </code><i>turn_on</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ioperm</code>() sets the port access permission bits for the calling thread for <i>num</i> bits starting from port address <i>from</i>. If <i>turn_on</i> is nonzero, then permission for the specified bits is enabled; otherwise it is disabled. If <i>turn_on</i> is nonzero, the calling thread must be privileged (<code>CAP_SYS_RAWIO</code>). </p>
<p> Before Linux 2.6.8, only the first 0x3ff I/O ports could be specified in this manner. For more ports, the <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2) system call had to be used (with a <i>level</i> argument of 3). Since Linux 2.6.8, 65,536 I/O ports can be specified. </p>
<p> Permissions are inherited by the child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) (but see NOTES). Permissions are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2); this is useful for giving port access permissions to unprivileged programs. </p>
<p> This call is mostly for the i386 architecture. On many other architectures it does not exist or will always return an error.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> Invalid values for <i>from</i> or <i>num</i>.</p>
<dt><code>EIO</code></p>
<dd> (on PowerPC) This call is not supported.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>EPERM</code></p>
<dd> The calling thread has insufficient privilege.</dl>
<h2>CONFORMING TO</h2>
<p> <code>ioperm</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> The <i>/proc/ioports</i> file shows the I/O ports that are currently allocated on the system. </p>
<p> Before Linux 2.4, permissions were not inherited by a child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> Glibc has an <code>ioperm</code>() prototype both in <i>&lt;sys/io.h&gt;</i> and in <i>&lt;sys/perm.h&gt;</i>. Avoid the latter, it is available on i386 only.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2), <code><a href="/docs/linux/man/2-outb/">outb</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
