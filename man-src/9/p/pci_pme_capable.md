---
title: "pci_pme_capable(9)"
name: "pci_pme_capable"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_pme_capable/"
description: "pci_pme_capable – check the capability of PCI device to generate PME#"
---

<p>pci_pme_capable &#8211; check the capability of PCI device to generate PME#</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_pme_capable(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, pci_power_t&nbsp;<wbr></code><i>state</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to handle.</dl>
<p> <i>state</i></p>
<dl>
<dd>PCI state from which device will issue PME#.</dl>
<h2>Copyright</h2>
