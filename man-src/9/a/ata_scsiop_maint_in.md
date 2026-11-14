---
title: "ata_scsiop_maint_in(9)"
name: "ata_scsiop_maint_in"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsiop_maint_in/"
description: "ata_scsiop_maint_in – Simulate a subset of MAINTENANCE_IN"
---

<p>ata_scsiop_maint_in &#8211; Simulate a subset of MAINTENANCE_IN</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsiop_maint_in(struct ata_scsi_args *args, u8 *rbuf);</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device MAINTENANCE_IN data / SCSI command of interest.</dl>
<p> <i>rbuf</i></p>
<dl>
<dd>Response buffer, to which simulated SCSI cmd output is sent.</dl>
<h2>Description</h2>
<p>Yields a subset to satisfy <code>scsi_report_opcode</code> </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
