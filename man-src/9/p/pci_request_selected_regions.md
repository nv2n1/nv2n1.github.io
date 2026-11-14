---
title: "pci_request_selected_regions(9)"
name: "pci_request_selected_regions"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_request_selected_regions/"
---

pci_request_selected_regions - Reserve selected PCI I/O and memory resources

<h2>Synopsis</h2>

<pre><code>int pci_request_selected_regions(struct pci_dev *pdev, int bars, const char *res_name);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device whose resources are to be reserved</dl>
 

 <i>bars</i>
<dl><dd>Bitmask of BARs to be requested</dl>
 

 <i>res_name</i>
<dl><dd>Name to be associated with resource</dl>

<h2>Copyright</h2>


