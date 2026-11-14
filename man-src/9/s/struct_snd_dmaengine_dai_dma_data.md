---
title: "struct_snd_dmaengine_dai_dma_data(9)"
name: "struct_snd_dmaengine_dai_dma_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_dmaengine_dai_dma_data/"
---

struct_snd_dmaengine_dai_dma_data - DAI DMA configuration data

<h2>Synopsis</h2>

<pre><code>struct snd_dmaengine_dai_dma_data {
    dma_addr_t addr;
    enum dma_slave_buswidth addr_width;
    u32 maxburst;
    unsigned int slave_id;
    void *filter_data;
    const char *chan_name;
    unsigned int fifo_size;
    unsigned int flags;
};</code></pre>

<h2>Members</h2>

addr
<dl><dd>Address of the DAI data source or destination register.</dl>
 

 addr_width
<dl><dd>Width of the DAI data source or destination register.</dl>
 

 maxburst
<dl><dd>Maximum number of words(note: words, as in units of the src_addr_width member, not bytes) that can be send to or received from the DAI in one burst.</dl>
 

 slave_id
<dl><dd>Slave requester id for the DMA channel.</dl>
 

 filter_data
<dl><dd>Custom DMA channel filter data, this will usually be used when requesting the DMA channel.</dl>
 

 chan_name
<dl><dd>Custom channel name to use when requesting DMA channel.</dl>
 

 fifo_size
<dl><dd>FIFO size of the DAI controller in bytes</dl>
 

 flags
<dl><dd>PCM_DAI flags, only SND_DMAENGINE_PCM_DAI_FLAG_PACK for now</dl>

<h2>Copyright</h2>


