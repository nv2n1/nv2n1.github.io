---
title: "s390_pci_mmio_read(2)"
name: "s390_pci_mmio_read"
section: "2"
letter: "s"
url: "/docs/linux/man/2-s390_pci_mmio_read/"
description: "s390_pci_mmio_write, s390_pci_mmio_read – transfer data to/from PCI MMIO memory page"
---

<h2 class="name">NAME</h2>
<p> s390_pci_mmio_write, s390_pci_mmio_read &#8211; transfer data to/from PCI MMIO memory page </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/unistd.h&gt;
int s390_pci_mmio_write(unsigned long mmio_addr,
                        void *user_buffer, size_t length);
int s390_pci_mmio_read(unsigned long mmio_addr,
                       void *user_buffer, size_t length);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>s390_pci_mmio_write</code>() system call writes <i>length</i> bytes of data from the user-space buffer <i>user_buffer</i> to the PCI MMIO memory location specified by <i>mmio_addr</i>. The <code>s390_pci_mmio_read</code>() system call reads <i>length</i> bytes of data from the PCI MMIO memory location specified by <i>mmio_addr</i> to the user-space buffer <i>user_buffer</i>. </p>
<p> These system calls must be used instead of the simple assignment or data-transfer operations that are used to access the PCI MMIO memory areas mapped to user space on the Linux System z platform. The address specified by <i>mmio_addr</i> must belong to a PCI MMIO memory page mapping in the caller&#8217;s address space, and the data being written or read must not cross a page boundary. The <i>length</i> value cannot be greater than the system page size.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>s390_pci_mmio_write</code>() and <code>s390_pci_mmio_read</code>() return 0. On error, -1 is returned and <i>errno</i> is set to one of the error codes listed below.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The address in <i>mmio_addr</i> is invalid.</p>
<dt><code>EFAULT</code></p>
<dd> <i>user_buffer</i> does not point to a valid location in the caller&#8217;s address space.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid <i>length</i> argument.</p>
<dt><code>ENODEV</code></p>
<dd> PCI support is not enabled.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory.</dl>
<h2>VERSIONS</h2>
<p> These system calls are available since Linux 3.19.</p>
<h2>CONFORMING TO</h2>
<p> This Linux-specific system call is available only on the s390 architecture. The required PCI support is available beginning with System z EC12.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) to call it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
