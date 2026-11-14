---
title: "pci_map_rom(9)"
name: "pci_map_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_map_rom/"
---

pci_map_rom - map a PCI ROM to kernel space

<h2>Synopsis</h2>

<pre><code>void __iomem *pci_map_rom(struct pci_dev *pdev, size_t *size);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>pointer to pci device struct</dl>
 

 <i>size</i>
<dl><dd>pointer to receive size of pci window over ROM</dl>

<h2>Return</h2>

kernel virtual pointer to image of ROM 

 Map a PCI ROM into kernel space. If ROM is boot video ROM, the shadow BIOS copy will be returned instead of the actual ROM.

<h2>Copyright</h2>


