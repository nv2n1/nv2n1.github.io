---
title: "ata_scsi_flush_xlat(9)"
name: "ata_scsi_flush_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_flush_xlat/"
description: "ata_scsi_flush_xlat – Translate SCSI SYNCHRONIZE CACHE command"
---

<p>ata_scsi_flush_xlat &#8211; Translate SCSI SYNCHRONIZE CACHE command</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_flush_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<h2>Description</h2>
<p>Sets up an ATA taskfile to issue FLUSH CACHE or FLUSH CACHE EXT. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, non-zero on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
