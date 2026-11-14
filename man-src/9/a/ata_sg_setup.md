---
title: "ata_sg_setup(9)"
name: "ata_sg_setup"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sg_setup/"
description: "ata_sg_setup – DMA-map the scatter-gather table associated with a command."
---

<p>ata_sg_setup &#8211; DMA-map the scatter-gather table associated with a command.</p>
<h2>Synopsis</h2>
<pre><code>int ata_sg_setup(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command with scatter-gather table to be mapped.</dl>
<h2>Description</h2>
<p>DMA-map the scatter-gather table associated with queued_cmd <i>qc</i>. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, negative on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
