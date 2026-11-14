---
title: "ata_qc_free(9)"
name: "ata_qc_free"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_qc_free/"
description: "ata_qc_free – free unused ata_queued_cmd"
---

<p>ata_qc_free &#8211; free unused ata_queued_cmd</p>
<h2>Synopsis</h2>
<pre><code>void ata_qc_free(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command to complete</dl>
<h2>Description</h2>
<p>Designed to free unused ata_queued_cmd object in case something prevents using it. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
