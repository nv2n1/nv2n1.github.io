---
title: "pci_find_next_bus(9)"
name: "pci_find_next_bus"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_next_bus/"
description: "pci_find_next_bus – begin or continue searching for a PCI bus"
---

<p>pci_find_next_bus &#8211; begin or continue searching for a PCI bus</p>
<h2>Synopsis</h2>
<pre><code>struct pci_bus *pci_find_next_bus(const struct pci_bus *from);</code></pre>
<h2>Arguments</h2>
<p><i>from</i></p>
<dl>
<dd>
<dd>Previous PCI bus found, or <code>NULL</code> for new search.</dl>
<h2>Description</h2>
<p>Iterates through the list of known PCI buses. A new search is initiated by passing <code>NULL</code> as the <i>from</i> argument. Otherwise if <i>from</i> is not <code>NULL</code>, searches continue from next device on the global list.</p>
<h2>Copyright</h2>
