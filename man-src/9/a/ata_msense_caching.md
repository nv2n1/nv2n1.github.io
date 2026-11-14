---
title: "ata_msense_caching(9)"
name: "ata_msense_caching"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_msense_caching/"
description: "ata_msense_caching – Simulate MODE SENSE caching info page"
---

<p>ata_msense_caching &#8211; Simulate MODE SENSE caching info page</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_msense_caching(u16 *id, u8 *buf, bool changeable);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>device IDENTIFY data</dl>
<p> <i>buf</i></p>
<dl>
<dd>output buffer</dl>
<p> <i>changeable</i></p>
<dl>
<dd>whether changeable parameters are requested</dl>
<h2>Description</h2>
<p>Generate a caching info page, which conditionally indicates write caching to the SCSI layer, depending on device capabilities. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
