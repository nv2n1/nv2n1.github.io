---
title: "ata_cable_ignore(9)"
name: "ata_cable_ignore"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_cable_ignore/"
description: "ata_cable_ignore – return ignored PATA cable."
---

<p>ata_cable_ignore &#8211; return ignored PATA cable.</p>
<h2>Synopsis</h2>
<pre><code>int ata_cable_ignore(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port</dl>
<h2>Description</h2>
<p>Helper method for drivers which don&#8217;t use cable type to limit transfer mode.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
