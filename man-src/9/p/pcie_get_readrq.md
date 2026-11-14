---
title: "pcie_get_readrq(9)"
name: "pcie_get_readrq"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcie_get_readrq/"
---

pcie_get_readrq - get PCI Express read request size

<h2>Synopsis</h2>

<pre><code>int pcie_get_readrq(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>

<h2>Description</h2>

Returns maximum memory read request in bytes or appropriate error value.

<h2>Copyright</h2>


