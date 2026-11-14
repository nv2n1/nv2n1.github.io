---
title: "pci_release_region(9)"
name: "pci_release_region"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_release_region/"
---

pci_release_region - Release a PCI bar

<h2>Synopsis</h2>

<pre><code>void pci_release_region(struct pci_dev *pdev, int bar);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device whose resources were previously reserved by pci_request_region</dl>
 

 <i>bar</i>
<dl><dd>BAR to release</dl>

<h2>Description</h2>

Releases the PCI I/O and memory resources previously reserved by a successful call to pci_request_region. Call this function only after all use of the PCI regions has ceased.

<h2>Copyright</h2>


