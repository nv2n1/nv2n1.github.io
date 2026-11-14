---
title: "pci_reset_slot(9)"
name: "pci_reset_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_reset_slot/"
---

pci_reset_slot - reset a PCI slot

<h2>Synopsis</h2>

<pre><code>int pci_reset_slot(struct pci_slot *slot);</code></pre>

<h2>Arguments</h2>

<i>slot</i>
<dl><dd><dd>PCI slot to reset</dl>

<h2>Description</h2>

A PCI bus may host multiple slots, each slot may support a reset mechanism independent of other slots. For instance, some slots may support slot power control. In the case of a 1:1 bus to slot architecture, this function may wrap the bus reset to avoid spurious slot related events such as hotplug. Generally a slot reset should be attempted before a bus reset. All of the function of the slot and any subordinate buses behind the slot are reset through this function. PCI config space of all devices in the slot and behind the slot is saved before and restored after reset. 

 Return 0 on success, non-zero on error.

<h2>Copyright</h2>


