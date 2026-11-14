---
title: "pci_lost_interrupt(9)"
name: "pci_lost_interrupt"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_lost_interrupt/"
description: "pci_lost_interrupt – reports a lost PCI interrupt"
---

<p>pci_lost_interrupt &#8211; reports a lost PCI interrupt</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>enum pci_lost_interrupt_reason pci_lost_interrupt(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>pdev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>device whose interrupt is lost</dl>
<h2>Description</h2>
<p>The primary function of this routine is to report a lost interrupt in a standard way which users can recognise (instead of blaming the driver).</p>
<h2>Return</h2>
<p>a suggestion for fixing it (although the driver is not required to act on this).</p>
<h2>Copyright</h2>
