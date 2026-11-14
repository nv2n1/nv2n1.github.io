---
title: "ata_msense_control(9)"
name: "ata_msense_control"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_msense_control/"
description: "ata_msense_control – Simulate MODE SENSE control mode page"
---

<p>ata_msense_control &#8211; Simulate MODE SENSE control mode page</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_msense_control(struct ata_device *dev, u8 *buf, bool changeable);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device of interest</dl>
<p> <i>buf</i></p>
<dl>
<dd>output buffer</dl>
<p> <i>changeable</i></p>
<dl>
<dd>whether changeable parameters are requested</dl>
<h2>Description</h2>
<p>Generate a generic MODE SENSE control mode page. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
