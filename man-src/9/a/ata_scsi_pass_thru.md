---
title: "ata_scsi_pass_thru(9)"
name: "ata_scsi_pass_thru"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_pass_thru/"
description: "ata_scsi_pass_thru – convert ATA pass-thru CDB to taskfile"
---

<p>ata_scsi_pass_thru &#8211; convert ATA pass-thru CDB to taskfile</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_pass_thru(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>command structure to be initialized</dl>
<h2>Description</h2>
<p>Handles either 12 or 16-byte versions of the CDB.</p>
<h2>Return</h2>
<p>Zero on success, non-zero on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
