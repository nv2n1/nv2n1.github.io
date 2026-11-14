---
title: "ata_pio_need_iordy(9)"
name: "ata_pio_need_iordy"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_pio_need_iordy/"
description: "ata_pio_need_iordy – check if iordy needed"
---

<p>ata_pio_need_iordy &#8211; check if iordy needed</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_pio_need_iordy(const struct ata_device *adev);</code></pre>
<h2>Arguments</h2>
<p><i>adev</i></p>
<dl>
<dd>
<dd>ATA device</dl>
<h2>Description</h2>
<p>Check if the current speed of the device requires IORDY. Used by various controllers for chip configuration.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
