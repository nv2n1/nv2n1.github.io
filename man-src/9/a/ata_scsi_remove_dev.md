---
title: "ata_scsi_remove_dev(9)"
name: "ata_scsi_remove_dev"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_remove_dev/"
description: "ata_scsi_remove_dev – remove attached SCSI device"
---

<p>ata_scsi_remove_dev &#8211; remove attached SCSI device</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_remove_dev(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device to remove attached SCSI device for</dl>
<h2>Description</h2>
<p>This function is called from <code>ata_eh_scsi_hotplug</code> and responsible for removing the SCSI device attached to <i>dev</i>. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
