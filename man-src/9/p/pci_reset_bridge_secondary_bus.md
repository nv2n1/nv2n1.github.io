---
title: "pci_reset_bridge_secondary_bus(9)"
name: "pci_reset_bridge_secondary_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_reset_bridge_secondary_bus/"
---

pci_reset_bridge_secondary_bus - Reset the secondary bus on a PCI bridge.

<h2>Synopsis</h2>

<pre><code>void pci_reset_bridge_secondary_bus(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Bridge device</dl>

<h2>Description</h2>

Use the bridge control register to assert reset on the secondary bus. Devices on the secondary bus are left in power-on state.

<h2>Copyright</h2>


