---
title: "rio_request_dma(9)"
name: "rio_request_dma"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_dma/"
description: "rio_request_dma – request RapidIO capable DMA channel that supports specified target RapidIO device."
---

<p>rio_request_dma &#8211; request RapidIO capable DMA channel that supports specified target RapidIO device.</p>
<h2>Synopsis</h2>
<pre><code>struct dma_chan *rio_request_dma(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device associated with DMA transfer</dl>
<h2>Description</h2>
<p>Returns pointer to allocated DMA channel or NULL if failed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
