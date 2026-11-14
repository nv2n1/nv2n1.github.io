---
title: "z8530_dma_status(9)"
name: "z8530_dma_status"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_dma_status/"
description: "z8530_dma_status – Handle a DMA status exception"
---

<p>z8530_dma_status &#8211; Handle a DMA status exception</p>
<h2>Synopsis</h2>
<pre><code>void z8530_dma_status(struct z8530_channel *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>Z8530 channel to process </p>
<p> A status event occurred on the Z8530. We receive these for two reasons when in DMA mode. Firstly if we finished a packet transfer we get one and kick the next packet out. Secondly we may see a DCD change.</dl>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
