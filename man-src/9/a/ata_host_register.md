---
title: "ata_host_register(9)"
name: "ata_host_register"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_register/"
description: "ata_host_register – register initialized ATA host"
---

<p>ata_host_register &#8211; register initialized ATA host</p>
<h2>Synopsis</h2>
<pre><code>int ata_host_register(struct ata_host *host, struct scsi_host_template *sht);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>ATA host to register</dl>
<p> <i>sht</i></p>
<dl>
<dd>template for SCSI host</dl>
<h2>Description</h2>
<p>Register initialized ATA host. <i>host</i> is allocated using <code>ata_host_alloc</code> and fully initialized by LLD. This function starts ports, registers <i>host</i> with ATA and SCSI layers and probe registered devices. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
