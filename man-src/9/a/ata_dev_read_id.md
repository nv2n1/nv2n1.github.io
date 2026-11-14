---
title: "ata_dev_read_id(9)"
name: "ata_dev_read_id"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_read_id/"
description: "ata_dev_read_id – Read ID data from the specified device"
---

<p>ata_dev_read_id &#8211; Read ID data from the specified device</p>
<h2>Synopsis</h2>
<pre><code>int ata_dev_read_id(struct ata_device *dev, unsigned int *p_class, unsigned int flags, u16 *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>target device</dl>
<p> <i>p_class</i></p>
<dl>
<dd>pointer to class of the target device (may be changed)</dl>
<p> <i>flags</i></p>
<dl>
<dd>ATA_READID_* flags</dl>
<p> <i>id</i></p>
<dl>
<dd>buffer to read IDENTIFY data into</dl>
<h2>Description</h2>
<p>Read ID data from the specified device. ATA_CMD_ID_ATA is performed on ATA devices and ATA_CMD_ID_ATAPI on ATAPI devices. This function also issues ATA_CMD_INIT_DEV_PARAMS for pre-ATA4 drives. </p>
<p> FIXME: ATA_CMD_ID_ATA is optional for early drives and right now we abort if we hit that case. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
