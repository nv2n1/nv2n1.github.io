---
title: "ata_scsiop_report_luns(9)"
name: "ata_scsiop_report_luns"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsiop_report_luns/"
description: "ata_scsiop_report_luns – Simulate REPORT LUNS command"
---

<p>ata_scsiop_report_luns &#8211; Simulate REPORT LUNS command</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsiop_report_luns(struct ata_scsi_args *args, u8 *rbuf);</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device IDENTIFY data / SCSI command of interest.</dl>
<p> <i>rbuf</i></p>
<dl>
<dd>Response buffer, to which simulated SCSI cmd output is sent.</dl>
<h2>Description</h2>
<p>Simulate REPORT LUNS command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
