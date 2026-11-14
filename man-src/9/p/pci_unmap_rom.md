---
title: "pci_unmap_rom(9)"
name: "pci_unmap_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_unmap_rom/"
---

pci_unmap_rom - unmap the ROM from kernel space

<h2>Synopsis</h2>

<pre><code>void pci_unmap_rom(struct pci_dev *pdev, void __iomem *rom);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>pointer to pci device struct</dl>
 

 <i>rom</i>
<dl><dd>virtual address of the previous mapping</dl>

<h2>Description</h2>

Remove a mapping of a previously mapped ROM

<h2>Copyright</h2>


