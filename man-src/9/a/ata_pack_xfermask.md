---
title: "ata_pack_xfermask(9)"
name: "ata_pack_xfermask"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_pack_xfermask/"
description: "ata_pack_xfermask – Pack pio, mwdma and udma masks into xfer_mask"
---

<p>ata_pack_xfermask &#8211; Pack pio, mwdma and udma masks into xfer_mask</p>
<h2>Synopsis</h2>
<pre><code>unsigned long ata_pack_xfermask(unsigned long pio_mask, unsigned long mwdma_mask, unsigned long udma_mask);</code></pre>
<h2>Arguments</h2>
<p><i>pio_mask</i></p>
<dl>
<dd>
<dd>pio_mask</dl>
<p> <i>mwdma_mask</i></p>
<dl>
<dd>mwdma_mask</dl>
<p> <i>udma_mask</i></p>
<dl>
<dd>udma_mask</dl>
<h2>Description</h2>
<p>Pack <i>pio_mask</i>, <i>mwdma_mask</i> and <i>udma_mask</i> into a single unsigned int xfer_mask. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Packed xfer_mask.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
