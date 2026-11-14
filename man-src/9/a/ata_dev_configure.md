---
title: "ata_dev_configure(9)"
name: "ata_dev_configure"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_configure/"
description: "ata_dev_configure – Configure the specified ATA/ATAPI device"
---

<p>ata_dev_configure &#8211; Configure the specified ATA/ATAPI device</p>
<h2>Synopsis</h2>
<pre><code>int ata_dev_configure(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Target device to configure</dl>
<h2>Description</h2>
<p>Configure <i>dev</i> according to <i>dev</i>-&gt;id. Generic and low-level driver specific fixups are also applied. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
