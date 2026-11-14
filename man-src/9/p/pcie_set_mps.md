---
title: "pcie_set_mps(9)"
name: "pcie_set_mps"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcie_set_mps/"
---

pcie_set_mps - set PCI Express maximum payload size

<h2>Synopsis</h2>

<pre><code>int pcie_set_mps(struct pci_dev *dev, int mps);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>mps</i>
<dl><dd>maximum payload size in bytes valid values are 128, 256, 512, 1024, 2048, 4096</dl>

<h2>Description</h2>

If possible sets maximum payload size

<h2>Copyright</h2>


