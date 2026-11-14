---
title: "usb_hcd_pci_remove(9)"
name: "usb_hcd_pci_remove"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_pci_remove/"
description: "usb_hcd_pci_remove – shutdown processing for PCI-based HCDs"
---

<p>usb_hcd_pci_remove &#8211; shutdown processing for PCI-based HCDs</p>
<h2>Synopsis</h2>
<pre><code>void usb_hcd_pci_remove(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>USB Host Controller being removed</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Reverses the effect of <code>usb_hcd_pci_probe</code>, first invoking the HCD&#8217;s <code>stop</code> method. It is always called from a thread context, normally &#8220;rmmod&#8221;, &#8220;apmd&#8221;, or something similar. </p>
<p> Store this function in the HCD&#8217;s struct pci_driver as <code>remove</code>.</p>
<h2>Copyright</h2>
