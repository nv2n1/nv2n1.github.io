---
title: "ata_to_sense_error(9)"
name: "ata_to_sense_error"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_to_sense_error/"
description: "ata_to_sense_error – convert ATA error to SCSI error"
---

<p>ata_to_sense_error &#8211; convert ATA error to SCSI error</p>
<h2>Synopsis</h2>
<pre><code>void ata_to_sense_error(unsigned id, u8 drv_stat, u8 drv_err, u8 *sk, u8 *asc, u8 *ascq, int verbose);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>ATA device number</dl>
<p> <i>drv_stat</i></p>
<dl>
<dd>value contained in ATA status register</dl>
<p> <i>drv_err</i></p>
<dl>
<dd>value contained in ATA error register</dl>
<p> <i>sk</i></p>
<dl>
<dd>the sense key we&#8217;ll fill out</dl>
<p> <i>asc</i></p>
<dl>
<dd>the additional sense code we&#8217;ll fill out</dl>
<p> <i>ascq</i></p>
<dl>
<dd>the additional sense code qualifier we&#8217;ll fill out</dl>
<p> <i>verbose</i></p>
<dl>
<dd>be verbose</dl>
<h2>Description</h2>
<p>Converts an ATA error into a SCSI error. Fill out pointers to SK, ASC, and ASCQ bytes for later use in fixed or descriptor format sense blocks. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
