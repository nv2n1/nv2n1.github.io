---
title: "ata_scsiop_mode_sense(9)"
name: "ata_scsiop_mode_sense"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsiop_mode_sense/"
description: "ata_scsiop_mode_sense – Simulate MODE SENSE 6, 10 commands"
---

<p>ata_scsiop_mode_sense &#8211; Simulate MODE SENSE 6, 10 commands</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsiop_mode_sense(struct ata_scsi_args *args, u8 *rbuf);</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device IDENTIFY data / SCSI command of interest.</dl>
<p> <i>rbuf</i></p>
<dl>
<dd>Response buffer, to which simulated SCSI cmd output is sent.</dl>
<h2>Description</h2>
<p>Simulate MODE SENSE commands. Assume this is invoked for direct access devices (e.g. disks) only. There should be no block descriptor for other device types. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
