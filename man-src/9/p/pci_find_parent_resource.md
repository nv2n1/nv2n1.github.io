---
title: "pci_find_parent_resource(9)"
name: "pci_find_parent_resource"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_parent_resource/"
---

pci_find_parent_resource - return resource region of parent bus of given region

<h2>Synopsis</h2>

<pre><code>struct resource *pci_find_parent_resource(const struct pci_dev *dev, struct resource *res);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device structure contains resources to be searched</dl>
 

 <i>res</i>
<dl><dd>child resource record for which parent is sought</dl>

<h2>Description</h2>

For given resource region of given device, return the resource region of parent bus the given region is contained in.

<h2>Copyright</h2>


