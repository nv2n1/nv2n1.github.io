---
title: "snd_dmaengine_pcm_open_request_chan(9)"
name: "snd_dmaengine_pcm_open_request_chan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_open_request_chan/"
---

snd_dmaengine_pcm_open_request_chan - Open a dmaengine based PCM substream and request channel

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_open_request_chan(struct snd_pcm_substream *substream, dma_filter_fn filter_fn, void *filter_data);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>filter_fn</i>
<dl><dd>Filter function used to request the DMA channel</dl>
 

 <i>filter_data</i>
<dl><dd>Data passed to the DMA filter function</dl>

<h2>Description</h2>

Returns 0 on success, a negative error code otherwise. 

 This function will request a DMA channel using the passed filter function and data. The function should usually be called from the pcm open callback. Note that this function will use private_data field of the substream's runtime. So it is not available to your pcm driver implementation.

<h2>Copyright</h2>


