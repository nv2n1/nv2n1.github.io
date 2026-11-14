---
title: "pci_set_master(9)"
name: "pci_set_master"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_set_master/"
description: "pci_set_master – enables bus-mastering for device dev"
---

<p>pci_set_master &#8211; enables bus-mastering for device dev</p>
<h2>Synopsis</h2>
<pre><code>void pci_set_master(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device to enable</dl>
<h2>Description</h2>
<p>Enables bus-mastering on the device and calls <code>pcibios_set_master</code> to do the needed arch specific settings.</p>
<h2>Copyright</h2>
