---
title: "snd_dmaengine_pcm_request_channel(9)"
name: "snd_dmaengine_pcm_request_channel"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_request_channel/"
---

snd_dmaengine_pcm_request_channel - Request channel for the dmaengine PCM

<h2>Synopsis</h2>

<pre><code>struct dma_chan *snd_dmaengine_pcm_request_channel(dma_filter_fn filter_fn, void *filter_data);</code></pre>

<h2>Arguments</h2>

<i>filter_fn</i>
<dl><dd><dd>Filter function used to request the DMA channel</dl>
 

 <i>filter_data</i>
<dl><dd>Data passed to the DMA filter function</dl>

<h2>Description</h2>

Returns NULL or the requested DMA channel. 

 This function request a DMA channel for usage with dmaengine PCM.

<h2>Copyright</h2>


