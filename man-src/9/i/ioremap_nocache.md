---
title: "ioremap_nocache(9)"
name: "ioremap_nocache"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ioremap_nocache/"
description: "ioremap_nocache – map bus memory into CPU space"
---

<p>ioremap_nocache &#8211; map bus memory into CPU space</p>
<h2>Synopsis</h2>
<pre><code>void __iomem *ioremap_nocache(resource_size_t offset, unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>offset</i></p>
<dl>
<dd>
<dd>bus address of the memory</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the resource to map</dl>
<h2>Description</h2>
<p>ioremap performs a platform specific sequence of operations to make bus memory CPU accessible via the readb/readw/readl/writeb/ writew/writel functions and the other mmio helpers. The returned address is not guaranteed to be usable directly as a virtual address. </p>
<p> If the area you are trying to map is a PCI BAR you should have a look at <code>pci_iomap</code>.</p>
<h2>Authors</h2>
<p><code>Matthew Wilcox</code> &lt;matthew [at] wil.cx&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
