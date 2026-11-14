---
title: "pci_dev_run_wake(9)"
name: "pci_dev_run_wake"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_dev_run_wake/"
description: "pci_dev_run_wake – Check if device can generate run-time wake-up events."
---

<p>pci_dev_run_wake &#8211; Check if device can generate run-time wake-up events.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_dev_run_wake(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to check.</dl>
<h2>Description</h2>
<p>Return true if the device itself is capable of generating wake-up events (through the platform or using the native PCIe PME) or if the device supports PME and one of its upstream bridges can generate wake-up events.</p>
<h2>Copyright</h2>
