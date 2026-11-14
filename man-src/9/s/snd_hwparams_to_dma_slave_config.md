---
title: "snd_hwparams_to_dma_slave_config(9)"
name: "snd_hwparams_to_dma_slave_config"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_hwparams_to_dma_slave_config/"
---

snd_hwparams_to_dma_slave_config - Convert hw_params to dma_slave_config

<h2>Synopsis</h2>

<pre><code>int snd_hwparams_to_dma_slave_config(const struct snd_pcm_substream *substream, const struct snd_pcm_hw_params *params, struct dma_slave_config *slave_config);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>params</i>
<dl><dd>hw_params</dl>
 

 <i>slave_config</i>
<dl><dd>DMA slave config</dl>

<h2>Description</h2>

This function can be used to initialize a dma_slave_config from a substream and hw_params in a dmaengine based PCM driver implementation.

<h2>Copyright</h2>


