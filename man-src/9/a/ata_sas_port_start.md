---
title: "ata_sas_port_start(9)"
name: "ata_sas_port_start"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_port_start/"
description: "ata_sas_port_start – Set port up for dma."
---

<p>ata_sas_port_start &#8211; Set port up for dma.</p>
<h2>Synopsis</h2>
<pre><code>int ata_sas_port_start(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port to initialize</dl>
<h2>Description</h2>
<p>Called just after data structures for each port are initialized. </p>
<p> May be used as the <code>port_start</code> entry in ata_port_operations. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
