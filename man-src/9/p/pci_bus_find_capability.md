---
title: "pci_bus_find_capability(9)"
name: "pci_bus_find_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_bus_find_capability/"
description: "pci_bus_find_capability – query for devices’ capabilities"
---

<p>pci_bus_find_capability &#8211; query for devices&#8217; capabilities</p>
<h2>Synopsis</h2>
<pre><code>int pci_bus_find_capability(struct pci_bus *bus, unsigned int devfn, int cap);</code></pre>
<h2>Arguments</h2>
<p><i>bus</i></p>
<dl>
<dd>
<dd>the PCI bus to query</dl>
<p> <i>devfn</i></p>
<dl>
<dd>PCI device to query</dl>
<p> <i>cap</i></p>
<dl>
<dd>capability code</dl>
<h2>Description</h2>
<p>Like <code>pci_find_capability</code> but works for pci devices that do not have a pci_dev structure set up yet. </p>
<p> Returns the address of the requested capability structure within the device&#8217;s PCI configuration space or 0 in case the device does not support it.</p>
<h2>Copyright</h2>
