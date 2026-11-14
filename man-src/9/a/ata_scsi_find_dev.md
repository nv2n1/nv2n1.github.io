---
title: "ata_scsi_find_dev(9)"
name: "ata_scsi_find_dev"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_find_dev/"
description: "ata_scsi_find_dev – lookup ata_device from scsi_cmnd"
---

<p>ata_scsi_find_dev &#8211; lookup ata_device from scsi_cmnd</p>
<h2>Synopsis</h2>
<pre><code>struct ata_device *ata_scsi_find_dev(struct ata_port *ap, const struct scsi_device *scsidev);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port to which the device is attached</dl>
<p> <i>scsidev</i></p>
<dl>
<dd>SCSI device from which we derive the ATA device</dl>
<h2>Description</h2>
<p>Given various information provided in struct scsi_cmnd, map that onto an ATA bus, and using that mapping determine which ata_device is associated with the SCSI command to be sent. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Associated ATA device, or <code>NULL</code> if not found.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
