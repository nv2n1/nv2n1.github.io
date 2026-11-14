---
title: "pci_try_reset_function(9)"
name: "pci_try_reset_function"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_try_reset_function/"
---

pci_try_reset_function - quiesce and reset a PCI device function

<h2>Synopsis</h2>

<pre><code>int pci_try_reset_function(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to reset</dl>

<h2>Description</h2>

Same as above, except return -EAGAIN if unable to lock device.

<h2>Copyright</h2>


