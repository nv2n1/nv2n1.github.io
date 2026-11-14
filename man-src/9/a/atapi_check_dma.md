---
title: "atapi_check_dma(9)"
name: "atapi_check_dma"
section: "9"
letter: "a"
url: "/docs/linux/man/9-atapi_check_dma/"
description: "atapi_check_dma – Check whether ATAPI DMA can be supported"
---

<p>atapi_check_dma &#8211; Check whether ATAPI DMA can be supported</p>
<h2>Synopsis</h2>
<pre><code>int atapi_check_dma(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Metadata associated with taskfile to check</dl>
<h2>Description</h2>
<p>Allow low-level driver to filter ATA PACKET commands, returning a status indicating whether or not it is OK to use DMA for the supplied PACKET command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>0 when ATAPI DMA can be used nonzero otherwise</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
