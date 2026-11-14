---
title: "ata_scsi_hotplug(9)"
name: "ata_scsi_hotplug"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_hotplug/"
description: "ata_scsi_hotplug – SCSI part of hotplug"
---

<p>ata_scsi_hotplug &#8211; SCSI part of hotplug</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_hotplug(struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>work</i></p>
<dl>
<dd>
<dd>Pointer to ATA port to perform SCSI hotplug on</dl>
<h2>Description</h2>
<p>Perform SCSI part of hotplug. It&#8217;s executed from a separate workqueue after EH completes. This is necessary because SCSI hot plugging requires working EH and hot unplugging is synchronized with hot plugging with a mutex. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
