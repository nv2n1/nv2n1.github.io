---
title: "ata_scsi_rbuf_fill(9)"
name: "ata_scsi_rbuf_fill"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_rbuf_fill/"
description: "ata_scsi_rbuf_fill – wrapper for SCSI command simulators"
---

<p>ata_scsi_rbuf_fill &#8211; wrapper for SCSI command simulators</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_rbuf_fill(struct ata_scsi_args *args, unsigned int (*actor)(struct ata_scsi_args *args, u8 *rbuf));</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device IDENTIFY data / SCSI command of interest.</dl>
<p> <i>actor</i></p>
<dl>
<dd>Callback hook for desired SCSI command simulator</dl>
<h2>Description</h2>
<p>Takes care of the hard work of simulating a SCSI command&#8230; Mapping the response buffer, calling the command&#8217;s handler, and handling the handler&#8217;s return value. This return value indicates whether the handler wishes the SCSI command to be completed successfully (0), or not (in which case cmd-&gt;result and sense buffer are assumed to be set). </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
