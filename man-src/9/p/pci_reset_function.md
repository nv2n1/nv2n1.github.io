---
title: "pci_reset_function(9)"
name: "pci_reset_function"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_reset_function/"
---

pci_reset_function - quiesce and reset a PCI device function

<h2>Synopsis</h2>

<pre><code>int pci_reset_function(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to reset</dl>

<h2>Description</h2>

Some devices allow an individual function to be reset without affecting other functions in the same device. The PCI device must be responsive to PCI config space in order to use this function. 

 This function does not just reset the PCI portion of a device, but clears all the state associated with the device. This function differs from __pci_reset_function in that it saves and restores device state over the reset. 

 Returns 0 if the device function was successfully reset or negative if the device doesn't support resetting a single function.

<h2>Copyright</h2>


