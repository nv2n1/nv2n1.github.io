---
title: "pci_reset_bus(9)"
name: "pci_reset_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_reset_bus/"
---

pci_reset_bus - reset a PCI bus

<h2>Synopsis</h2>

<pre><code>int pci_reset_bus(struct pci_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>top level PCI bus to reset</dl>

<h2>Description</h2>

Do a bus reset on the given bus and any subordinate buses, saving and restoring state of all devices. 

 Return 0 on success, non-zero on error.

<h2>Copyright</h2>


