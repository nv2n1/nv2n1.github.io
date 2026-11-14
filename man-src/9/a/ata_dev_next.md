---
title: "ata_dev_next(9)"
name: "ata_dev_next"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_next/"
description: "ata_dev_next – device iteration helper"
---

<p>ata_dev_next &#8211; device iteration helper</p>
<h2>Synopsis</h2>
<pre><code>struct ata_device *ata_dev_next(struct ata_device *dev, struct ata_link *link, enum ata_dev_iter_mode mode);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the previous device, NULL to start</dl>
<p> <i>link</i></p>
<dl>
<dd>ATA link containing devices to iterate</dl>
<p> <i>mode</i></p>
<dl>
<dd>iteration mode, one of ATA_DITER_*</dl>
<h2>Description</h2>
<p>LOCKING: Host lock or EH context.</p>
<h2>Return</h2>
<p>Pointer to the next device.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
