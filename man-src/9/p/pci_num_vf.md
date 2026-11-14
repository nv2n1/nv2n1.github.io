---
title: "pci_num_vf(9)"
name: "pci_num_vf"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_num_vf/"
---

pci_num_vf - return number of VFs associated with a PF device_release_driver

<h2>Synopsis</h2>

<pre><code>int pci_num_vf(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device</dl>

<h2>Description</h2>

Returns number of VFs, or 0 if SR-IOV is not enabled.

<h2>Copyright</h2>


