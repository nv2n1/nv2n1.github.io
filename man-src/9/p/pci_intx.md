---
title: "pci_intx(9)"
name: "pci_intx"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_intx/"
---

pci_intx - enables/disables PCI INTx for device dev

<h2>Synopsis</h2>

<pre><code>void pci_intx(struct pci_dev *pdev, int enable);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>the PCI device to operate on</dl>
 

 <i>enable</i>
<dl><dd>boolean: whether to enable or disable PCI INTx</dl>

<h2>Description</h2>

Enables/disables PCI INTx for device dev

<h2>Copyright</h2>


