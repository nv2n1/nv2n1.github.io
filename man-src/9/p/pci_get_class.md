---
title: "pci_get_class(9)"
name: "pci_get_class"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_get_class/"
description: "pci_get_class – begin or continue searching for a PCI device by class"
---

<p>pci_get_class &#8211; begin or continue searching for a PCI device by class</p>
<h2>Synopsis</h2>
<pre><code>struct pci_dev *pci_get_class(unsigned int class, struct pci_dev *from);</code></pre>
<h2>Arguments</h2>
<p><i>class</i></p>
<dl>
<dd>
<dd>search for a PCI device with this class designation</dl>
<p> <i>from</i></p>
<dl>
<dd>Previous PCI device found in search, or <code>NULL</code> for new search.</dl>
<h2>Description</h2>
<p>Iterates through the list of known PCI devices. If a PCI device is found with a matching <i>class</i>, the reference count to the device is incremented and a pointer to its device structure is returned. Otherwise, <code>NULL</code> is returned. A new search is initiated by passing <code>NULL</code> as the <i>from</i> argument. Otherwise if <i>from</i> is not <code>NULL</code>, searches continue from next device on the global list. The reference count for <i>from</i> is always decremented if it is not <code>NULL</code>.</p>
<h2>Copyright</h2>
