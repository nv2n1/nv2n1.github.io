---
title: "dma_pool_free(9)"
name: "dma_pool_free"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dma_pool_free/"
---

dma_pool_free - put block back into dma pool

<h2>Synopsis</h2>

<pre><code>void dma_pool_free(struct dma_pool *pool, void *vaddr, dma_addr_t dma);</code></pre>

<h2>Arguments</h2>

<i>pool</i>
<dl><dd><dd>the dma pool holding the block</dl>
 

 <i>vaddr</i>
<dl><dd>virtual address of block</dl>
 

 <i>dma</i>
<dl><dd>dma address of block</dl>

<h2>Description</h2>

Caller promises neither device nor driver will again touch this block unless it is first re-allocated.

<h2>Copyright</h2>


