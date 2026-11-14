---
title: "snd_dmaengine_pcm_open(9)"
name: "snd_dmaengine_pcm_open"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_open/"
---

snd_dmaengine_pcm_open - Open a dmaengine based PCM substream

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_open(struct snd_pcm_substream *substream, struct dma_chan *chan);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>chan</i>
<dl><dd>DMA channel to use for data transfers</dl>

<h2>Description</h2>

Returns 0 on success, a negative error code otherwise. 

 The function should usually be called from the pcm open callback. Note that this function will use private_data field of the substream's runtime. So it is not available to your pcm driver implementation.

<h2>Copyright</h2>


