---
title: "z8530_sync_dma_open(9)"
name: "z8530_sync_dma_open"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_sync_dma_open/"
description: "z8530_sync_dma_open – Open a Z8530 for DMA I/O"
---

<p>z8530_sync_dma_open &#8211; Open a Z8530 for DMA I/O</p>
<h2>Synopsis</h2>
<pre><code>int z8530_sync_dma_open(struct net_device *dev, struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>The network device to attach</dl>
<p> <i>c</i></p>
<dl>
<dd>The Z8530 channel to configure in sync DMA mode.</dl>
<h2>Description</h2>
<p>Set up a Z85x30 device for synchronous DMA in both directions. Two ISA DMA channels must be available for this to work. We assume ISA DMA driven I/O and PC limits on access.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
