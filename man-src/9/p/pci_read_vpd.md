---
title: "pci_read_vpd(9)"
name: "pci_read_vpd"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_read_vpd/"
description: "pci_read_vpd – Read one entry from Vital Product Data"
---

<p>pci_read_vpd &#8211; Read one entry from Vital Product Data</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t pci_read_vpd(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, loff_t&nbsp;<wbr></code><i>pos</i><code>, size_t&nbsp;<wbr></code><i>count</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>pci device struct</dl>
<p> <i>pos</i></p>
<dl>
<dd>offset in vpd space</dl>
<p> <i>count</i></p>
<dl>
<dd>number of bytes to read</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to where to store result</dl>
<h2>Copyright</h2>
