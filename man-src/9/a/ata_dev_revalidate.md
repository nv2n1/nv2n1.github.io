---
title: "ata_dev_revalidate(9)"
name: "ata_dev_revalidate"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_revalidate/"
description: "ata_dev_revalidate – Revalidate ATA device"
---

<p>ata_dev_revalidate &#8211; Revalidate ATA device</p>
<h2>Synopsis</h2>
<pre><code>int ata_dev_revalidate(struct ata_device *dev, unsigned int new_class, unsigned int readid_flags);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to revalidate</dl>
<p> <i>new_class</i></p>
<dl>
<dd>new class code</dl>
<p> <i>readid_flags</i></p>
<dl>
<dd>read ID flags</dl>
<h2>Description</h2>
<p>Re-read IDENTIFY page, make sure <i>dev</i> is still attached to the port and reconfigure it according to the new IDENTIFY page. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, negative errno otherwise</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
