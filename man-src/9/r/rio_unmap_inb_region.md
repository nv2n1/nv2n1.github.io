---
title: "rio_unmap_inb_region(9)"
name: "rio_unmap_inb_region"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_unmap_inb_region/"
description: "rio_unmap_inb_region – – Unmap the inbound memory region"
---

<p>rio_unmap_inb_region &#8211; &#8211; Unmap the inbound memory region</p>
<h2>Synopsis</h2>
<pre><code>void rio_unmap_inb_region(struct rio_mport *mport, dma_addr_t lstart);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port</dl>
<p> <i>lstart</i></p>
<dl>
<dd>physical address of memory region to be unmapped</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
