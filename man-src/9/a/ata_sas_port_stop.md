---
title: "ata_sas_port_stop(9)"
name: "ata_sas_port_stop"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_port_stop/"
description: "ata_sas_port_stop – Undo ata_sas_port_start"
---

<p>ata_sas_port_stop &#8211; Undo <code>ata_sas_port_start</code></p>
<h2>Synopsis</h2>
<pre><code>void ata_sas_port_stop(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port to shut down</dl>
<h2>Description</h2>
<p>May be used as the <code>port_stop</code> entry in ata_port_operations. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
