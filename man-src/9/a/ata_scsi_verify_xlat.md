---
title: "ata_scsi_verify_xlat(9)"
name: "ata_scsi_verify_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_verify_xlat/"
description: "ata_scsi_verify_xlat – Translate SCSI VERIFY command into an ATA one"
---

<p>ata_scsi_verify_xlat &#8211; Translate SCSI VERIFY command into an ATA one</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_verify_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<h2>Description</h2>
<p>Converts SCSI VERIFY command to an ATA READ VERIFY command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, non-zero on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
