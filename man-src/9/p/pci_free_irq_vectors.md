---
title: "pci_free_irq_vectors(9)"
name: "pci_free_irq_vectors"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_free_irq_vectors/"
description: "pci_free_irq_vectors – free previously allocated IRQs for a device"
---

<p>pci_free_irq_vectors &#8211; free previously allocated IRQs for a device</p>
<h2>Synopsis</h2>
<pre><code>void pci_free_irq_vectors(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to operate on</dl>
<h2>Description</h2>
<p>Undoes the allocations and enabling in <code>pci_alloc_irq_vectors</code>.</p>
<h2>Copyright</h2>
