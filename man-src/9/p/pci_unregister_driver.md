---
title: "pci_unregister_driver(9)"
name: "pci_unregister_driver"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_unregister_driver/"
description: "pci_unregister_driver – unregister a pci driver"
---

<p>pci_unregister_driver &#8211; unregister a pci driver</p>
<h2>Synopsis</h2>
<pre><code>void pci_unregister_driver(struct pci_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>drv</i></p>
<dl>
<dd>
<dd>the driver structure to unregister</dl>
<h2>Description</h2>
<p>Deletes the driver structure from the list of registered PCI drivers, gives it a chance to clean up by calling its <code>remove</code> function for each device it was responsible for, and marks those devices as driverless.</p>
<h2>Copyright</h2>
