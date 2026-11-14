---
title: "ata_scsi_offline_dev(9)"
name: "ata_scsi_offline_dev"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_offline_dev/"
description: "ata_scsi_offline_dev – offline attached SCSI device"
---

<p>ata_scsi_offline_dev &#8211; offline attached SCSI device</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_offline_dev(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device to offline attached SCSI device for</dl>
<h2>Description</h2>
<p>This function is called from <code>ata_eh_hotplug</code> and responsible for taking the SCSI device attached to <i>dev</i> offline. This function is called with host lock which protects dev-&gt;sdev against clearing. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>1 if attached SCSI device exists, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
