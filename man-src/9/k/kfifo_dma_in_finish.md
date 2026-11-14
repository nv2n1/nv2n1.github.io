---
title: "kfifo_dma_in_finish(9)"
name: "kfifo_dma_in_finish"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_dma_in_finish/"
description: "kfifo_dma_in_finish – finish a DMA IN operation"
---

<p>kfifo_dma_in_finish &#8211; finish a DMA IN operation</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_dma_in_finish(</code><i>fifo</i><code>, </code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to received</dl>
<h2>Description</h2>
<p>This macro finish a DMA IN operation. The in counter will be updated by the len parameter. No error checking will be done. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macros.</p>
<h2>Copyright</h2>
