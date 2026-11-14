---
title: "scsi_16_lba_len(9)"
name: "scsi_16_lba_len"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_16_lba_len/"
description: "scsi_16_lba_len – Get LBA and transfer length"
---

<p>scsi_16_lba_len &#8211; Get LBA and transfer length</p>
<h2>Synopsis</h2>
<pre><code>void scsi_16_lba_len(const u8 *cdb, u64 *plba, u32 *plen);</code></pre>
<h2>Arguments</h2>
<p><i>cdb</i></p>
<dl>
<dd>
<dd>SCSI command to translate</dl>
<p> <i>plba</i></p>
<dl>
<dd>the LBA</dl>
<p> <i>plen</i></p>
<dl>
<dd>the transfer length</dl>
<h2>Description</h2>
<p>Calculate LBA and transfer length for 16-byte commands.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
