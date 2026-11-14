---
title: "pci_enable_msix(9)"
name: "pci_enable_msix"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_msix/"
---

pci_enable_msix - configure device's MSI-X capability structure

<h2>Synopsis</h2>

<pre><code>int pci_enable_msix(struct pci_dev *dev, struct msix_entry *entries, int nvec);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pointer to the pci_dev data structure of MSI-X device function</dl>
 

 <i>entries</i>
<dl><dd>pointer to an array of MSI-X entries (optional)</dl>
 

 <i>nvec</i>
<dl><dd>number of MSI-X irqs requested for allocation by device driver</dl>

<h2>Description</h2>

Setup the MSI-X capability structure of device function with the number of requested irqs upon its software driver call to request for MSI-X mode enabled on its hardware device function. A return of zero indicates the successful configuration of MSI-X capability structure with new allocated MSI-X irqs. A return of &lt; 0 indicates a failure. Or a return of &gt; 0 indicates that driver request is exceeding the number of irqs or MSI-X vectors available. Driver should use the returned value to re-send its request.

<h2>Copyright</h2>


