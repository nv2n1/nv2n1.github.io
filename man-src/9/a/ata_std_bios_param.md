---
title: "ata_std_bios_param(9)"
name: "ata_std_bios_param"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_std_bios_param/"
description: "ata_std_bios_param – generic bios head/sector/cylinder calculator used by sd."
---

<p>ata_std_bios_param &#8211; generic bios head/sector/cylinder calculator used by sd.</p>
<h2>Synopsis</h2>
<pre><code>int ata_std_bios_param(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int geom[]);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device for which BIOS geometry is to be determined</dl>
<p> <i>bdev</i></p>
<dl>
<dd>block device associated with <i>sdev</i></dl>
<p> <i>capacity</i></p>
<dl>
<dd>capacity of SCSI device</dl>
<p> <i>geom[]</i></p>
<dl>
<dd>location to which geometry will be output</dl>
<h2>Description</h2>
<p>Generic bios head/sector/cylinder calculator used by sd. Most BIOSes nowadays expect a XXX/255/16 (CHS) mapping. Some situations may arise where the disk is not bootable if this is not used. </p>
<p> LOCKING: Defined by the SCSI layer. We don&#8217;t really care.</p>
<h2>Return</h2>
<p>Zero.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
