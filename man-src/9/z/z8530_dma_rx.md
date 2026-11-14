---
title: "z8530_dma_rx(9)"
name: "z8530_dma_rx"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_dma_rx/"
description: "z8530_dma_rx – Handle a DMA RX event"
---

<p>z8530_dma_rx &#8211; Handle a DMA RX event</p>
<h2>Synopsis</h2>
<pre><code>void z8530_dma_rx(struct z8530_channel *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>Channel to handle</dl>
<h2>Description</h2>
<p>Non bus mastering DMA interfaces for the Z8x30 devices. This is really pretty PC specific. The DMA mode means that most receive events are handled by the DMA hardware. We get a kick here only if a frame ended.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
