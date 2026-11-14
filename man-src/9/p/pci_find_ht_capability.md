---
title: "pci_find_ht_capability(9)"
name: "pci_find_ht_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_ht_capability/"
---

pci_find_ht_capability - query a device's Hypertransport capabilities

<h2>Synopsis</h2>

<pre><code>int pci_find_ht_capability(struct pci_dev *dev, int ht_cap);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>ht_cap</i>
<dl><dd>Hypertransport capability code</dl>

<h2>Description</h2>

Tell if a device supports a given Hypertransport capability. Returns an address within the device's PCI configuration space or 0 in case the device does not support the request capability. The address points to the PCI capability, of type PCI_CAP_ID_HT, which has a Hypertransport capability matching <i>ht_cap</i>.

<h2>Copyright</h2>


