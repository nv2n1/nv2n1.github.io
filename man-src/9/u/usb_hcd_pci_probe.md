---
title: "usb_hcd_pci_probe(9)"
name: "usb_hcd_pci_probe"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_pci_probe/"
description: "usb_hcd_pci_probe – initialize PCI-based HCDs"
---

<p>usb_hcd_pci_probe &#8211; initialize PCI-based HCDs</p>
<h2>Synopsis</h2>
<pre><code>int usb_hcd_pci_probe(struct pci_dev *dev, const struct pci_device_id *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>USB Host Controller being probed</dl>
<p> <i>id</i></p>
<dl>
<dd>pci hotplug id connecting controller to HCD framework</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Allocates basic PCI resources for this USB host controller, and then invokes the <code>start</code> method for the HCD associated with it through the hotplug entry&#8217;s driver_data. </p>
<p> Store this function in the HCD&#8217;s struct pci_driver as <code>probe</code>.</p>
<h2>Return</h2>
<p>0 if successful.</p>
<h2>Copyright</h2>
