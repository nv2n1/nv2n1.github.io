---
title: "pci_dev_present(9)"
name: "pci_dev_present"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_dev_present/"
---

pci_dev_present - Returns 1 if device matching the device list is present, 0 if not.

<h2>Synopsis</h2>

<pre><code>int pci_dev_present(const struct pci_device_id *ids);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>A pointer to a null terminated list of struct pci_device_id structures that describe the type of PCI device the caller is trying to find.</dl>

<h2>Description</h2>

Obvious fact: You do not have a reference to any device that might be found by this function, so if that device is removed from the system right after this function is finished, the value will be stale. Use this function to find devices that are usually built into a system, or for a general hint as to if another device happens to be present at this specific moment in time.

<h2>Copyright</h2>


