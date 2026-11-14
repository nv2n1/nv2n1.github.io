---
title: "pci_enable_msi_range(9)"
name: "pci_enable_msi_range"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_msi_range/"
---

pci_enable_msi_range - configure device's MSI capability structure

<h2>Synopsis</h2>

<pre><code>int pci_enable_msi_range(struct pci_dev *dev, int minvec, int maxvec);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to configure</dl>
 

 <i>minvec</i>
<dl><dd>minimal number of interrupts to configure</dl>
 

 <i>maxvec</i>
<dl><dd>maximum number of interrupts to configure</dl>

<h2>Description</h2>

This function tries to allocate a maximum possible number of interrupts in a range between <i>minvec</i> and <i>maxvec</i>. It returns a negative errno if an error occurs. If it succeeds, it returns the actual number of interrupts allocated and updates the <i>dev</i>'s irq member to the lowest new interrupt number; the other interrupt numbers allocated to this device are consecutive.

<h2>Copyright</h2>


