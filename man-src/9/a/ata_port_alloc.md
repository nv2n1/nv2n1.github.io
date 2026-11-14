---
title: "ata_port_alloc(9)"
name: "ata_port_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_port_alloc/"
description: "ata_port_alloc – allocate and initialize basic ATA port resources"
---

<p>ata_port_alloc &#8211; allocate and initialize basic ATA port resources</p>
<h2>Synopsis</h2>
<pre><code>struct ata_port *ata_port_alloc(struct ata_host *host);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>ATA host this allocated port belongs to</dl>
<h2>Description</h2>
<p>Allocate and initialize basic ATA port resources.</p>
<h2>Return</h2>
<p>Allocate ATA port on success, NULL on failure. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
