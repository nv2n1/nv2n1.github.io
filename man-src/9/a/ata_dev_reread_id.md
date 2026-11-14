---
title: "ata_dev_reread_id(9)"
name: "ata_dev_reread_id"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_reread_id/"
description: "ata_dev_reread_id – Re-read IDENTIFY data"
---

<p>ata_dev_reread_id &#8211; Re-read IDENTIFY data</p>
<h2>Synopsis</h2>
<pre><code>int ata_dev_reread_id(struct ata_device *dev, unsigned int readid_flags);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>target ATA device</dl>
<p> <i>readid_flags</i></p>
<dl>
<dd>read ID flags</dl>
<h2>Description</h2>
<p>Re-read IDENTIFY page and make sure <i>dev</i> is still attached to the port. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, negative errno otherwise</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
