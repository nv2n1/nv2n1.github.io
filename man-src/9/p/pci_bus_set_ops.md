---
title: "pci_bus_set_ops(9)"
name: "pci_bus_set_ops"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_bus_set_ops/"
---

pci_bus_set_ops - Set raw operations of pci bus

<h2>Synopsis</h2>

<pre><code>struct pci_ops *pci_bus_set_ops(struct pci_bus *bus, struct pci_ops *ops);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>pci bus struct</dl>
 

 <i>ops</i>
<dl><dd>new raw operations</dl>

<h2>Description</h2>

Return previous raw operations

<h2>Copyright</h2>


