---
title: "pci_find_next_ext_capability(9)"
name: "pci_find_next_ext_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_next_ext_capability/"
---

pci_find_next_ext_capability - Find an extended capability

<h2>Synopsis</h2>

<pre><code>int pci_find_next_ext_capability(struct pci_dev *dev, int start, int cap);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>start</i>
<dl><dd>address at which to start looking (0 to start at beginning of list)</dl>
 

 <i>cap</i>
<dl><dd>capability code</dl>

<h2>Description</h2>

Returns the address of the next matching extended capability structure within the device's PCI configuration space or 0 if the device does not support it. Some capabilities can occur several times, e.g., the vendor-specific capability, and this provides a way to find them all.

<h2>Copyright</h2>


