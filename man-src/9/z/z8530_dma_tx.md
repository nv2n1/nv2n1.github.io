---
title: "z8530_dma_tx(9)"
name: "z8530_dma_tx"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_dma_tx/"
description: "z8530_dma_tx – Handle a DMA TX event"
---

<p>z8530_dma_tx &#8211; Handle a DMA TX event</p>
<h2>Synopsis</h2>
<pre><code>void z8530_dma_tx(struct z8530_channel *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>The Z8530 channel to handle</dl>
<h2>Description</h2>
<p>We have received an interrupt while doing DMA transmissions. It shouldn&#8217;t happen. Scream loudly if it does.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
