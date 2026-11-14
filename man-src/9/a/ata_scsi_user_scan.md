---
title: "ata_scsi_user_scan(9)"
name: "ata_scsi_user_scan"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_user_scan/"
description: "ata_scsi_user_scan – indication for user-initiated bus scan"
---

<p>ata_scsi_user_scan &#8211; indication for user-initiated bus scan</p>
<h2>Synopsis</h2>
<pre><code>int ata_scsi_user_scan(struct Scsi_Host *shost, unsigned int channel, unsigned int id, u64 lun);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>SCSI host to scan</dl>
<p> <i>channel</i></p>
<dl>
<dd>Channel to scan</dl>
<p> <i>id</i></p>
<dl>
<dd>ID to scan</dl>
<p> <i>lun</i></p>
<dl>
<dd>LUN to scan</dl>
<h2>Description</h2>
<p>This function is called when user explicitly requests bus scan. Set probe pending flag and invoke EH. </p>
<p> LOCKING: SCSI layer (we don&#8217;t care)</p>
<h2>Return</h2>
<p>Zero.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
