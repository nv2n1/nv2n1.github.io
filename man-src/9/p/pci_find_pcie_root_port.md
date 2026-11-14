---
title: "pci_find_pcie_root_port(9)"
name: "pci_find_pcie_root_port"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_pcie_root_port/"
---

pci_find_pcie_root_port - return PCIe Root Port

<h2>Synopsis</h2>

<pre><code>struct pci_dev *pci_find_pcie_root_port(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>

<h2>Description</h2>

Traverse up the parent chain and return the PCIe Root Port PCI Device for a given PCI Device.

<h2>Copyright</h2>


