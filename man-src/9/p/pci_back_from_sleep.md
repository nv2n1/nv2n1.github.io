---
title: "pci_back_from_sleep(9)"
name: "pci_back_from_sleep"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_back_from_sleep/"
---

pci_back_from_sleep - turn PCI device on during system-wide transition into working state

<h2>Synopsis</h2>

<pre><code>int pci_back_from_sleep(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Device to handle.</dl>

<h2>Description</h2>

Disable device's system wake-up capability and put it into D0.

<h2>Copyright</h2>


