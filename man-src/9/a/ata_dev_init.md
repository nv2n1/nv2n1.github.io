---
title: "ata_dev_init(9)"
name: "ata_dev_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_init/"
description: "ata_dev_init – Initialize an ata_device structure"
---

<p>ata_dev_init &#8211; Initialize an ata_device structure</p>
<h2>Synopsis</h2>
<pre><code>void ata_dev_init(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device structure to initialize</dl>
<h2>Description</h2>
<p>Initialize <i>dev</i> in preparation for probing. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
