---
title: "pci_cfg_access_unlock(9)"
name: "pci_cfg_access_unlock"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_cfg_access_unlock/"
---

pci_cfg_access_unlock - Unlock PCI config reads/writes

<h2>Synopsis</h2>

<pre><code>void pci_cfg_access_unlock(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pci device struct</dl>

<h2>Description</h2>

This function allows PCI config accesses to resume.

<h2>Copyright</h2>


