---
title: "ata_pci_remove_one(9)"
name: "ata_pci_remove_one"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_pci_remove_one/"
description: "ata_pci_remove_one – PCI layer callback for device removal"
---

<p>ata_pci_remove_one &#8211; PCI layer callback for device removal</p>
<h2>Synopsis</h2>
<pre><code>void ata_pci_remove_one(struct pci_dev *pdev);</code></pre>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>PCI device that was removed</dl>
<h2>Description</h2>
<p>PCI layer indicates to libata via this hook that hot-unplug or module unload event has occurred. Detach all ports. Resource release is handled via devres. </p>
<p> LOCKING: Inherited from PCI layer (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
