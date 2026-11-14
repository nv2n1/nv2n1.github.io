---
title: "ata_sas_slave_configure(9)"
name: "ata_sas_slave_configure"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_slave_configure/"
description: "ata_sas_slave_configure – Default slave_config routine for libata devices"
---

<p>ata_sas_slave_configure &#8211; Default slave_config routine for libata devices</p>
<h2>Synopsis</h2>
<pre><code>int ata_sas_slave_configure(struct scsi_device *sdev, struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to configure</dl>
<p> <i>ap</i></p>
<dl>
<dd>ATA port to which SCSI device is attached</dl>
<h2>Return</h2>
<p>Zero.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
