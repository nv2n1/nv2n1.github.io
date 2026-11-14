---
title: "ata_scsi_rbuf_get(9)"
name: "ata_scsi_rbuf_get"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_rbuf_get/"
description: "ata_scsi_rbuf_get – Map response buffer."
---

<p>ata_scsi_rbuf_get &#8211; Map response buffer.</p>
<h2>Synopsis</h2>
<pre><code>void *ata_scsi_rbuf_get(struct scsi_cmnd *cmd, bool copy_in, unsigned long *flags);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>SCSI command containing buffer to be mapped.</dl>
<p> <i>copy_in</i></p>
<dl>
<dd>copy in from user buffer</dl>
<p> <i>flags</i></p>
<dl>
<dd>unsigned long variable to store irq enable status</dl>
<h2>Description</h2>
<p>Prepare buffer for simulated SCSI commands. </p>
<p> LOCKING: spin_lock_irqsave(ata_scsi_rbuf_lock) on success</p>
<h2>Return</h2>
<p>Pointer to response buffer.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
