---
title: "ata_port_detach(9)"
name: "ata_port_detach"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_port_detach/"
description: "ata_port_detach – Detach ATA port in preparation of device removal"
---

<p>ata_port_detach &#8211; Detach ATA port in preparation of device removal</p>
<h2>Synopsis</h2>
<pre><code>void ata_port_detach(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port to be detached</dl>
<h2>Description</h2>
<p>Detach all ATA devices and the associated SCSI devices of <i>ap</i>; then, remove the associated SCSI host. <i>ap</i> is guaranteed to be quiescent on return from this function. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
