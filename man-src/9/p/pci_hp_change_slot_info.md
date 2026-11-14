---
title: "pci_hp_change_slot_info(9)"
name: "pci_hp_change_slot_info"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_hp_change_slot_info/"
description: "pci_hp_change_slot_info – changes the slot’s information structure in the core"
---

<p>pci_hp_change_slot_info &#8211; changes the slot&#8217;s information structure in the core</p>
<h2>Synopsis</h2>
<pre><code>int pci_hp_change_slot_info(struct hotplug_slot *slot, struct hotplug_slot_info *info);</code></pre>
<h2>Arguments</h2>
<p><i>slot</i></p>
<dl>
<dd>
<dd>pointer to the slot whose info has changed</dl>
<p> <i>info</i></p>
<dl>
<dd>pointer to the info copy into the slot&#8217;s info structure</dl>
<h2>Description</h2>
<p><i>slot</i> must have been registered with the pci hotplug subsystem previously with a call to <code>pci_hp_register</code>. </p>
<p> Returns 0 if successful, anything else for an error.</p>
<h2>Copyright</h2>
