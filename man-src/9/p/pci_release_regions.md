---
title: "pci_release_regions(9)"
name: "pci_release_regions"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_release_regions/"
---

pci_release_regions - Release reserved PCI I/O and memory resources

<h2>Synopsis</h2>

<pre><code>void pci_release_regions(struct pci_dev *pdev);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device whose resources were previously reserved by pci_request_regions</dl>

<h2>Description</h2>

Releases all PCI I/O and memory resources previously reserved by a successful call to pci_request_regions. Call this function only after all use of the PCI regions has ceased.

<h2>Copyright</h2>


