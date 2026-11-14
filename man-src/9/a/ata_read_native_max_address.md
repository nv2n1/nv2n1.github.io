---
title: "ata_read_native_max_address(9)"
name: "ata_read_native_max_address"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_read_native_max_address/"
description: "ata_read_native_max_address – Read native max address"
---

<p>ata_read_native_max_address &#8211; Read native max address</p>
<h2>Synopsis</h2>
<pre><code>int ata_read_native_max_address(struct ata_device *dev, u64 *max_sectors);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>target device</dl>
<p> <i>max_sectors</i></p>
<dl>
<dd>out parameter for the result native max address</dl>
<h2>Description</h2>
<p>Perform an LBA48 or LBA28 native size query upon the device in question.</p>
<h2>Return</h2>
<p>0 on success, -EACCES if command is aborted by the drive. -EIO on other errors.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
