---
title: "pci_sriov_set_totalvfs(9)"
name: "pci_sriov_set_totalvfs"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_sriov_set_totalvfs/"
---

pci_sriov_set_totalvfs - - reduce the TotalVFs available

<h2>Synopsis</h2>

<pre><code>int pci_sriov_set_totalvfs(struct pci_dev *dev, u16 numvfs);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI PF device</dl>
 

 <i>numvfs</i>
<dl><dd>number that should be used for TotalVFs supported</dl>

<h2>Description</h2>

Should be called from PF driver's probe routine with device's mutex held. 

 Returns 0 if PF is an SRIOV-capable device and value of numvfs valid. If not a PF return -ENOSYS; if numvfs is invalid return -EINVAL; if VFs already enabled, return -EBUSY.

<h2>Copyright</h2>


