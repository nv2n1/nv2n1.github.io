---
title: "scsicam_bios_param(9)"
name: "scsicam_bios_param"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsicam_bios_param/"
description: "scsicam_bios_param – Determine geometry of a disk in cylinders/heads/sectors."
---

<p>scsicam_bios_param &#8211; Determine geometry of a disk in cylinders/heads/sectors.</p>
<h2>Synopsis</h2>
<pre><code>int scsicam_bios_param(struct block_device *bdev, sector_t capacity, int *ip);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>which device</dl>
<p> <i>capacity</i></p>
<dl>
<dd>size of the disk in sectors</dl>
<p> <i>ip</i></p>
<dl>
<dd>return value: ip[0]=heads, ip[1]=sectors, ip[2]=cylinders</dl>
<h2>Description</h2>
<p>determine the BIOS mapping/geometry used for a drive in a SCSI-CAM system, storing the results in ip as required by the HDIO_GETGEO <code>ioctl</code>.</p>
<h2>Return</h2>
<p>-1 on failure, 0 on success.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
