---
title: "pciconfig_read(2)"
name: "pciconfig_read"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pciconfig_read/"
description: "pciconfig_read, pciconfig_write, pciconfig_iobase – pci device information handling"
---

<h2 class="name">NAME</h2>
<p> pciconfig_read, pciconfig_write, pciconfig_iobase &#8211; pci device information handling </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;pci.h&gt;
int pciconfig_read(unsigned long bus, unsigned long dfn,
                   unsigned long off, unsigned long len, void *buf);
int pciconfig_write(unsigned long bus, unsigned long dfn,
                    unsigned long off, unsigned long len, void *buf);
int pciconfig_iobase(long which, unsigned long bus,
                     unsigned long devfn);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Most of the interaction with PCI devices is already handled by the kernel PCI layer, and thus these calls should not normally need to be accessed from user space.</p>
<dl>
<dt><code>pciconfig_read</code>()</p>
<dd> Reads to <i>buf</i> from device <i>dev</i> at offset <i>off</i> value.</p>
<dt><code>pciconfig_write</code>()</p>
<dd> Writes from <i>buf</i> to device <i>dev</i> at offset <i>off</i> value.</p>
<dt><code>pciconfig_iobase</code>()</p>
<dd> You pass it a bus/devfn pair and get a physical address for either the memory offset (for things like prep, this is 0xc0000000), the IO base for PIO cycles, or the ISA holes if any.</dl>
<h2>RETURN VALUE</h2>
<dl>
<dt><code>pciconfig_read</code>()</p>
<dd> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<dt><code>pciconfig_write</code>()</p>
<dd> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<dt><code>pciconfig_iobase</code>()</p>
<dd> Returns information on locations of various I/O regions in physical memory according to the <i>which</i> value. Values for <i>which</i> are: <code>IOBASE_BRIDGE_NUMBER</code>, <code>IOBASE_MEMORY</code>, <code>IOBASE_IO</code>, <code>IOBASE_ISA_IO</code>, <code>IOBASE_ISA_MEM</code>.</dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>len</i> value is invalid. This does not apply to <code>pciconfig_iobase</code>().</p>
<dt><code>EIO</code></p>
<dd> I/O error.</p>
<dt><code>ENODEV</code></p>
<dd> For <code>pciconfig_iobase</code>(), &quot;hose&quot; value is NULL. For the other calls, could not find a slot.</p>
<dt><code>ENOSYS</code></p>
<dd> The system has not implemented these calls (<code>CONFIG_PCI</code> not defined).</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> This return value is valid only for <code>pciconfig_iobase</code>(). It is returned if the value for <i>which</i> is invalid.</p>
<dt><code>EPERM</code></p>
<dd> User does not have the <code>CAP_SYS_ADMIN</code> capability. This does not apply to <code>pciconfig_iobase</code>().</dl>
<h2>CONFORMING TO</h2>
<p> These calls are Linux-specific, available since Linux 2.0.26/2.1.11.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
