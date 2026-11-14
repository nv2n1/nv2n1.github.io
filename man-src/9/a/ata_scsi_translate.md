---
title: "ata_scsi_translate(9)"
name: "ata_scsi_translate"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_translate/"
description: "ata_scsi_translate – Translate then issue SCSI command to ATA device"
---

<p>ata_scsi_translate &#8211; Translate then issue SCSI command to ATA device</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_translate(struct ata_device *dev, struct scsi_cmnd *cmd, ata_xlat_func_t xlat_func);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device to which the command is addressed</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command to execute</dl>
<p> <i>xlat_func</i></p>
<dl>
<dd>Actor which translates <i>cmd</i> to an ATA taskfile</dl>
<h2>Description</h2>
<p>Our -&gt;<code>queuecommand</code> function has decided that the SCSI command issued can be directly translated into an ATA command, rather than handled internally. </p>
<p> This function sets up an ata_queued_cmd structure for the SCSI command, and sends that ata_queued_cmd to the hardware. </p>
<p> The xlat_func argument (actor) returns 0 if ready to execute ATA command, else 1 to finish translation. If 1 is returned then cmd-&gt;result (and possibly cmd-&gt;sense_buffer) are assumed to be set reflecting an error condition or clean (early) termination. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>0 on success, SCSI_ML_QUEUE_DEVICE_BUSY if the command needs to be deferred.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
