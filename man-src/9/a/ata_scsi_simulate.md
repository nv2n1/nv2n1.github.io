---
title: "ata_scsi_simulate(9)"
name: "ata_scsi_simulate"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_simulate/"
description: "ata_scsi_simulate – simulate SCSI command on ATA device"
---

<p>ata_scsi_simulate &#8211; simulate SCSI command on ATA device</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_simulate(struct ata_device *dev, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the target device</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command being sent to device.</dl>
<h2>Description</h2>
<p>Interprets and directly executes a select list of SCSI commands that can be handled internally. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
