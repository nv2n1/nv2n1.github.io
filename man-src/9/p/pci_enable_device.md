---
title: "pci_enable_device(9)"
name: "pci_enable_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_device/"
---

pci_enable_device - Initialize device before it's used by a driver.

<h2>Synopsis</h2>

<pre><code>int pci_enable_device(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to be initialized</dl>

<h2>Description</h2>

Initialize device before it's used by a driver. Ask low-level code to enable I/O and memory. Wake up the device if it was suspended. Beware, this function can fail. 

 Note we don't actually enable the device many times if we call this function repeatedly (we just increment the count).

<h2>Copyright</h2>


