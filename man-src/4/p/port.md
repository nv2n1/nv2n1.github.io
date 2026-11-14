---
title: "port(4)"
name: "port"
section: "4"
letter: "p"
url: "/docs/linux/man/4-port/"
description: "mem, kmem, port – system memory, kernel memory and system ports"
---

<p>mem, kmem, port &#8211; system memory, kernel memory and system ports</p>
<h2>Description</h2>
<p><i>/dev/mem</i> is a character device file that is an image of the main memory of the computer. It may be used, for example, to examine (and even patch) the system. </p>
<p> Byte addresses in <i>/dev/mem</i> are interpreted as physical memory addresses. References to nonexistent locations cause errors to be returned. </p>
<p> Examining and patching is likely to lead to unexpected results when read-only or write-only bits are present. </p>
<p> Since Linux 2.6.26, and depending on the architecture, the <code>CONFIG_STRICT_DEVMEM</code> kernel configuration option limits the areas which can be accessed through this file. For example: on x86, RAM access is not allowed but accessing memory-mapped PCI regions is. </p>
<p> It is typically created by: </p>
<p> mknod -m 660 /dev/mem c 1 1 chown root:kmem /dev/mem </p>
<p> The file <i>/dev/kmem</i> is the same as <i>/dev/mem</i>, except that the kernel virtual memory rather than physical memory is accessed. Since Linux 2.6.26, this file is available only if the <code>CONFIG_DEVKMEM</code> kernel configuration option is enabled. </p>
<p> It is typically created by: </p>
<p> mknod -m 640 /dev/kmem c 1 2 chown root:kmem /dev/kmem </p>
<p> <i>/dev/port</i> is similar to <i>/dev/mem</i>, but the I/O ports are accessed. </p>
<p> It is typically created by: </p>
<p> mknod -m 660 /dev/port c 1 4 chown root:kmem /dev/port</p>
<h2>Files</h2>
<p><i>/dev/mem</i><br />
 <i>/dev/kmem</i><br />
 <i>/dev/port</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
