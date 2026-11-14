---
title: "pci_dev_get(9)"
name: "pci_dev_get"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_dev_get/"
description: "pci_dev_get – increments the reference count of the pci device structure"
---

<p>pci_dev_get &#8211; increments the reference count of the pci device structure</p>
<h2>Synopsis</h2>
<pre><code>struct pci_dev *pci_dev_get(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device being referenced</dl>
<h2>Description</h2>
<p>Each live reference to a device should be refcounted. </p>
<p> Drivers for PCI devices should normally record such references in their <code>probe</code> methods, when they bind to a device, and release them by calling <code>pci_dev_put</code>, in their <code>disconnect</code> methods. </p>
<p> A pointer to the device with the incremented reference counter is returned.</p>
<h2>Copyright</h2>
