---
title: "ata_format_dsm_trim_descr(9)"
name: "ata_format_dsm_trim_descr"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_format_dsm_trim_descr/"
description: "ata_format_dsm_trim_descr – SATL Write Same to DSM Trim"
---

<p>ata_format_dsm_trim_descr &#8211; SATL Write Same to DSM Trim</p>
<h2>Synopsis</h2>
<pre><code>size_t ata_format_dsm_trim_descr(struct scsi_cmnd *cmd, u32 trmax, u64 sector, u32 count);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>SCSI command being translated</dl>
<p> <i>trmax</i></p>
<dl>
<dd>Maximum number of entries that will fit in sector_size bytes.</dl>
<p> <i>sector</i></p>
<dl>
<dd>Starting sector</dl>
<p> <i>count</i></p>
<dl>
<dd>Total Range of request in logical sectors</dl>
<h2>Description</h2>
<p>Rewrite the WRITE SAME descriptor to be a DSM TRIM little-endian formatted descriptor. </p>
<p> Upto 64 entries of the format: 63:48 Range Length 47:0 LBA </p>
<p> Range Length of 0 is ignored. LBA&#8217;s should be sorted order and not overlap.</p>
<h2>Note</h2>
<p>this is the same format as ADD LBA(S) TO NV CACHE PINNED SET</p>
<h2>Return</h2>
<p>Number of bytes copied into sglist.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
