---
title: "ata_force_cbl(9)"
name: "ata_force_cbl"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_force_cbl/"
description: "ata_force_cbl – force cable type according to libata.force"
---

<p>ata_force_cbl &#8211; force cable type according to libata.force</p>
<h2>Synopsis</h2>
<pre><code>void ata_force_cbl(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port of interest</dl>
<h2>Description</h2>
<p>Force cable type according to libata.force and whine about it. The last entry which has matching port number is used, so it can be specified as part of device force parameters. For example, both &#8220;a:40c,1.00:udma4&#8221; and &#8220;1.00:40c,udma4&#8221; have the same effect. </p>
<p> LOCKING: EH context.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
