---
title: "ata_format_sct_write_same(9)"
name: "ata_format_sct_write_same"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_format_sct_write_same/"
description: "ata_format_sct_write_same – SATL Write Same to ATA SCT Write Same"
---

<p>ata_format_sct_write_same &#8211; SATL Write Same to ATA SCT Write Same</p>
<h2>Synopsis</h2>
<pre><code>size_t ata_format_sct_write_same(struct scsi_cmnd *cmd, u64 lba, u64 num);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>SCSI command being translated</dl>
<p> <i>lba</i></p>
<dl>
<dd>Starting sector</dl>
<p> <i>num</i></p>
<dl>
<dd>Number of sectors to be zero&#8217;d.</dl>
<h2>Description</h2>
<p>Rewrite the WRITE SAME payload to be an SCT Write Same formatted descriptor.</p>
<h2>Note</h2>
<p>Writes a pattern (0&#8217;s) in the foreground.</p>
<h2>Return</h2>
<p>Number of bytes copied into sglist.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
