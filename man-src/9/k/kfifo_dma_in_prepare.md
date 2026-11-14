---
title: "kfifo_dma_in_prepare(9)"
name: "kfifo_dma_in_prepare"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_dma_in_prepare/"
description: "kfifo_dma_in_prepare – setup a scatterlist for DMA input"
---

<p>kfifo_dma_in_prepare &#8211; setup a scatterlist for DMA input</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_dma_in_prepare(</code><i>fifo</i><code>, </code><i>sgl</i><code>, </code><i>nents</i><code>, </code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>sgl</i></p>
<dl>
<dd>pointer to the scatterlist array</dl>
<p> <i>nents</i></p>
<dl>
<dd>number of entries in the scatterlist array</dl>
<p> <i>len</i></p>
<dl>
<dd>number of elements to transfer</dl>
<h2>Description</h2>
<p>This macro fills a scatterlist for DMA input. It returns the number entries in the scatterlist array. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macros.</p>
<h2>Copyright</h2>
