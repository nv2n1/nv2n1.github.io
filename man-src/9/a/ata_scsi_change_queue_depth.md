---
title: "ata_scsi_change_queue_depth(9)"
name: "ata_scsi_change_queue_depth"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_change_queue_depth/"
description: "ata_scsi_change_queue_depth – SCSI callback for queue depth config"
---

<p>ata_scsi_change_queue_depth &#8211; SCSI callback for queue depth config</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_change_queue_depth(struct scsi_device *sdev, int queue_depth);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to configure queue depth for</dl>
<p> <i>queue_depth</i></p>
<dl>
<dd>new queue depth</dl>
<h2>Description</h2>
<p>This is libata standard hostt-&gt;change_queue_depth callback. SCSI will call into this callback when user tries to set queue depth via sysfs. </p>
<p> LOCKING: SCSI layer (we don&#8217;t care)</p>
<h2>Return</h2>
<p>Newly configured queue depth.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
