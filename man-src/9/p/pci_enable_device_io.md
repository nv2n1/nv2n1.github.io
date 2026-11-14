---
title: "pci_enable_device_io(9)"
name: "pci_enable_device_io"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_device_io/"
---

pci_enable_device_io - Initialize a device for use with IO space

<h2>Synopsis</h2>

<pre><code>int pci_enable_device_io(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to be initialized</dl>

<h2>Description</h2>

Initialize device before it's used by a driver. Ask low-level code to enable I/O resources. Wake up the device if it was suspended. Beware, this function can fail.

<h2>Copyright</h2>


