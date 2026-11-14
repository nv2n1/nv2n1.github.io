---
title: "ata_scsi_media_change_notify(9)"
name: "ata_scsi_media_change_notify"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_media_change_notify/"
description: "ata_scsi_media_change_notify – send media change event"
---

<p>ata_scsi_media_change_notify &#8211; send media change event</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_media_change_notify(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Pointer to the disk device with media change event</dl>
<h2>Description</h2>
<p>Tell the block layer to send a media change notification event. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
