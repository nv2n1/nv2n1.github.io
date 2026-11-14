---
title: "pci_msi_vec_count(9)"
name: "pci_msi_vec_count"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_msi_vec_count/"
---

pci_msi_vec_count - Return the number of MSI vectors a device can send

<h2>Synopsis</h2>

<pre><code>int pci_msi_vec_count(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to report about</dl>

<h2>Description</h2>

This function returns the number of MSI vectors a device requested via Multiple Message Capable register. It returns a negative errno if the device is not capable sending MSI interrupts. Otherwise, the call succeeds and returns a power of two, up to a maximum of 2^5 (32), according to the MSI specification.

<h2>Copyright</h2>


