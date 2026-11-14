---
title: "pci_probe_reset_slot(9)"
name: "pci_probe_reset_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_probe_reset_slot/"
---

pci_probe_reset_slot - probe whether a PCI slot can be reset

<h2>Synopsis</h2>

<pre><code>int pci_probe_reset_slot(struct pci_slot *slot);</code></pre>

<h2>Arguments</h2>

<i>slot</i>
<dl><dd><dd>PCI slot to probe</dl>

<h2>Description</h2>

Return 0 if slot can be reset, negative if a slot reset is not supported.

<h2>Copyright</h2>


