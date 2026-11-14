---
title: "piix_init_one(9)"
name: "piix_init_one"
section: "9"
letter: "p"
url: "/docs/linux/man/9-piix_init_one/"
description: "piix_init_one – Register PIIX ATA PCI device with kernel services"
---

<p>piix_init_one &#8211; Register PIIX ATA PCI device with kernel services</p>
<h2>Synopsis</h2>
<pre><code>int piix_init_one(struct pci_dev *pdev, const struct pci_device_id *ent);</code></pre>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>PCI device to register</dl>
<p> <i>ent</i></p>
<dl>
<dd>Entry in piix_pci_tbl matching with <i>pdev</i></dl>
<h2>Description</h2>
<p>Called from kernel PCI layer. We probe for combined mode (sigh), and then hand over control to libata, for it to do the rest. </p>
<p> LOCKING: Inherited from PCI layer (may sleep).</p>
<h2>Return</h2>
<p>Zero on success, or -ERRNO value.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
