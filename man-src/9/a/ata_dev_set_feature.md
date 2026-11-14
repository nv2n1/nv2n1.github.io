---
title: "ata_dev_set_feature(9)"
name: "ata_dev_set_feature"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_set_feature/"
description: "ata_dev_set_feature – Issue SET FEATURES – SATA FEATURES"
---

<p>ata_dev_set_feature &#8211; Issue SET FEATURES &#8211; SATA FEATURES</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_dev_set_feature(struct ata_device *dev, u8 enable, u8 feature);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to which command will be sent</dl>
<p> <i>enable</i></p>
<dl>
<dd>Whether to enable or disable the feature</dl>
<p> <i>feature</i></p>
<dl>
<dd>The sector count represents the feature to set</dl>
<h2>Description</h2>
<p>Issue SET FEATURES &#8211; SATA FEATURES command to device <i>dev</i> on port <i>ap</i> with sector count </p>
<p> LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>0 on success, AC_ERR_* mask otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
