---
title: "ata_xfer_mode2shift(9)"
name: "ata_xfer_mode2shift"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_xfer_mode2shift/"
description: "ata_xfer_mode2shift – Find matching xfer_shift for XFER_*"
---

<p>ata_xfer_mode2shift &#8211; Find matching xfer_shift for XFER_*</p>
<h2>Synopsis</h2>
<pre><code>int ata_xfer_mode2shift(unsigned long xfer_mode);</code></pre>
<h2>Arguments</h2>
<p><i>xfer_mode</i></p>
<dl>
<dd>
<dd>XFER_* of interest</dl>
<h2>Description</h2>
<p>Return matching xfer_shift for <i>xfer_mode</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Matching xfer_shift, -1 if no match found.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
