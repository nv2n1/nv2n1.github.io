---
title: "ata_do_dev_read_id(9)"
name: "ata_do_dev_read_id"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_do_dev_read_id/"
description: "ata_do_dev_read_id – default ID read method"
---

<p>ata_do_dev_read_id &#8211; default ID read method</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_do_dev_read_id(struct ata_device *dev, struct ata_taskfile *tf, u16 *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device</dl>
<p> <i>tf</i></p>
<dl>
<dd>proposed taskfile</dl>
<p> <i>id</i></p>
<dl>
<dd>data buffer</dl>
<h2>Description</h2>
<p>Issue the identify taskfile and hand back the buffer containing identify data. For some RAID controllers and for pre ATA devices this function is wrapped or replaced by the driver</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
