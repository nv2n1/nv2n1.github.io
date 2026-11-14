---
title: "pci_check_and_unmask_intx(9)"
name: "pci_check_and_unmask_intx"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_check_and_unmask_intx/"
description: "pci_check_and_unmask_intx – unmask INTx if no interrupt is pending"
---

<p>pci_check_and_unmask_intx &#8211; unmask INTx if no interrupt is pending</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_check_and_unmask_intx(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device to operate on</dl>
<h2>Description</h2>
<p>Check if the device dev has its INTx line asserted, unmask it if not and return true. False is returned and the mask remains active if there was still an interrupt pending.</p>
<h2>Copyright</h2>
