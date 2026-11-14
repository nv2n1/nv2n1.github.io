---
title: "pcie_set_readrq(9)"
name: "pcie_set_readrq"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcie_set_readrq/"
---

pcie_set_readrq - set PCI Express maximum memory read request

<h2>Synopsis</h2>

<pre><code>int pcie_set_readrq(struct pci_dev *dev, int rq);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>rq</i>
<dl><dd>maximum memory read count in bytes valid values are 128, 256, 512, 1024, 2048, 4096</dl>

<h2>Description</h2>

If possible sets maximum memory read request in bytes

<h2>Copyright</h2>


