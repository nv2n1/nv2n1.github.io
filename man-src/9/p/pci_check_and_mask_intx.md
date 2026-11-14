---
title: "pci_check_and_mask_intx(9)"
name: "pci_check_and_mask_intx"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_check_and_mask_intx/"
description: "pci_check_and_mask_intx – mask INTx on pending interrupt"
---

<p>pci_check_and_mask_intx &#8211; mask INTx on pending interrupt</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_check_and_mask_intx(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device to operate on</dl>
<h2>Description</h2>
<p>Check if the device dev has its INTx line asserted, mask it and return true in that case. False is returned if not interrupt was pending.</p>
<h2>Copyright</h2>
