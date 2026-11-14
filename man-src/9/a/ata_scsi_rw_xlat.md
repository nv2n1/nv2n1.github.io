---
title: "ata_scsi_rw_xlat(9)"
name: "ata_scsi_rw_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_rw_xlat/"
description: "ata_scsi_rw_xlat – Translate SCSI r/w command into an ATA one"
---

<p>ata_scsi_rw_xlat &#8211; Translate SCSI r/w command into an ATA one</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_rw_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<h2>Description</h2>
<p>Converts any of six SCSI read/write commands into the ATA counterpart, including starting sector (LBA), sector count, and taking into account the device&#8217;s LBA48 support. </p>
<p> Commands <code>READ_6</code>, <code>READ_10</code>, <code>READ_16</code>, <code>WRITE_6</code>, <code>WRITE_10</code>, and <code>WRITE_16</code> are currently supported. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, non-zero on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
