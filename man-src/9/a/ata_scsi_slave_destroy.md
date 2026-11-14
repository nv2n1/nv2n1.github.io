---
title: "ata_scsi_slave_destroy(9)"
name: "ata_scsi_slave_destroy"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_slave_destroy/"
description: "ata_scsi_slave_destroy – SCSI device is about to be destroyed"
---

<p>ata_scsi_slave_destroy &#8211; SCSI device is about to be destroyed</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_slave_destroy(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to be destroyed</dl>
<h2>Description</h2>
<p><i>sdev</i> is about to be destroyed for hot/warm unplugging. If this unplugging was initiated by libata as indicated by NULL dev-&gt;sdev, this function doesn&#8217;t have to do anything. Otherwise, SCSI layer initiated warm-unplug is in progress. Clear dev-&gt;sdev, schedule the device for ATA detach and invoke EH. </p>
<p> LOCKING: Defined by SCSI layer. We don&#8217;t really care.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
