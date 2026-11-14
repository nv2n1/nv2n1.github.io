---
title: "ata_dev_classify(9)"
name: "ata_dev_classify"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_classify/"
description: "ata_dev_classify – determine device type based on ATA-spec signature"
---

<p>ata_dev_classify &#8211; determine device type based on ATA-spec signature</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_dev_classify(const struct ata_taskfile *tf);</code></pre>
<h2>Arguments</h2>
<p><i>tf</i></p>
<dl>
<dd>
<dd>ATA taskfile register set for device to be identified</dl>
<h2>Description</h2>
<p>Determine from taskfile register contents whether a device is ATA or ATAPI, as per &#8220;Signature and persistence&#8221; section of ATA/PI spec (volume 1, sect 5.14). </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Device type, <code>ATA_DEV_ATA</code>, <code>ATA_DEV_ATAPI</code>, <code>ATA_DEV_PMP</code>, <code>ATA_DEV_ZAC</code>, or <code>ATA_DEV_UNKNOWN</code> the event of failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
