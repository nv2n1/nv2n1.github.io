---
title: "pci_irq_get_affinity(9)"
name: "pci_irq_get_affinity"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_irq_get_affinity/"
---

pci_irq_get_affinity - return the affinity of a particular msi vector

<h2>Synopsis</h2>

<pre><code>const struct cpumask *pci_irq_get_affinity(struct pci_dev *dev, int nr);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to operate on</dl>
 

 <i>nr</i>
<dl><dd>device-relative interrupt vector index (0-based).</dl>

<h2>Copyright</h2>


