---
title: "pci_release_selected_regions(9)"
name: "pci_release_selected_regions"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_release_selected_regions/"
---

pci_release_selected_regions - Release selected PCI I/O and memory resources

<h2>Synopsis</h2>

<pre><code>void pci_release_selected_regions(struct pci_dev *pdev, int bars);</code></pre>

<h2>Arguments</h2>

<i>pdev</i>
<dl><dd><dd>PCI device whose resources were previously reserved</dl>
 

 <i>bars</i>
<dl><dd>Bitmask of BARs to be released</dl>

<h2>Description</h2>

Release selected PCI I/O and memory resources previously reserved. Call this function only after all use of the PCI regions has ceased.

<h2>Copyright</h2>


