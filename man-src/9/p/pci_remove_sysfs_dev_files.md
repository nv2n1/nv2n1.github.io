---
title: "pci_remove_sysfs_dev_files(9)"
name: "pci_remove_sysfs_dev_files"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_remove_sysfs_dev_files/"
---

pci_remove_sysfs_dev_files - cleanup PCI specific sysfs files

<h2>Synopsis</h2>

<pre><code>void pci_remove_sysfs_dev_files(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>device whose entries we should free</dl>

<h2>Description</h2>

Cleanup when <i>pdev</i> is removed from sysfs.

<h2>Copyright</h2>


