---
title: "pci_destroy_slot(9)"
name: "pci_destroy_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_destroy_slot/"
description: "pci_destroy_slot – decrement refcount for physical PCI slot"
---

<p>pci_destroy_slot &#8211; decrement refcount for physical PCI slot</p>
<h2>Synopsis</h2>
<pre><code>void pci_destroy_slot(struct pci_slot *slot);</code></pre>
<h2>Arguments</h2>
<p><i>slot</i></p>
<dl>
<dd>
<dd>struct pci_slot to decrement</dl>
<h2>Description</h2>
<p><code>struct</code> pci_slot is refcounted, so destroying them is really easy; we just call kobject_put on its kobj and let our release methods do the rest.</p>
<h2>Copyright</h2>
