---
title: "pci_reenable_device(9)"
name: "pci_reenable_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_reenable_device/"
---

pci_reenable_device - Resume abandoned device

<h2>Synopsis</h2>

<pre><code>int pci_reenable_device(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to be resumed</dl>

<h2>Description</h2>

Note this function is a backend of pci_default_resume and is not supposed to be called by normal code, write proper resume handler and use it instead.

<h2>Copyright</h2>


