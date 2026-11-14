---
title: "ata_scsi_qc_new(9)"
name: "ata_scsi_qc_new"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_qc_new/"
description: "ata_scsi_qc_new – acquire new ata_queued_cmd reference"
---

<p>ata_scsi_qc_new &#8211; acquire new ata_queued_cmd reference</p>
<h2>Synopsis</h2>
<pre><code>struct ata_queued_cmd *ata_scsi_qc_new(struct ata_device *dev, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device to which the new command is attached</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command that originated this ATA command</dl>
<h2>Description</h2>
<p>Obtain a reference to an unused ata_queued_cmd structure, which is the basic libata structure representing a single ATA command sent to the hardware. </p>
<p> If a command was available, fill in the SCSI-specific portions of the structure with information on the current command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Command allocated, or <code>NULL</code> if none available.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
