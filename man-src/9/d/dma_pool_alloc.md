---
title: "dma_pool_alloc(9)"
name: "dma_pool_alloc"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dma_pool_alloc/"
description: "dma_pool_alloc – get a block of consistent memory"
---

<p>dma_pool_alloc &#8211; get a block of consistent memory</p>
<h2>Synopsis</h2>
<pre><code>void *dma_pool_alloc(struct dma_pool *pool, gfp_t mem_flags, dma_addr_t *handle);</code></pre>
<h2>Arguments</h2>
<p><i>pool</i></p>
<dl>
<dd>
<dd>dma pool that will produce the block</dl>
<p> <i>mem_flags</i></p>
<dl>
<dd>GFP_* bitmask</dl>
<p> <i>handle</i></p>
<dl>
<dd>pointer to dma address of block</dl>
<h2>Description</h2>
<p>This returns the kernel virtual address of a currently unused block, and reports its dma address through the handle. If such a memory block can&#8217;t be allocated, <code>NULL</code> is returned.</p>
<h2>Copyright</h2>
