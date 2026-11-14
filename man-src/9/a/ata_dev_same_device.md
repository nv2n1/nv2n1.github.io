---
title: "ata_dev_same_device(9)"
name: "ata_dev_same_device"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_same_device/"
description: "ata_dev_same_device – Determine whether new ID matches configured device"
---

<p>ata_dev_same_device &#8211; Determine whether new ID matches configured device</p>
<h2>Synopsis</h2>
<pre><code>int ata_dev_same_device(struct ata_device *dev, unsigned int new_class, const u16 *new_id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to compare against</dl>
<p> <i>new_class</i></p>
<dl>
<dd>class of the new device</dl>
<p> <i>new_id</i></p>
<dl>
<dd>IDENTIFY page of the new device</dl>
<h2>Description</h2>
<p>Compare <i>new_class</i> and <i>new_id</i> against <i>dev</i> and determine whether <i>dev</i> is the device indicated by <i>new_class</i> and <i>new_id</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>1 if <i>dev</i> matches <i>new_class</i> and <i>new_id</i>, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
