---
title: "ata_xfer_mode2mask(9)"
name: "ata_xfer_mode2mask"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_xfer_mode2mask/"
description: "ata_xfer_mode2mask – Find matching xfer_mask for XFER_*"
---

<p>ata_xfer_mode2mask &#8211; Find matching xfer_mask for XFER_*</p>
<h2>Synopsis</h2>
<pre><code>unsigned long ata_xfer_mode2mask(u8 xfer_mode);</code></pre>
<h2>Arguments</h2>
<p><i>xfer_mode</i></p>
<dl>
<dd>
<dd>XFER_* of interest</dl>
<h2>Description</h2>
<p>Return matching xfer_mask for <i>xfer_mode</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Matching xfer_mask, 0 if no match found.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
