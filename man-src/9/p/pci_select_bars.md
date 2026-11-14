---
title: "pci_select_bars(9)"
name: "pci_select_bars"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_select_bars/"
---

pci_select_bars - Make BAR mask from the type of resource

<h2>Synopsis</h2>

<pre><code>int pci_select_bars(struct pci_dev *dev, unsigned long flags);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device for which BAR mask is made</dl>
 

 <i>flags</i>
<dl><dd>resource type mask to be selected</dl>

<h2>Description</h2>

This helper routine makes bar mask from the type of resource.

<h2>Copyright</h2>


