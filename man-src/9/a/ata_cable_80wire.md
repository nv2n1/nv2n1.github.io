---
title: "ata_cable_80wire(9)"
name: "ata_cable_80wire"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_cable_80wire/"
description: "ata_cable_80wire – return 80 wire cable type"
---

<p>ata_cable_80wire &#8211; return 80 wire cable type</p>
<h2>Synopsis</h2>
<pre><code>int ata_cable_80wire(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port</dl>
<h2>Description</h2>
<p>Helper method for drivers which want to hardwire 80 wire cable detection.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
