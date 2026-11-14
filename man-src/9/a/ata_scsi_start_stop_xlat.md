---
title: "ata_scsi_start_stop_xlat(9)"
name: "ata_scsi_start_stop_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_start_stop_xlat/"
description: "ata_scsi_start_stop_xlat – Translate SCSI START STOP UNIT command"
---

<p>ata_scsi_start_stop_xlat &#8211; Translate SCSI START STOP UNIT command</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_start_stop_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<h2>Description</h2>
<p>Sets up an ATA taskfile to issue STANDBY (to stop) or READ VERIFY (to start). Perhaps these commands should be preceded by CHECK POWER MODE to see what power mode the device is already in. [See SAT revision 5 at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>] </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, non-zero on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
