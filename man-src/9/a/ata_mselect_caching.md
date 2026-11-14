---
title: "ata_mselect_caching(9)"
name: "ata_mselect_caching"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_mselect_caching/"
description: "ata_mselect_caching – Simulate MODE SELECT for caching info page"
---

<p>ata_mselect_caching &#8211; Simulate MODE SELECT for caching info page</p>
<h2>Synopsis</h2>
<pre><code>int ata_mselect_caching(struct ata_queued_cmd *qc, const u8 *buf, int len, u16 *fp);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Storage for translated ATA taskfile</dl>
<p> <i>buf</i></p>
<dl>
<dd>input buffer</dl>
<p> <i>len</i></p>
<dl>
<dd>number of valid bytes in the input buffer</dl>
<p> <i>fp</i></p>
<dl>
<dd>out parameter for the failed field on error</dl>
<h2>Description</h2>
<p>Prepare a taskfile to modify caching information for the device. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
