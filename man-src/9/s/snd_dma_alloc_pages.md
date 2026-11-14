---
title: "snd_dma_alloc_pages(9)"
name: "snd_dma_alloc_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dma_alloc_pages/"
---

snd_dma_alloc_pages - allocate the buffer area according to the given type

<h2>Synopsis</h2>

<pre><code>int snd_dma_alloc_pages(int type, struct device *device, size_t size, struct snd_dma_buffer *dmab);</code></pre>

<h2>Arguments</h2>

<i>type</i>
<dl><dd><dd>the DMA buffer type</dl>
 

 <i>device</i>
<dl><dd>the device pointer</dl>
 

 <i>size</i>
<dl><dd>the buffer size to allocate</dl>
 

 <i>dmab</i>
<dl><dd>buffer allocation record to store the allocated data</dl>

<h2>Description</h2>

Calls the memory-allocator function for the corresponding buffer type.

<h2>Return</h2>

Zero if the buffer with the given size is allocated successfully, otherwise a negative value on error.

<h2>Copyright</h2>


