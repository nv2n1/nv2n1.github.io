---
title: "pci_remove_resource_files(9)"
name: "pci_remove_resource_files"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_remove_resource_files/"
---

pci_remove_resource_files - cleanup resource files

<h2>Synopsis</h2>

<pre><code>void pci_remove_resource_files(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>dev to cleanup</dl>

<h2>Description</h2>

If we created resource files for <i>pdev</i>, remove them from sysfs and free their resources.

<h2>Copyright</h2>


