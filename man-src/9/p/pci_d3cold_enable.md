---
title: "pci_d3cold_enable(9)"
name: "pci_d3cold_enable"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_d3cold_enable/"
---

pci_d3cold_enable - Enable D3cold for device

<h2>Synopsis</h2>

<pre><code>void pci_d3cold_enable(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to handle</dl>

<h2>Description</h2>

This function can be used in drivers to enable D3cold from the device they handle. It also updates upstream PCI bridge PM capabilities accordingly.

<h2>Copyright</h2>


