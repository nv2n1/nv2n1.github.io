---
title: "pci_get_subsys(9)"
name: "pci_get_subsys"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_get_subsys/"
description: "pci_get_subsys – begin or continue searching for a PCI device by vendor/subvendor/device/subdevice id"
---

<p>pci_get_subsys &#8211; begin or continue searching for a PCI device by vendor/subvendor/device/subdevice id</p>
<h2>Synopsis</h2>
<pre><code>struct pci_dev *pci_get_subsys(unsigned int vendor, unsigned int device, unsigned int ss_vendor, unsigned int ss_device, struct pci_dev *from);</code></pre>
<h2>Arguments</h2>
<p><i>vendor</i></p>
<dl>
<dd>
<dd>PCI vendor id to match, or <code>PCI_ANY_ID</code> to match all vendor ids</dl>
<p> <i>device</i></p>
<dl>
<dd>PCI device id to match, or <code>PCI_ANY_ID</code> to match all device ids</dl>
<p> <i>ss_vendor</i></p>
<dl>
<dd>PCI subsystem vendor id to match, or <code>PCI_ANY_ID</code> to match all vendor ids</dl>
<p> <i>ss_device</i></p>
<dl>
<dd>PCI subsystem device id to match, or <code>PCI_ANY_ID</code> to match all device ids</dl>
<p> <i>from</i></p>
<dl>
<dd>Previous PCI device found in search, or <code>NULL</code> for new search.</dl>
<h2>Description</h2>
<p>Iterates through the list of known PCI devices. If a PCI device is found with a matching <i>vendor</i>, <i>device</i>, <i>ss_vendor</i> and <i>ss_device</i>, a pointer to its device structure is returned, and the reference count to the device is incremented. Otherwise, <code>NULL</code> is returned. A new search is initiated by passing <code>NULL</code> as the <i>from</i> argument. Otherwise if <i>from</i> is not <code>NULL</code>, searches continue from next device on the global list. The reference count for <i>from</i> is always decremented if it is not <code>NULL</code>.</p>
<h2>Copyright</h2>
