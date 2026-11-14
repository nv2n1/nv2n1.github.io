---
title: "ata_get_identity(9)"
name: "ata_get_identity"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_get_identity/"
description: "ata_get_identity – Handler for HDIO_GET_IDENTITY ioctl"
---

<p>ata_get_identity &#8211; Handler for HDIO_GET_IDENTITY ioctl</p>
<h2>Synopsis</h2>
<pre><code>int ata_get_identity(struct ata_port *ap, struct scsi_device *sdev, void __user *arg);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>target port</dl>
<p> <i>sdev</i></p>
<dl>
<dd>SCSI device to get identify data for</dl>
<p> <i>arg</i></p>
<dl>
<dd>User buffer area for identify data</dl>
<h2>Description</h2>
<p>LOCKING: Defined by the SCSI layer. We don&#8217;t really care.</p>
<h2>Return</h2>
<p>Zero on success, negative errno on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
