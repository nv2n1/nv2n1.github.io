---
title: "ata_sas_port_init(9)"
name: "ata_sas_port_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_port_init/"
description: "ata_sas_port_init – Initialize a SATA device"
---

<p>ata_sas_port_init &#8211; Initialize a SATA device</p>
<h2>Synopsis</h2>
<pre><code>int ata_sas_port_init(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>SATA port to initialize</dl>
<h2>Description</h2>
<p>LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>Zero on success, non-zero on error.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
