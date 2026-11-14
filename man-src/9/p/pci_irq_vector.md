---
title: "pci_irq_vector(9)"
name: "pci_irq_vector"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_irq_vector/"
---

pci_irq_vector - return Linux IRQ number of a device vector

<h2>Synopsis</h2>

<pre><code>int pci_irq_vector(struct pci_dev *dev, unsigned int nr);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to operate on</dl>
 

 <i>nr</i>
<dl><dd>device-relative interrupt vector index (0-based).</dl>

<h2>Copyright</h2>


