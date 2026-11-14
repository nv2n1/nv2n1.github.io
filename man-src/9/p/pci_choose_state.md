---
title: "pci_choose_state(9)"
name: "pci_choose_state"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_choose_state/"
description: "pci_choose_state – Choose the power state of a PCI device"
---

<p>pci_choose_state &#8211; Choose the power state of a PCI device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pci_power_t pci_choose_state(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, pm_message_t&nbsp;<wbr></code><i>state</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to be suspended</dl>
<p> <i>state</i></p>
<dl>
<dd>target sleep state for the whole system. This is the value that is passed to <code>suspend</code> function.</dl>
<h2>Description</h2>
<p>Returns PCI power state suitable for given device and given system message.</p>
<h2>Copyright</h2>
