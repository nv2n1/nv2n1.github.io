---
title: "z8530_sync_dma_close(9)"
name: "z8530_sync_dma_close"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_sync_dma_close/"
description: "z8530_sync_dma_close – Close down DMA I/O"
---

<p>z8530_sync_dma_close &#8211; Close down DMA I/O</p>
<h2>Synopsis</h2>
<pre><code>int z8530_sync_dma_close(struct net_device *dev, struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Network device to detach</dl>
<p> <i>c</i></p>
<dl>
<dd>Z8530 channel to move into discard mode</dl>
<h2>Description</h2>
<p>Shut down a DMA mode synchronous interface. Halt the DMA, and free the buffers.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
