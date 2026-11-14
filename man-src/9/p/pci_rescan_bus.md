---
title: "pci_rescan_bus(9)"
name: "pci_rescan_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_rescan_bus/"
---

pci_rescan_bus - scan a PCI bus for devices.

<h2>Synopsis</h2>

<pre><code>unsigned int pci_rescan_bus(struct pci_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>PCI bus to scan</dl>

<h2>Description</h2>

Scan a PCI bus and child buses for new devices, adds them, and enables them. 

 Returns the max number of subordinate bus discovered.

<h2>Copyright</h2>


