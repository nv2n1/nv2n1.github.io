---
title: "dmam_pool_create(9)"
name: "dmam_pool_create"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmam_pool_create/"
description: "dmam_pool_create – Managed dma_pool_create"
---

<p>dmam_pool_create &#8211; Managed <code>dma_pool_create</code></p>
<h2>Synopsis</h2>
<pre><code>struct dma_pool *dmam_pool_create(const char *name, struct device *dev, size_t size, size_t align, size_t allocation);</code></pre>
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
<p> <i>allocation</i></p>
<dl>
<dd>returned blocks won&#8217;t cross this boundary (or zero)</dl>
<h2>Description</h2>
<p>Managed <code>dma_pool_create</code>. DMA pool created with this function is automatically destroyed on driver detach.</p>
<h2>Copyright</h2>
