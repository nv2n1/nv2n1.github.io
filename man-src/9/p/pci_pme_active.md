---
title: "pci_pme_active(9)"
name: "pci_pme_active"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_pme_active/"
---

pci_pme_active - enable or disable PCI device's PME# function

<h2>Synopsis</h2>

<pre><code>void pci_pme_active(struct pci_dev *dev, bool enable);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to handle.</dl>
 

 <i>enable</i>
<dl><dd>'true' to enable PME# generation; 'false' to disable it.</dl>

<h2>Description</h2>

The caller must verify that the device is capable of generating PME# before calling this function with <i>enable</i> equal to 'true'.

<h2>Copyright</h2>


