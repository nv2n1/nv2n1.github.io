---
title: "ata_scsi_mode_select_xlat(9)"
name: "ata_scsi_mode_select_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_mode_select_xlat/"
description: "ata_scsi_mode_select_xlat – Simulate MODE SELECT 6, 10 commands"
---

<p>ata_scsi_mode_select_xlat &#8211; Simulate MODE SELECT 6, 10 commands</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsi_mode_select_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<h2>Description</h2>
<p>Converts a MODE SELECT command to an ATA SET FEATURES taskfile. Assume this is invoked for direct access devices (e.g. disks) only. There should be no block descriptor for other device types. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
