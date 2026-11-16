---
title: "pci_write_vpd(9)"
name: "pci_write_vpd"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_write_vpd/"
description: "pci_write_vpd – Write entry to Vital Product Data"
---

<p>pci_write_vpd &#8211; Write entry to Vital Product Data</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t pci_write_vpd(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, loff_t&nbsp;<wbr></code><i>pos</i><code>, size_t&nbsp;<wbr></code><i>count</i><code>, const void&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>);</code></dt></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
</dd><dd>pci device struct</dd></dl>
<p> <i>pos</i></p>
<dl>
<dd>offset in vpd space</dd></dl>
<p> <i>count</i></p>
<dl>
<dd>number of bytes to write</dd></dl>
<p> <i>buf</i></p>
<dl>
<dd>buffer containing write data</dd></dl>
<h2>Copyright</h2>
