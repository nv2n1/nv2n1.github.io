---

title: "pciconfig_read(2)"
name: "pciconfig_read"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pciconfig_read/"
description: "pciconfig_read, pciconfig_write, pciconfig_iobase – pci device information handling"
---

<pre><code>
#include &lt;pci.h&gt;
int pciconfig_read(unsigned long bus, unsigned long dfn,
                   unsigned long off, unsigned long len, void *buf);
int pciconfig_write(unsigned long bus, unsigned long dfn,
                    unsigned long off, unsigned long len, void *buf);
int pciconfig_iobase(long which, unsigned long bus,
                     unsigned long devfn);
</code></pre>
<p> Most of the interaction with PCI devices is already handled by the kernel PCI layer, and thus these calls should not normally need to be accessed from user space.</p>
<dl>
<dt><code>pciconfig_read</code>()</dt>
<dd> Reads to <i>buf</i> from device <i>dev</i> at offset <i>off</i> value.</dd>
<dt><code>pciconfig_write</code>()</dt>
<dd> Writes from <i>buf</i> to device <i>dev</i> at offset <i>off</i> value.</dd>
<dt><code>pciconfig_iobase</code>()</dt>
<dd> You pass it a bus/devfn pair and get a physical address for either the memory offset (for things like prep, this is 0xc0000000), the IO base for PIO cycles, or the ISA holes if any.</dd></dl>
<h2>RETURN VALUE</h2>
<dl>
<dt><code>pciconfig_read</code>()</dt>
<dd> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</dd>
<dt><code>pciconfig_write</code>()</dt>
<dd> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</dd>
<dt><code>pciconfig_iobase</code>()</dt>
<dd> Returns information on locations of various I/O regions in physical memory according to the <i>which</i> value. Values for <i>which</i> are: <code>IOBASE_BRIDGE_NUMBER</code>, <code>IOBASE_MEMORY</code>, <code>IOBASE_IO</code>, <code>IOBASE_ISA_IO</code>, <code>IOBASE_ISA_MEM</code>.</dd></dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> <i>len</i> value is invalid. This does not apply to <code>pciconfig_iobase</code>().</dd>
<dt><code>EIO</code></dt>
<dd> I/O error.</dd>
<dt><code>ENODEV</code></dt>
<dd> For <code>pciconfig_iobase</code>(), &quot;hose&quot; value is NULL. For the other calls, could not find a slot.</dd>
<dt><code>ENOSYS</code></dt>
<dd> The system has not implemented these calls (<code>CONFIG_PCI</code> not defined).</dd>
<dt><code>EOPNOTSUPP</code></dt>
<dd> This return value is valid only for <code>pciconfig_iobase</code>(). It is returned if the value for <i>which</i> is invalid.</dd>
<dt><code>EPERM</code></dt>
<dd> User does not have the <code>CAP_SYS_ADMIN</code> capability. This does not apply to <code>pciconfig_iobase</code>().</dd></dl>
<h2>CONFORMING TO</h2>
<p> These calls are Linux-specific, available since Linux 2.0.26/2.1.11.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
