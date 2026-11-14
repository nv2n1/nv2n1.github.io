---
title: "pci_hp_create_module_link(9)"
name: "pci_hp_create_module_link"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_hp_create_module_link/"
---

pci_hp_create_module_link - create symbolic link to the hotplug driver module.

<h2>Synopsis</h2>

<pre><code>void pci_hp_create_module_link(struct pci_slot *pci_slot);</code></pre>

<h2>Arguments</h2>

<i>pci_slot</i>
<dl><dd><dd>struct pci_slot</dl>

<h2>Description</h2>

Helper function for pci_hotplug_core.c to create symbolic link to the hotplug driver module.

<h2>Copyright</h2>


