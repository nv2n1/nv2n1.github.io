---
title: "pci_prepare_to_sleep(9)"
name: "pci_prepare_to_sleep"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_prepare_to_sleep/"
---

pci_prepare_to_sleep - prepare PCI device for system-wide transition into a sleep state

<h2>Synopsis</h2>

<pre><code>int pci_prepare_to_sleep(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Device to handle.</dl>

<h2>Description</h2>

Choose the power state appropriate for the device depending on whether it can wake up the system and/or is power manageable by the platform (PCI_D3hot is the default) and put the device into that state.

<h2>Copyright</h2>


