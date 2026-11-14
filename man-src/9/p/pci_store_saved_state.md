---
title: "pci_store_saved_state(9)"
name: "pci_store_saved_state"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_store_saved_state/"
---

pci_store_saved_state - Allocate and return an opaque struct containing the device saved state.

<h2>Synopsis</h2>

<pre><code>struct pci_saved_state *pci_store_saved_state(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device that we're dealing with</dl>

<h2>Description</h2>

Return NULL if no state or error.

<h2>Copyright</h2>


