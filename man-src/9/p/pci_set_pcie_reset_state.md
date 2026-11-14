---
title: "pci_set_pcie_reset_state(9)"
name: "pci_set_pcie_reset_state"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_set_pcie_reset_state/"
---

pci_set_pcie_reset_state - set reset state for device dev

<h2>Synopsis</h2>

<pre><code>int pci_set_pcie_reset_state(struct pci_dev *dev, enum pcie_reset_state state);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCIe device reset</dl>
 

 <i>state</i>
<dl><dd>Reset state to enter into</dl>

<h2>Description</h2>

Sets the PCI reset state for the device.

<h2>Copyright</h2>


