---
title: "pci_find_bus(9)"
name: "pci_find_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_bus/"
description: "pci_find_bus – locate PCI bus from a given domain and bus number"
---

<p>pci_find_bus &#8211; locate PCI bus from a given domain and bus number</p>
<h2>Synopsis</h2>
<pre><code>struct pci_bus *pci_find_bus(int domain, int busnr);</code></pre>
<h2>Arguments</h2>
<p><i>domain</i></p>
<dl>
<dd>
<dd>number of PCI domain to search</dl>
<p> <i>busnr</i></p>
<dl>
<dd>number of desired PCI bus</dl>
<h2>Description</h2>
<p>Given a PCI bus number and domain number, the desired PCI bus is located in the global list of PCI buses. If the bus is found, a pointer to its data structure is returned. If no bus is found, <code>NULL</code> is returned.</p>
<h2>Copyright</h2>
