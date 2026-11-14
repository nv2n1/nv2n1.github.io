---
title: "set_dma_reserve(9)"
name: "set_dma_reserve"
section: "9"
letter: "s"
url: "/docs/linux/man/9-set_dma_reserve/"
---

set_dma_reserve - set the specified number of pages reserved in the first zone

<h2>Synopsis</h2>

<pre><code>void set_dma_reserve(unsigned long new_dma_reserve);</code></pre>

<h2>Arguments</h2>

<i>new_dma_reserve</i>
<dl><dd><dd>The number of pages to mark reserved</dl>

<h2>Description</h2>

The per-cpu batchsize and zone watermarks are determined by managed_pages. In the DMA zone, a significant percentage may be consumed by kernel image and other unfreeable allocations which can skew the watermarks badly. This function may optionally be used to account for unfreeable pages in the first zone (e.g., ZONE_DMA). The effect will be lower watermarks and smaller per-cpu batchsize.

<h2>Copyright</h2>


