---
title: "ata_dev_set_xfermode(9)"
name: "ata_dev_set_xfermode"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_set_xfermode/"
description: "ata_dev_set_xfermode – Issue SET FEATURES – XFER MODE command"
---

<p>ata_dev_set_xfermode &#8211; Issue SET FEATURES &#8211; XFER MODE command</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_dev_set_xfermode(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to which command will be sent</dl>
<h2>Description</h2>
<p>Issue SET FEATURES &#8211; XFER MODE command to device <i>dev</i> on port <i>ap</i>. </p>
<p> LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>0 on success, AC_ERR_* mask otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
