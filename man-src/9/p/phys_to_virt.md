---
title: "phys_to_virt(9)"
name: "phys_to_virt"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phys_to_virt/"
description: "phys_to_virt – map physical address to virtual"
---

<p>phys_to_virt &#8211; map physical address to virtual</p>
<h2>Synopsis</h2>
<pre><code>void *phys_to_virt(phys_addr_t address);</code></pre>
<h2>Arguments</h2>
<p><i>address</i></p>
<dl>
<dd>
<dd>address to remap</dl>
<h2>Description</h2>
<p>The returned virtual address is a current CPU mapping for the memory address given. It is only valid to use this function on addresses that have a kernel mapping </p>
<p> This function does not handle bus mappings for DMA transfers. In almost all conceivable cases a device driver should not be using this function</p>
<h2>Authors</h2>
<p><code>Matthew Wilcox</code> &lt;matthew [at] wil.cx&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
