---
title: "pci_wake_from_d3(9)"
name: "pci_wake_from_d3"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_wake_from_d3/"
description: "pci_wake_from_d3 – enable/disable device to wake up from D3_hot or D3_cold"
---

<p>pci_wake_from_d3 &#8211; enable/disable device to wake up from D3_hot or D3_cold</p>
<h2>Synopsis</h2>
<pre><code>int pci_wake_from_d3(struct pci_dev *dev, bool enable);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to prepare</dl>
<p> <i>enable</i></p>
<dl>
<dd>True to enable wake-up event generation; false to disable</dl>
<h2>Description</h2>
<p>Many drivers want the device to wake up the system from D3_hot or D3_cold and this function allows them to set that up cleanly &#8211; <code>pci_enable_wake</code> should not be called twice in a row to enable wake-up due to PCI PM vs ACPI ordering constraints. </p>
<p> This function only returns error code if the device is not capable of generating PME# from both D3_hot and D3_cold, and the platform is unable to enable wake-up power for it.</p>
<h2>Copyright</h2>
