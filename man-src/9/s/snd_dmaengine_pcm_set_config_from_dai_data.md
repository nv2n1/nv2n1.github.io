---
title: "snd_dmaengine_pcm_set_config_from_dai_data(9)"
name: "snd_dmaengine_pcm_set_config_from_dai_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_dmaengine_pcm_set_config_from_dai_data/"
---

snd_dmaengine_pcm_set_config_from_dai_data - Initializes a dma slave config using DAI DMA data.

<h2>Synopsis</h2>

<pre><code>void snd_dmaengine_pcm_set_config_from_dai_data(const struct snd_pcm_substream *substream, const struct snd_dmaengine_dai_dma_data *dma_data, struct dma_slave_config *slave_config);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>dma_data</i>
<dl><dd>DAI DMA data</dl>
 

 <i>slave_config</i>
<dl><dd>DMA slave configuration</dl>

<h2>Description</h2>

Initializes the {dst,src}_addr, {dst,src}_maxburst, {dst,src}_addr_width and slave_id fields of the DMA slave config from the same fields of the DAI DMA data struct. The src and dst fields will be initialized depending on the direction of the substream. If the substream is a playback stream the dst fields will be initialized, if it is a capture stream the src fields will be initialized. The {dst,src}_addr_width field will only be initialized if the SND_DMAENGINE_PCM_DAI_FLAG_PACK flag is set or if the addr_width field of the DAI DMA data struct is not equal to DMA_SLAVE_BUSWIDTH_UNDEFINED. If both conditions are met the latter takes priority.

<h2>Copyright</h2>


