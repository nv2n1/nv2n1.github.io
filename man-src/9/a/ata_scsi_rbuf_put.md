---
title: "ata_scsi_rbuf_put(9)"
name: "ata_scsi_rbuf_put"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_rbuf_put/"
description: "ata_scsi_rbuf_put – Unmap response buffer."
---

<p>ata_scsi_rbuf_put &#8211; Unmap response buffer.</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_rbuf_put(struct scsi_cmnd *cmd, bool copy_out, unsigned long *flags);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>SCSI command containing buffer to be unmapped.</dl>
<p> <i>copy_out</i></p>
<dl>
<dd>copy out result</dl>
<p> <i>flags</i></p>
<dl>
<dd><i>flags</i> passed to <code>ata_scsi_rbuf_get</code></dl>
<h2>Description</h2>
<p>Returns rbuf buffer. The result is copied to <i>cmd</i>&#8216;s buffer if <i>copy_back</i> is true. </p>
<p> LOCKING: Unlocks ata_scsi_rbuf_lock.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
