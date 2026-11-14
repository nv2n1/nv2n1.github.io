---
title: "ata_pio_mask_no_iordy(9)"
name: "ata_pio_mask_no_iordy"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_pio_mask_no_iordy/"
description: "ata_pio_mask_no_iordy – Return the non IORDY mask"
---

<p>ata_pio_mask_no_iordy &#8211; Return the non IORDY mask</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 ata_pio_mask_no_iordy(const struct ata_device&nbsp;<wbr>*&nbsp;<wbr></code><i>adev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>adev</i></p>
<dl>
<dd>
<dd>ATA device</dl>
<h2>Description</h2>
<p>Compute the highest mode possible if we are not using iordy. Return -1 if no iordy mode is available.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
