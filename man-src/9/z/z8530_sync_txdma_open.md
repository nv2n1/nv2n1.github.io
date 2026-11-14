---
title: "z8530_sync_txdma_open(9)"
name: "z8530_sync_txdma_open"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_sync_txdma_open/"
description: "z8530_sync_txdma_open – Open a Z8530 for TX driven DMA"
---

<p>z8530_sync_txdma_open &#8211; Open a Z8530 for TX driven DMA</p>
<h2>Synopsis</h2>
<pre><code>int z8530_sync_txdma_open(struct net_device *dev, struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>The network device to attach</dl>
<p> <i>c</i></p>
<dl>
<dd>The Z8530 channel to configure in sync DMA mode.</dl>
<h2>Description</h2>
<p>Set up a Z85x30 device for synchronous DMA transmission. One ISA DMA channel must be available for this to work. The receive side is run in PIO mode, but then it has the bigger FIFO.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
