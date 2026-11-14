---
title: "pci_find_capability(9)"
name: "pci_find_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_capability/"
description: "pci_find_capability – query for devices’ capabilities"
---

<p>pci_find_capability &#8211; query for devices&#8217; capabilities</p>
<h2>Synopsis</h2>
<pre><code>int pci_find_capability(struct pci_dev *dev, int cap);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to query</dl>
<p> <i>cap</i></p>
<dl>
<dd>capability code</dl>
<h2>Description</h2>
<p>Tell if a device supports a given PCI capability. Returns the address of the requested capability structure within the device&#8217;s PCI configuration space or 0 in case the device does not support it. Possible values for <i>cap</i>: </p>
<p> <code>PCI_CAP_ID_PM</code> Power Management <code>PCI_CAP_ID_AGP</code> Accelerated Graphics Port <code>PCI_CAP_ID_VPD</code> Vital Product Data <code>PCI_CAP_ID_SLOTID</code> Slot Identification <code>PCI_CAP_ID_MSI</code> Message Signalled Interrupts <code>PCI_CAP_ID_CHSWP</code> CompactPCI HotSwap <code>PCI_CAP_ID_PCIX</code> PCI-X <code>PCI_CAP_ID_EXP</code> PCI Express</p>
<h2>Copyright</h2>
