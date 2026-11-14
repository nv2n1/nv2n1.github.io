---
title: "pci_enable_msix_range(9)"
name: "pci_enable_msix_range"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_msix_range/"
---

pci_enable_msix_range - configure device's MSI-X capability structure

<h2>Synopsis</h2>

<pre><code>int pci_enable_msix_range(struct pci_dev *dev, struct msix_entry *entries, int minvec, int maxvec);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pointer to the pci_dev data structure of MSI-X device function</dl>
 

 <i>entries</i>
<dl><dd>pointer to an array of MSI-X entries</dl>
 

 <i>minvec</i>
<dl><dd>minimum number of MSI-X irqs requested</dl>
 

 <i>maxvec</i>
<dl><dd>maximum number of MSI-X irqs requested</dl>

<h2>Description</h2>

Setup the MSI-X capability structure of device function with a maximum possible number of interrupts in the range between <i>minvec</i> and <i>maxvec</i> upon its software driver call to request for MSI-X mode enabled on its hardware device function. It returns a negative errno if an error occurs. If it succeeds, it returns the actual number of interrupts allocated and indicates the successful configuration of MSI-X capability structure with new allocated MSI-X interrupts.

<h2>Copyright</h2>


