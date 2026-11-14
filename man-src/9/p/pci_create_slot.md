---
title: "pci_create_slot(9)"
name: "pci_create_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_create_slot/"
description: "pci_create_slot – create or increment refcount for physical PCI slot"
---

<p>pci_create_slot &#8211; create or increment refcount for physical PCI slot</p>
<h2>Synopsis</h2>
<pre><code>struct pci_slot *pci_create_slot(struct pci_bus *parent, int slot_nr, const char *name, struct hotplug_slot *hotplug);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>struct pci_bus of parent bridge</dl>
<p> <i>slot_nr</i></p>
<dl>
<dd>PCI_SLOT(pci_dev-&gt;devfn) or -1 for placeholder</dl>
<p> <i>name</i></p>
<dl>
<dd>user visible string presented in /sys/bus/pci/slots/&lt;name&gt;</dl>
<p> <i>hotplug</i></p>
<dl>
<dd>set if caller is hotplug driver, NULL otherwise</dl>
<h2>Description</h2>
<p>PCI slots have first class attributes such as address, speed, width, and a struct pci_slot is used to manage them. This interface will either return a new struct pci_slot to the caller, or if the pci_slot already exists, its refcount will be incremented. </p>
<p> Slots are uniquely identified by a <i>pci_bus</i>, <i>slot_nr</i> tuple. </p>
<p> There are known platforms with broken firmware that assign the same name to multiple slots. Workaround these broken platforms by renaming the slots on behalf of the caller. If firmware assigns name N to multiple slots: </p>
<p> The first slot is assigned N The second slot is assigned N-1 The third slot is assigned N-2 etc. </p>
<p> Placeholder slots: In most cases, <i>pci_bus</i>, <i>slot_nr</i> will be sufficient to uniquely identify a slot. There is one notable exception &#8211; pSeries (rpaphp), where the <i>slot_nr</i> cannot be determined until a device is actually inserted into the slot. In this scenario, the caller may pass -1 for <i>slot_nr</i>. </p>
<p> The following semantics are imposed when the caller passes <i>slot_nr</i> == -1. First, we no longer check for an existing <code>struct</code> pci_slot, as there may be many slots with <i>slot_nr</i> of -1. The other change in semantics is user-visible, which is the &#8216;address&#8217; parameter presented in sysfs will consist solely of a dddd:bb tuple, where dddd is the PCI domain of the <code>struct</code> pci_bus and bb is the bus number. In other words, the devfn of the &#8216;placeholder&#8217; slot will not be displayed.</p>
<h2>Copyright</h2>
