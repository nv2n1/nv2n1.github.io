---
title: "rio_request_mport_dma(9)"
name: "rio_request_mport_dma"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_mport_dma/"
description: "rio_request_mport_dma – request RapidIO capable DMA channel associated with specified local RapidIO mport device."
---

<p>rio_request_mport_dma &#8211; request RapidIO capable DMA channel associated with specified local RapidIO mport device.</p>
<h2>Synopsis</h2>
<pre><code>struct dma_chan *rio_request_mport_dma(struct rio_mport *mport);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO mport to perform DMA data transfers</dl>
<h2>Description</h2>
<p>Returns pointer to allocated DMA channel or NULL if failed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
