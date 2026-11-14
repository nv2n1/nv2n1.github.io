---
title: "ata_scsi_slave_config(9)"
name: "ata_scsi_slave_config"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_slave_config/"
description: "ata_scsi_slave_config – Set SCSI device attributes"
---

<p>ata_scsi_slave_config &#8211; Set SCSI device attributes</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_slave_config(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to examine</dl>
<h2>Description</h2>
<p>This is called before we actually start reading and writing to the device, to configure certain SCSI mid-layer behaviors. </p>
<p> LOCKING: Defined by SCSI layer. We don&#8217;t really care.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
