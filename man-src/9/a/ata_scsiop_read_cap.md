---
title: "ata_scsiop_read_cap(9)"
name: "ata_scsiop_read_cap"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsiop_read_cap/"
description: "ata_scsiop_read_cap – Simulate READ CAPACITY[ 16] commands"
---

<p>ata_scsiop_read_cap &#8211; Simulate READ CAPACITY[ 16] commands</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_scsiop_read_cap(struct ata_scsi_args *args, u8 *rbuf);</code></pre>
<h2>Arguments</h2>
<p><i>args</i></p>
<dl>
<dd>
<dd>device IDENTIFY data / SCSI command of interest.</dl>
<p> <i>rbuf</i></p>
<dl>
<dd>Response buffer, to which simulated SCSI cmd output is sent.</dl>
<h2>Description</h2>
<p>Simulate READ CAPACITY commands. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
