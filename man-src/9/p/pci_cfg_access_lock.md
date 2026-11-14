---
title: "pci_cfg_access_lock(9)"
name: "pci_cfg_access_lock"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_cfg_access_lock/"
---

pci_cfg_access_lock - Lock PCI config reads/writes

<h2>Synopsis</h2>

<pre><code>void pci_cfg_access_lock(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pci device struct</dl>

<h2>Description</h2>

When access is locked, any userspace reads or writes to config space and concurrent lock requests will sleep until access is allowed via pci_cfg_access_unlocked again.

<h2>Copyright</h2>


