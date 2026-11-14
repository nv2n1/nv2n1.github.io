---
title: "pci_dev_put(9)"
name: "pci_dev_put"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_dev_put/"
---

pci_dev_put - release a use of the pci device structure

<h2>Synopsis</h2>

<pre><code>void pci_dev_put(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device that's been disconnected</dl>

<h2>Description</h2>

Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.

<h2>Copyright</h2>


