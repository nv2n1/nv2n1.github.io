---
title: "ata_qc_new_init(9)"
name: "ata_qc_new_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_qc_new_init/"
description: "ata_qc_new_init – Request an available ATA command, and initialize it"
---

<p>ata_qc_new_init &#8211; Request an available ATA command, and initialize it</p>
<h2>Synopsis</h2>
<pre><code>struct ata_queued_cmd *ata_qc_new_init(struct ata_device *dev, int tag);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device from whom we request an available command structure</dl>
<p> <i>tag</i></p>
<dl>
<dd>tag</dl>
<h2>Description</h2>
<p>LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
