---
title: "dma_pool_destroy(9)"
name: "dma_pool_destroy"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dma_pool_destroy/"
description: "dma_pool_destroy – destroys a pool of dma memory blocks."
---

<p>dma_pool_destroy &#8211; destroys a pool of dma memory blocks.</p>
<h2>Synopsis</h2>
<pre><code>void dma_pool_destroy(struct dma_pool *pool);</code></pre>
<h2>Arguments</h2>
<p><i>pool</i></p>
<dl>
<dd>
<dd>dma pool that will be destroyed</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Caller guarantees that no more memory from the pool is in use, and that nothing will try to use the pool after this call.</p>
<h2>Copyright</h2>
