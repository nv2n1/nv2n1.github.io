---
title: "pci_match_id(9)"
name: "pci_match_id"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_match_id/"
description: "pci_match_id – See if a pci device matches a given pci_id table"
---

<p>pci_match_id &#8211; See if a pci device matches a given pci_id table</p>
<h2>Synopsis</h2>
<pre><code>const struct pci_device_id *pci_match_id(const struct pci_device_id *ids, struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>ids</i></p>
<dl>
<dd>
<dd>array of PCI device id structures to search in</dl>
<p> <i>dev</i></p>
<dl>
<dd>the PCI device structure to match against.</dl>
<h2>Description</h2>
<p>Used by a driver to check whether a PCI device present in the system is in its list of supported devices. Returns the matching pci_device_id structure or <code>NULL</code> if there is no match. </p>
<p> Deprecated, don&#8217;t use this as it will not catch any dynamic ids that a driver might want to check for.</p>
<h2>Copyright</h2>
