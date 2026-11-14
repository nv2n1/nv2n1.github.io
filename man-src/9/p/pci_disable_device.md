---
title: "pci_disable_device(9)"
name: "pci_disable_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_disable_device/"
description: "pci_disable_device – Disable PCI device after use"
---

<p>pci_disable_device &#8211; Disable PCI device after use</p>
<h2>Synopsis</h2>
<pre><code>void pci_disable_device(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to be disabled</dl>
<h2>Description</h2>
<p>Signal to the system that the PCI device is not in use by the system anymore. This only involves disabling PCI bus-mastering, if active. </p>
<p> Note we don&#8217;t actually disable the device until all callers of <code>pci_enable_device</code> have called <code>pci_disable_device</code>.</p>
<h2>Copyright</h2>
