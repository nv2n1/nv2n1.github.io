---
title: "pcie_get_minimum_link(9)"
name: "pcie_get_minimum_link"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcie_get_minimum_link/"
---

pcie_get_minimum_link - determine minimum link settings of a PCI device

<h2>Synopsis</h2>

<pre><code>int pcie_get_minimum_link(struct pci_dev *dev, enum pci_bus_speed *speed, enum pcie_link_width *width);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>speed</i>
<dl><dd>storage for minimum speed</dl>
 

 <i>width</i>
<dl><dd>storage for minimum width</dl>

<h2>Description</h2>

This function will walk up the PCI device chain and determine the minimum link width and speed of the device.

<h2>Copyright</h2>


