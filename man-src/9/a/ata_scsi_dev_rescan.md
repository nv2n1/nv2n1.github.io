---
title: "ata_scsi_dev_rescan(9)"
name: "ata_scsi_dev_rescan"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_dev_rescan/"
description: "ata_scsi_dev_rescan – initiate scsi_rescan_device"
---

<p>ata_scsi_dev_rescan &#8211; initiate <code>scsi_rescan_device</code></p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_dev_rescan(struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>work</i></p>
<dl>
<dd>
<dd>Pointer to ATA port to perform <code>scsi_rescan_device</code></dl>
<h2>Description</h2>
<p>After ATA pass thru (SAT) commands are executed successfully, libata need to propagate the changes to SCSI layer. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
