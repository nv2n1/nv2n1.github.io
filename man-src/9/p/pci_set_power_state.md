---
title: "pci_set_power_state(9)"
name: "pci_set_power_state"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_set_power_state/"
---

pci_set_power_state - Set the power state of a PCI device

<h2>Synopsis</h2>

<pre><code>int pci_set_power_state(struct pci_dev *dev, pci_power_t state);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to handle.</dl>
 

 <i>state</i>
<dl><dd>PCI power state (D0, D1, D2, D3hot) to put the device into.</dl>

<h2>Description</h2>

Transition a device to a new power state, using the platform firmware and/or the device's PCI PM registers. 

 RETURN VALUE: -EINVAL if the requested state is invalid. -EIO if device does not support PCI PM or its PM capabilities register has a wrong version, or device doesn't support the requested state. 0 if device already is in the requested state. 0 if device's power state has been successfully changed.

<h2>Copyright</h2>


