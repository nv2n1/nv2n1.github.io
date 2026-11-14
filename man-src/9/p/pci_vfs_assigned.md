---
title: "pci_vfs_assigned(9)"
name: "pci_vfs_assigned"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_vfs_assigned/"
---

pci_vfs_assigned - returns number of VFs are assigned to a guest

<h2>Synopsis</h2>

<pre><code>int pci_vfs_assigned(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device</dl>

<h2>Description</h2>

Returns number of VFs belonging to this device that are assigned to a guest. If device is not a physical function returns 0.

<h2>Copyright</h2>


