---
title: "pci_find_resource(9)"
name: "pci_find_resource"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_resource/"
description: "pci_find_resource – Return matching PCI device resource"
---

<p>pci_find_resource &#8211; Return matching PCI device resource</p>
<h2>Synopsis</h2>
<pre><code>struct resource *pci_find_resource(struct pci_dev *dev, struct resource *res);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to query</dl>
<p> <i>res</i></p>
<dl>
<dd>Resource to look for</dl>
<h2>Description</h2>
<p>Goes over standard PCI resources (BARs) and checks if the given resource is partially or fully contained in any of them. In that case the matching resource is returned, <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>
