---
title: "pci_hp_deregister(9)"
name: "pci_hp_deregister"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_hp_deregister/"
description: "pci_hp_deregister – deregister a hotplug_slot with the PCI hotplug subsystem"
---

<p>pci_hp_deregister &#8211; deregister a hotplug_slot with the PCI hotplug subsystem</p>
<h2>Synopsis</h2>
<pre><code>int pci_hp_deregister(struct hotplug_slot *slot);</code></pre>
<h2>Arguments</h2>
<p><i>slot</i></p>
<dl>
<dd>
<dd>pointer to the struct hotplug_slot to deregister</dl>
<h2>Description</h2>
<p>The <i>slot</i> must have been registered with the pci hotplug subsystem previously with a call to <code>pci_hp_register</code>. </p>
<p> Returns 0 if successful, anything else for an error.</p>
<h2>Copyright</h2>
