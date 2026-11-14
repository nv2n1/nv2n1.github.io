---
title: "pci_msix_vec_count(9)"
name: "pci_msix_vec_count"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_msix_vec_count/"
---

pci_msix_vec_count - return the number of device's MSI-X table entries

<h2>Synopsis</h2>

<pre><code>int pci_msix_vec_count(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pointer to the pci_dev data structure of MSI-X device function This function returns the number of device's MSI-X table entries and therefore the number of MSI-X vectors device is capable of sending. It returns a negative errno if the device is not capable of sending MSI-X interrupts.</dl>

<h2>Copyright</h2>


