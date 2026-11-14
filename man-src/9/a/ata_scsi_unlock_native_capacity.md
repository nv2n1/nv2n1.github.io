---
title: "ata_scsi_unlock_native_capacity(9)"
name: "ata_scsi_unlock_native_capacity"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_unlock_native_capacity/"
description: "ata_scsi_unlock_native_capacity – unlock native capacity"
---

<p>ata_scsi_unlock_native_capacity &#8211; unlock native capacity</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_unlock_native_capacity(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to adjust device capacity for</dl>
<h2>Description</h2>
<p>This function is called if a partition on <i>sdev</i> extends beyond the end of the device. It requests EH to unlock HPA. </p>
<p> LOCKING: Defined by the SCSI layer. Might sleep.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
