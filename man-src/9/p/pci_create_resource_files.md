---
title: "pci_create_resource_files(9)"
name: "pci_create_resource_files"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_create_resource_files/"
---

pci_create_resource_files - create resource files in sysfs for <i>dev</i>

<h2>Synopsis</h2>

<pre><code>int pci_create_resource_files(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>dev in question</dl>

<h2>Description</h2>

Walk the resources in <i>pdev</i> creating files for each resource available.

<h2>Copyright</h2>


