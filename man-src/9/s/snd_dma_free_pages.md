---
title: "snd_dma_free_pages(9)"
name: "snd_dma_free_pages"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dma_free_pages/"
description: "snd_dma_free_pages – release the allocated buffer"
---

<p>snd_dma_free_pages &#8211; release the allocated buffer</p>
<h2>Synopsis</h2>
<pre><code>void snd_dma_free_pages(struct snd_dma_buffer *dmab);</code></pre>
<h2>Arguments</h2>
<p><i>dmab</i></p>
<dl>
<dd>
<dd>the buffer allocation record to release</dl>
<h2>Description</h2>
<p>Releases the allocated buffer via <code>snd_dma_alloc_pages</code>.</p>
<h2>Copyright</h2>
