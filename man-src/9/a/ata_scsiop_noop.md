---
title: "ata_scsiop_noop(9)"
name: "ata_scsiop_noop"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsiop_noop/"
description: "ata_scsiop_noop – Command handler that simply returns success."
---

<p>ata_scsiop_noop &#8211; Command handler that simply returns success.</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsiop_noop(struct ata_scsi_args *args, u8 *rbuf);</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device IDENTIFY data / SCSI command of interest.</dl>
<p> <i>rbuf</i></p>
<dl>
<dd>Response buffer, to which simulated SCSI cmd output is sent.</dl>
<h2>Description</h2>
<p>No operation. Simply returns success to caller, to indicate that the caller should successfully complete this SCSI command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
