---
title: "pci_add_dynid(9)"
name: "pci_add_dynid"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_add_dynid/"
---

pci_add_dynid - add a new PCI device ID to this driver and re-probe devices

<h2>Synopsis</h2>

<pre><code>int pci_add_dynid(struct pci_driver *drv, unsigned int vendor, unsigned int device, unsigned int subvendor, unsigned int subdevice, unsigned int class, unsigned int class_mask, unsigned long driver_data);</code></pre>

<h2>Arguments</h2>

<i>drv</i>
<dl><dd><dd>target pci driver</dl>
 

 <i>vendor</i>
<dl><dd>PCI vendor ID</dl>
 

 <i>device</i>
<dl><dd>PCI device ID</dl>
 

 <i>subvendor</i>
<dl><dd>PCI subvendor ID</dl>
 

 <i>subdevice</i>
<dl><dd>PCI subdevice ID</dl>
 

 <i>class</i>
<dl><dd>PCI class</dl>
 

 <i>class_mask</i>
<dl><dd>PCI class mask</dl>
 

 <i>driver_data</i>
<dl><dd>private driver data</dl>

<h2>Description</h2>

Adds a new dynamic pci device ID to this driver and causes the driver to probe for all devices again. <i>drv</i> must have been registered prior to calling this function.

<h2>Context</h2>

Does GFP_KERNEL allocation.

<h2>Return</h2>

0 on success, -errno on failure.

<h2>Copyright</h2>


