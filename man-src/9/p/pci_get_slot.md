---
title: "pci_get_slot(9)"
name: "pci_get_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_get_slot/"
description: "pci_get_slot – locate PCI device for a given PCI slot"
---

<p>pci_get_slot &#8211; locate PCI device for a given PCI slot</p>
<h2>Synopsis</h2>
<pre><code>struct pci_dev *pci_get_slot(struct pci_bus *bus, unsigned int devfn);</code></pre>
<h2>Arguments</h2>
<p><i>bus</i></p>
<dl>
<dd>
<dd>PCI bus on which desired PCI device resides</dl>
<p> <i>devfn</i></p>
<dl>
<dd>encodes number of PCI slot in which the desired PCI device resides and the logical device number within that slot in case of multi-function devices.</dl>
<h2>Description</h2>
<p>Given a PCI bus and slot/function number, the desired PCI device is located in the list of PCI devices. If the device is found, its reference count is increased and this function returns a pointer to its data structure. The caller must decrement the reference count by calling <code>pci_dev_put</code>. If no device is found, <code>NULL</code> is returned.</p>
<h2>Copyright</h2>
