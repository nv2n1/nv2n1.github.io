---
title: "ata_sg_clean(9)"
name: "ata_sg_clean"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sg_clean/"
description: "ata_sg_clean – Unmap DMA memory associated with command"
---

<p>ata_sg_clean &#8211; Unmap DMA memory associated with command</p>
<h2>Synopsis</h2>
<pre><code>void ata_sg_clean(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command containing DMA memory to be released</dl>
<h2>Description</h2>
<p>Unmap all mapped DMA memory associated with this command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
