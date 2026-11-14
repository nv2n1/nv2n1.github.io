---
title: "ata_scsi_dump_cdb(9)"
name: "ata_scsi_dump_cdb"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_dump_cdb/"
description: "ata_scsi_dump_cdb – dump SCSI command contents to dmesg"
---

<p>ata_scsi_dump_cdb &#8211; dump SCSI command contents to dmesg</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_dump_cdb(struct ata_port *ap, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port to which the command was being sent</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command to dump</dl>
<h2>Description</h2>
<p>Prints the contents of a SCSI command via <code>printk</code>.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
