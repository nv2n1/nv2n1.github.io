---
title: "pcim_pin_device(9)"
name: "pcim_pin_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcim_pin_device/"
description: "pcim_pin_device – Pin managed PCI device"
---

<p>pcim_pin_device &#8211; Pin managed PCI device</p>
<h2>Synopsis</h2>
<pre><code>void pcim_pin_device(struct pci_dev *pdev);</code></pre>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>PCI device to pin</dl>
<h2>Description</h2>
<p>Pin managed PCI device <i>pdev</i>. Pinned device won&#8217;t be disabled on driver detach. <i>pdev</i> must have been enabled with <code>pcim_enable_device</code>.</p>
<h2>Copyright</h2>
