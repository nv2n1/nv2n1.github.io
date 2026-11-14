---
title: "ata_hpa_resize(9)"
name: "ata_hpa_resize"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_hpa_resize/"
description: "ata_hpa_resize – Resize a device with an HPA set"
---

<p>ata_hpa_resize &#8211; Resize a device with an HPA set</p>
<h2>Synopsis</h2>
<pre><code>int ata_hpa_resize(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to resize</dl>
<h2>Description</h2>
<p>Read the size of an LBA28 or LBA48 disk with HPA features and resize it if required to the full size of the media. The caller must check the drive has the HPA feature set enabled.</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
