---
title: "pci_bus_max_busnr(9)"
name: "pci_bus_max_busnr"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_bus_max_busnr/"
---

pci_bus_max_busnr - returns maximum PCI bus number of given bus' children

<h2>Synopsis</h2>

<pre><code>unsigned char pci_bus_max_busnr(struct pci_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>pointer to PCI bus structure to search</dl>

<h2>Description</h2>

Given a PCI bus, returns the highest PCI bus number present in the set including the given PCI bus and its list of child PCI buses.

<h2>Copyright</h2>


