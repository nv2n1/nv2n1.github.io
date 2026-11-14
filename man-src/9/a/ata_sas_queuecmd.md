---
title: "ata_sas_queuecmd(9)"
name: "ata_sas_queuecmd"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_queuecmd/"
description: "ata_sas_queuecmd – Issue SCSI cdb to libata-managed device"
---

<p>ata_sas_queuecmd &#8211; Issue SCSI cdb to libata-managed device</p>
<h2>Synopsis</h2>
<pre><code>int ata_sas_queuecmd(struct scsi_cmnd *cmd, struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>SCSI command to be sent</dl>
<p> <i>ap</i></p>
<dl>
<dd>ATA port to which the command is being sent</dl>
<h2>Return</h2>
<p>Return value from <code>__ata_scsi_queuecmd</code> if <i>cmd</i> can be queued, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
