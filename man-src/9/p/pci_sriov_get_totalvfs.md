---
title: "pci_sriov_get_totalvfs(9)"
name: "pci_sriov_get_totalvfs"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_sriov_get_totalvfs/"
---

pci_sriov_get_totalvfs - - get total VFs supported on this device

<h2>Synopsis</h2>

<pre><code>int pci_sriov_get_totalvfs(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI PF device</dl>

<h2>Description</h2>

For a PCIe device with SRIOV support, return the PCIe SRIOV capability value of TotalVFs or the value of driver_max_VFs if the driver reduced it. Otherwise 0.

<h2>Copyright</h2>


