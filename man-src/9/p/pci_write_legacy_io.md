---
title: "pci_write_legacy_io(9)"
name: "pci_write_legacy_io"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_write_legacy_io/"
description: "pci_write_legacy_io – write byte(s) to legacy I/O port space"
---

<p>pci_write_legacy_io &#8211; write byte(s) to legacy I/O port space</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t pci_write_legacy_io(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>filp</i><code>, struct kobject&nbsp;<wbr>*&nbsp;<wbr></code><i>kobj</i><code>, struct bin_attribute&nbsp;<wbr>*&nbsp;<wbr></code><i>bin_attr</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, loff_t&nbsp;<wbr></code><i>off</i><code>, size_t&nbsp;<wbr></code><i>count</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>open sysfs file</dl>
<p> <i>kobj</i></p>
<dl>
<dd>kobject corresponding to file to read from</dl>
<p> <i>bin_attr</i></p>
<dl>
<dd>struct bin_attribute for this file</dl>
<p> <i>buf</i></p>
<dl>
<dd>buffer containing value to be written</dl>
<p> <i>off</i></p>
<dl>
<dd>offset into legacy I/O port space</dl>
<p> <i>count</i></p>
<dl>
<dd>number of bytes to write</dl>
<h2>Description</h2>
<p>Writes 1, 2, or 4 bytes from legacy I/O port space using an arch specific callback routine (pci_legacy_write).</p>
<h2>Copyright</h2>
