---
title: "dma_pool_create(9)"
name: "dma_pool_create"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dma_pool_create/"
description: "dma_pool_create – Creates a pool of consistent memory blocks, for dma."
---

<p>dma_pool_create &#8211; Creates a pool of consistent memory blocks, for dma.</p>
<h2>Synopsis</h2>
<pre><code>struct dma_pool *dma_pool_create(const char *name, struct device *dev, size_t size, size_t align, size_t boundary);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>name of pool, for diagnostics</dl>
<p> <i>dev</i></p>
<dl>
<dd>device that will be doing the DMA</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the blocks in this pool.</dl>
<p> <i>align</i></p>
<dl>
<dd>alignment requirement for blocks; must be a power of two</dl>
<p> <i>boundary</i></p>
<dl>
<dd>returned blocks won&#8217;t cross this power of two boundary</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Returns a dma allocation pool with the requested characteristics, or null if one can&#8217;t be created. Given one of these pools, <code>dma_pool_alloc</code> may be used to allocate memory. Such memory will all have &#8220;consistent&#8221; DMA mappings, accessible by the device and its driver without using cache flushing primitives. The actual size of blocks allocated may be larger than requested because of alignment. </p>
<p> If <i>boundary</i> is nonzero, objects returned from <code>dma_pool_alloc</code> won&#8217;t cross that size boundary. This is useful for devices which have addressing restrictions on individual DMA transfers, such as not crossing boundaries of 4KBytes.</p>
<h2>Copyright</h2>
