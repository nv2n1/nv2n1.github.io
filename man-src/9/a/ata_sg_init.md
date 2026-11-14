---
title: "ata_sg_init(9)"
name: "ata_sg_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sg_init/"
description: "ata_sg_init – Associate command with scatter-gather table."
---

<p>ata_sg_init &#8211; Associate command with scatter-gather table.</p>
<h2>Synopsis</h2>
<pre><code>void ata_sg_init(struct ata_queued_cmd *qc, struct scatterlist *sg, unsigned int n_elem);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command to be associated</dl>
<p> <i>sg</i></p>
<dl>
<dd>Scatter-gather table.</dl>
<p> <i>n_elem</i></p>
<dl>
<dd>Number of elements in s/g table.</dl>
<h2>Description</h2>
<p>Initialize the data-related elements of queued_cmd <i>qc</i> to point to a scatter-gather table <i>sg</i>, containing <i>n_elem</i> elements. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
