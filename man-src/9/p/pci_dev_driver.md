---
title: "pci_dev_driver(9)"
name: "pci_dev_driver"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_dev_driver/"
description: "pci_dev_driver – get the pci_driver of a device"
---

<p>pci_dev_driver &#8211; get the pci_driver of a device</p>
<h2>Synopsis</h2>
<pre><code>struct pci_driver *pci_dev_driver(const struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device to query</dl>
<h2>Description</h2>
<p>Returns the appropriate pci_driver structure or <code>NULL</code> if there is no registered driver for the device.</p>
<h2>Copyright</h2>
