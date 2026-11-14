---
title: "ata_cable_40wire(9)"
name: "ata_cable_40wire"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_cable_40wire/"
description: "ata_cable_40wire – return 40 wire cable type"
---

<p>ata_cable_40wire &#8211; return 40 wire cable type</p>
<h2>Synopsis</h2>
<pre><code>int ata_cable_40wire(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port</dl>
<h2>Description</h2>
<p>Helper method for drivers which want to hardwire 40 wire cable detection.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
