---
title: "pci_enable_rom(9)"
name: "pci_enable_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_rom/"
---

pci_enable_rom - enable ROM decoding for a PCI device

<h2>Synopsis</h2>

<pre><code>int pci_enable_rom(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device to enable</dl>

<h2>Description</h2>

Enable ROM decoding on <i>dev</i>. This involves simply turning on the last bit of the PCI ROM BAR. Note that some cards may share address decoders between the ROM and other resources, so enabling it may disable access to MMIO registers or other card memory.

<h2>Copyright</h2>


