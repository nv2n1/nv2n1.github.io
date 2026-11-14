---
title: "pci_intx_mask_supported(9)"
name: "pci_intx_mask_supported"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_intx_mask_supported/"
description: "pci_intx_mask_supported – probe for INTx masking support"
---

<p>pci_intx_mask_supported &#8211; probe for INTx masking support</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_intx_mask_supported(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device to operate on</dl>
<h2>Description</h2>
<p>Check if the device dev support INTx masking via the config space command word.</p>
<h2>Copyright</h2>
