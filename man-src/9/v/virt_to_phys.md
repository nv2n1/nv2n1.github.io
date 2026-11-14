---
title: "virt_to_phys(9)"
name: "virt_to_phys"
section: "9"
letter: "v"
url: "/docs/linux/man/9-virt_to_phys/"
description: "virt_to_phys – map virtual addresses to physical"
---

<p>virt_to_phys &#8211; map virtual addresses to physical</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>phys_addr_t virt_to_phys(volatile void&nbsp;<wbr>*&nbsp;<wbr></code><i>address</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>address</i></p>
<dl>
<dd>
<dd>address to remap</dl>
<h2>Description</h2>
<p>The returned physical address is the physical (CPU) mapping for the memory address given. It is only valid to use this function on addresses directly mapped or allocated via kmalloc. </p>
<p> This function does not give bus mappings for DMA transfers. In almost all conceivable cases a device driver should not be using this function</p>
<h2>Authors</h2>
<p><code>Matthew Wilcox</code> &lt;matthew [at] wil.cx&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
