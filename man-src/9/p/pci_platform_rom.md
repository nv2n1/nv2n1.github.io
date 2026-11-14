---
title: "pci_platform_rom(9)"
name: "pci_platform_rom"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_platform_rom/"
---

pci_platform_rom - provides a pointer to any ROM image provided by the platform

<h2>Synopsis</h2>

<pre><code>void __iomem *pci_platform_rom(struct pci_dev *pdev, size_t *size);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>pointer to pci device struct</dl>
 

 <i>size</i>
<dl><dd>pointer to receive size of pci window over ROM</dl>

<h2>Copyright</h2>


