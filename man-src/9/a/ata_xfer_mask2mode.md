---
title: "ata_xfer_mask2mode(9)"
name: "ata_xfer_mask2mode"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_xfer_mask2mode/"
description: "ata_xfer_mask2mode – Find matching XFER_* for the given xfer_mask"
---

<p>ata_xfer_mask2mode &#8211; Find matching XFER_* for the given xfer_mask</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 ata_xfer_mask2mode(unsigned long&nbsp;<wbr></code><i>xfer_mask</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>xfer_mask</i></p>
<dl>
<dd>
<dd>xfer_mask of interest</dl>
<h2>Description</h2>
<p>Return matching XFER_* value for <i>xfer_mask</i>. Only the highest bit of <i>xfer_mask</i> is considered. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Matching XFER_* value, 0xff if no match found.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
