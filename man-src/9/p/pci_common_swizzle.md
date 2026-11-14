---
title: "pci_common_swizzle(9)"
name: "pci_common_swizzle"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_common_swizzle/"
description: "pci_common_swizzle – swizzle INTx all the way to root bridge"
---

<p>pci_common_swizzle &#8211; swizzle INTx all the way to root bridge</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 pci_common_swizzle(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, u8&nbsp;<wbr>*&nbsp;<wbr></code><i>pinp</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device</dl>
<p> <i>pinp</i></p>
<dl>
<dd>pointer to the INTx pin value (1=INTA, 2=INTB, 3=INTD, 4=INTD)</dl>
<h2>Description</h2>
<p>Perform INTx swizzling for a device. This traverses through all PCI-to-PCI bridges all the way up to a PCI root bus.</p>
<h2>Copyright</h2>
