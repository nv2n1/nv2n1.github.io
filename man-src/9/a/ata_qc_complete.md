---
title: "ata_qc_complete(9)"
name: "ata_qc_complete"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_qc_complete/"
description: "ata_qc_complete – Complete an active ATA command"
---

<p>ata_qc_complete &#8211; Complete an active ATA command</p>
<h2>Synopsis</h2>
<pre><code>void ata_qc_complete(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command to complete</dl>
<h2>Description</h2>
<p>Indicate to the mid and upper layers that an ATA command has completed, with either an ok or not-ok status. </p>
<p> Refrain from calling this function multiple times when successfully completing multiple NCQ commands. <code>ata_qc_complete_multiple</code> should be used instead, which will properly update IRQ expect state. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
