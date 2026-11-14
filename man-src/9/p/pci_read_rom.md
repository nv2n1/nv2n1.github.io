---
title: "pci_read_rom(9)"
name: "pci_read_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_read_rom/"
description: "pci_read_rom – read a PCI ROM"
---

<p>pci_read_rom &#8211; read a PCI ROM</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t pci_read_rom(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>filp</i><code>, struct kobject&nbsp;<wbr>*&nbsp;<wbr></code><i>kobj</i><code>, struct bin_attribute&nbsp;<wbr>*&nbsp;<wbr></code><i>bin_attr</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, loff_t&nbsp;<wbr></code><i>off</i><code>, size_t&nbsp;<wbr></code><i>count</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>sysfs file</dl>
<p> <i>kobj</i></p>
<dl>
<dd>kernel object handle</dl>
<p> <i>bin_attr</i></p>
<dl>
<dd>struct bin_attribute for this file</dl>
<p> <i>buf</i></p>
<dl>
<dd>where to put the data we read from the ROM</dl>
<p> <i>off</i></p>
<dl>
<dd>file offset</dl>
<p> <i>count</i></p>
<dl>
<dd>number of bytes to read</dl>
<h2>Description</h2>
<p>Put <i>count</i> bytes starting at <i>off</i> into <i>buf</i> from the ROM in the PCI device corresponding to <i>kobj</i>.</p>
<h2>Copyright</h2>
