---
title: "ata_cmd_ioctl(9)"
name: "ata_cmd_ioctl"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_cmd_ioctl/"
description: "ata_cmd_ioctl – Handler for HDIO_DRIVE_CMD ioctl"
---

<p>ata_cmd_ioctl &#8211; Handler for HDIO_DRIVE_CMD ioctl</p>
<h2>Synopsis</h2>
<pre><code>int ata_cmd_ioctl(struct scsi_device *scsidev, void __user *arg);</code></pre>
<h2>Arguments</h2>
<p><i>scsidev</i></p>
<dl>
<dd>
<dd>Device to which we are issuing command</dl>
<p> <i>arg</i></p>
<dl>
<dd>User provided data for issuing command</dl>
<h2>Description</h2>
<p>LOCKING: Defined by the SCSI layer. We don&#8217;t really care.</p>
<h2>Return</h2>
<p>Zero on success, negative errno on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
