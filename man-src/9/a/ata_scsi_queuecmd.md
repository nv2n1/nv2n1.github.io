---
title: "ata_scsi_queuecmd(9)"
name: "ata_scsi_queuecmd"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_queuecmd/"
description: "ata_scsi_queuecmd – Issue SCSI cdb to libata-managed device"
---

<p>ata_scsi_queuecmd &#8211; Issue SCSI cdb to libata-managed device</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_queuecmd(struct Scsi_Host *shost, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>SCSI host of command to be sent</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command to be sent</dl>
<h2>Description</h2>
<p>In some cases, this function translates SCSI commands into ATA taskfiles, and queues the taskfiles to be sent to hardware. In other cases, this function simulates a SCSI device by evaluating and responding to certain SCSI commands. This creates the overall effect of ATA and ATAPI devices appearing as SCSI devices. </p>
<p> LOCKING: ATA host lock</p>
<h2>Return</h2>
<p>Return value from <code>__ata_scsi_queuecmd</code> if <i>cmd</i> can be queued, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
