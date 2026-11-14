---
title: "pci_try_reset_slot(9)"
name: "pci_try_reset_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_try_reset_slot/"
---

pci_try_reset_slot - Try to reset a PCI slot

<h2>Synopsis</h2>

<pre><code>int pci_try_reset_slot(struct pci_slot *slot);</code></pre>

<h2>Arguments</h2>

<i>slot</i>
<dl><dd><dd>PCI slot to reset</dl>

<h2>Description</h2>

Same as above except return -EAGAIN if the slot cannot be locked

<h2>Copyright</h2>


