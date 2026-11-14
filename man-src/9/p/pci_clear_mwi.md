---
title: "pci_clear_mwi(9)"
name: "pci_clear_mwi"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_clear_mwi/"
---

pci_clear_mwi - disables Memory-Write-Invalidate for device dev

<h2>Synopsis</h2>

<pre><code>void pci_clear_mwi(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device to disable</dl>

<h2>Description</h2>

Disables PCI Memory-Write-Invalidate transaction on the device

<h2>Copyright</h2>


