---
title: "pci_scan_slot(9)"
name: "pci_scan_slot"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_scan_slot/"
---

pci_scan_slot - scan a PCI slot on a bus for devices.

<h2>Synopsis</h2>

<pre><code>int pci_scan_slot(struct pci_bus *bus, int devfn);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>PCI bus to scan</dl>
 

 <i>devfn</i>
<dl><dd>slot number to scan (must have zero function.)</dl>

<h2>Description</h2>

Scan a PCI slot on the specified PCI bus for devices, adding discovered devices to the <i>bus</i>-&gt;devices list. New devices will not have is_added set. 

 Returns the number of new devices found.

<h2>Copyright</h2>


