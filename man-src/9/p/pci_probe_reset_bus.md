---
title: "pci_probe_reset_bus(9)"
name: "pci_probe_reset_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_probe_reset_bus/"
---

pci_probe_reset_bus - probe whether a PCI bus can be reset

<h2>Synopsis</h2>

<pre><code>int pci_probe_reset_bus(struct pci_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>PCI bus to probe</dl>

<h2>Description</h2>

Return 0 if bus can be reset, negative if a bus reset is not supported.

<h2>Copyright</h2>


