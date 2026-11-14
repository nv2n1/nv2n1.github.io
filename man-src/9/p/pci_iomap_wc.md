---
title: "pci_iomap_wc(9)"
name: "pci_iomap_wc"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_iomap_wc/"
description: "pci_iomap_wc – create a virtual WC mapping cookie for a PCI BAR"
---

<p>pci_iomap_wc &#8211; create a virtual WC mapping cookie for a PCI BAR</p>
<h2>Synopsis</h2>
<pre><code>void __iomem *pci_iomap_wc(struct pci_dev *dev, int bar, unsigned long maxlen);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device that owns the BAR</dl>
<p> <i>bar</i></p>
<dl>
<dd>BAR number</dl>
<p> <i>maxlen</i></p>
<dl>
<dd>length of the memory to map</dl>
<h2>Description</h2>
<p>Using this function you will get a __iomem address to your device BAR. You can access it using ioread*() and iowrite*(). These functions hide the details if this is a MMIO or PIO address space and will just do what you expect from them in the correct way. When possible write combining is used. </p>
<p> <i>maxlen</i> specifies the maximum length to map. If you want to get access to the complete BAR without checking for its length first, pass <code>0</code> here.</p>
<h2>Authors</h2>
<p><code>Matthew Wilcox</code> &lt;matthew [at] wil.cx&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
