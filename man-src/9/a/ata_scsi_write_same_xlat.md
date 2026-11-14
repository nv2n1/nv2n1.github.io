---
title: "ata_scsi_write_same_xlat(9)"
name: "ata_scsi_write_same_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_write_same_xlat/"
description: "ata_scsi_write_same_xlat – SATL Write Same to ATA SCT Write Same"
---

<p>ata_scsi_write_same_xlat &#8211; SATL Write Same to ATA SCT Write Same</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_write_same_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command to be translated</dl>
<h2>Description</h2>
<p>Translate a SCSI WRITE SAME command to be either a DSM TRIM command or an SCT Write Same command. Based on WRITE SAME has the UNMAP flag When set translate to DSM TRIM When clear translate to SCT Write Same</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
