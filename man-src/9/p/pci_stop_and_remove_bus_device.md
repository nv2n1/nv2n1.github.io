---
title: "pci_stop_and_remove_bus_device(9)"
name: "pci_stop_and_remove_bus_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_stop_and_remove_bus_device/"
---

pci_stop_and_remove_bus_device - remove a PCI device and any children

<h2>Synopsis</h2>

<pre><code>void pci_stop_and_remove_bus_device(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the device to remove</dl>

<h2>Description</h2>

Remove a PCI device from the device lists, informing the drivers that the device has been removed. We also remove any subordinate buses and children in a depth-first manner. 

 For each device we remove, delete the device structure from the device lists, remove the /proc entry, and notify userspace (/sbin/hotplug).

<h2>Copyright</h2>


