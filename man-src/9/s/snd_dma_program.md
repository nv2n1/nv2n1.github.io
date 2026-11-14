---
title: "snd_dma_program(9)"
name: "snd_dma_program"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dma_program/"
---

snd_dma_program - program an ISA DMA transfer

<h2>Synopsis</h2>

<pre><code>void snd_dma_program(unsigned long dma, unsigned long addr, unsigned int size, unsigned short mode);</code></pre>

<h2>Arguments</h2>

<i>dma</i>
<dl><dd><dd>the dma number</dl>
 

 <i>addr</i>
<dl><dd>the physical address of the buffer</dl>
 

 <i>size</i>
<dl><dd>the DMA transfer size</dl>
 

 <i>mode</i>
<dl><dd>the DMA transfer mode, DMA_MODE_XXX</dl>

<h2>Description</h2>

Programs an ISA DMA transfer for the given buffer.

<h2>Copyright</h2>


