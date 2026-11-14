---
title: "snd_dma_pointer(9)"
name: "snd_dma_pointer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dma_pointer/"
---

snd_dma_pointer - return the current pointer to DMA transfer buffer in bytes

<h2>Synopsis</h2>

<pre><code>unsigned int snd_dma_pointer(unsigned long dma, unsigned int size);</code></pre>

<h2>Arguments</h2>

<i>dma</i>
<dl><dd><dd>the dma number</dl>
 

 <i>size</i>
<dl><dd>the dma transfer size</dl>

<h2>Return</h2>

The current pointer in DMA transfer buffer in bytes.

<h2>Copyright</h2>


