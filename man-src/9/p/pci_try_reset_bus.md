---
title: "pci_try_reset_bus(9)"
name: "pci_try_reset_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_try_reset_bus/"
---

pci_try_reset_bus - Try to reset a PCI bus

<h2>Synopsis</h2>

<pre><code>int pci_try_reset_bus(struct pci_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>top level PCI bus to reset</dl>

<h2>Description</h2>

Same as above except return -EAGAIN if the bus cannot be locked

<h2>Copyright</h2>


