---
title: "snd_dmaengine_pcm_prepare_slave_config(9)"
name: "snd_dmaengine_pcm_prepare_slave_config"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_prepare_slave_config/"
---

snd_dmaengine_pcm_prepare_slave_config - Generic prepare_slave_config callback

<h2>Synopsis</h2>

<pre><code>int snd_dmaengine_pcm_prepare_slave_config(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *params, struct dma_slave_config *slave_config);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>params</i>
<dl><dd>hw_params</dl>
 

 <i>slave_config</i>
<dl><dd>DMA slave config to prepare</dl>

<h2>Description</h2>

This function can be used as a generic prepare_slave_config callback for platforms which make use of the snd_dmaengine_dai_dma_data struct for their DAI DMA data. Internally the function will first call snd_hwparams_to_dma_slave_config to fill in the slave config based on the hw_params, followed by snd_dmaengine_set_config_from_dai_data to fill in the remaining fields based on the DAI DMA data.

<h2>Copyright</h2>


