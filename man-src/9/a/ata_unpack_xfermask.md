---
title: "ata_unpack_xfermask(9)"
name: "ata_unpack_xfermask"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_unpack_xfermask/"
description: "ata_unpack_xfermask – Unpack xfer_mask into pio, mwdma and udma masks"
---

<p>ata_unpack_xfermask &#8211; Unpack xfer_mask into pio, mwdma and udma masks</p>
<h2>Synopsis</h2>
<pre><code>void ata_unpack_xfermask(unsigned long xfer_mask, unsigned long *pio_mask, unsigned long *mwdma_mask, unsigned long *udma_mask);</code></pre>
<h2>Arguments</h2>
<p><i>xfer_mask</i></p>
<dl>
<dd>
<dd>xfer_mask to unpack</dl>
<p> <i>pio_mask</i></p>
<dl>
<dd>resulting pio_mask</dl>
<p> <i>mwdma_mask</i></p>
<dl>
<dd>resulting mwdma_mask</dl>
<p> <i>udma_mask</i></p>
<dl>
<dd>resulting udma_mask</dl>
<h2>Description</h2>
<p>Unpack <i>xfer_mask</i> into <i>pio_mask</i>, <i>mwdma_mask</i> and <i>udma_mask</i>. Any NULL destination masks will be ignored.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
