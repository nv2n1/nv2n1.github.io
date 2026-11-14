---
title: "pci_disable_rom(9)"
name: "pci_disable_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_disable_rom/"
---

pci_disable_rom - disable ROM decoding for a PCI device

<h2>Synopsis</h2>

<pre><code>void pci_disable_rom(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device to disable</dl>

<h2>Description</h2>

Disable ROM decoding on a PCI device by turning off the last bit in the ROM BAR.

<h2>Copyright</h2>


