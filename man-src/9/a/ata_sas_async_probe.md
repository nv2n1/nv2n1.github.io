---
title: "ata_sas_async_probe(9)"
name: "ata_sas_async_probe"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_async_probe/"
description: "ata_sas_async_probe – simply schedule probing and return"
---

<p>ata_sas_async_probe &#8211; simply schedule probing and return</p>
<h2>Synopsis</h2>
<pre><code>void ata_sas_async_probe(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port to probe</dl>
<h2>Description</h2>
<p>For batch scheduling of probe for sas attached ata devices, assumes the port has already been through <code>ata_sas_port_init</code></p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
