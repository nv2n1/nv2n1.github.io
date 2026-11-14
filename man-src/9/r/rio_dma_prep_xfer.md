---
title: "rio_dma_prep_xfer(9)"
name: "rio_dma_prep_xfer"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_dma_prep_xfer/"
description: "rio_dma_prep_xfer – RapidIO specific wrapper for device_prep_slave_sg callback defined by DMAENGINE."
---

<p>rio_dma_prep_xfer &#8211; RapidIO specific wrapper for device_prep_slave_sg callback defined by DMAENGINE.</p>
<h2>Synopsis</h2>
<pre><code>struct dma_async_tx_descriptor *rio_dma_prep_xfer(struct dma_chan *dchan, u16 destid, struct rio_dma_data *data, enum dma_transfer_direction direction, unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>dchan</i></p>
<dl>
<dd>
<dd>DMA channel to configure</dl>
<p> <i>destid</i></p>
<dl>
<dd>target RapidIO device destination ID</dl>
<p> <i>data</i></p>
<dl>
<dd>RIO specific data descriptor</dl>
<p> <i>direction</i></p>
<dl>
<dd>DMA data transfer direction (TO or FROM the device)</dl>
<p> <i>flags</i></p>
<dl>
<dd>dmaengine defined flags</dl>
<h2>Description</h2>
<p>Initializes RapidIO capable DMA channel for the specified data transfer. Uses DMA channel private extension to pass information related to remote target RIO device.</p>
<h2>Return</h2>
<p>pointer to DMA transaction descriptor if successful, error-valued pointer or NULL if failed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
