---
title: "ata_set_max_sectors(9)"
name: "ata_set_max_sectors"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_set_max_sectors/"
description: "ata_set_max_sectors – Set max sectors"
---

<p>ata_set_max_sectors &#8211; Set max sectors</p>
<h2>Synopsis</h2>
<pre><code>int ata_set_max_sectors(struct ata_device *dev, u64 new_sectors);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>target device</dl>
<p> <i>new_sectors</i></p>
<dl>
<dd>new max sectors value to set for the device</dl>
<h2>Description</h2>
<p>Set max sectors of <i>dev</i> to <i>new_sectors</i>.</p>
<h2>Return</h2>
<p>0 on success, -EACCES if command is aborted or denied (due to previous non-volatile SET_MAX) by the drive. -EIO on other errors.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
