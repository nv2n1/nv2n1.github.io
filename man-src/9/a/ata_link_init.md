---
title: "ata_link_init(9)"
name: "ata_link_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_link_init/"
description: "ata_link_init – Initialize an ata_link structure"
---

<p>ata_link_init &#8211; Initialize an ata_link structure</p>
<h2>Synopsis</h2>
<pre><code>void ata_link_init(struct ata_port *ap, struct ata_link *link, int pmp);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port link is attached to</dl>
<p> <i>link</i></p>
<dl>
<dd>Link structure to initialize</dl>
<p> <i>pmp</i></p>
<dl>
<dd>Port multiplier port number</dl>
<h2>Description</h2>
<p>Initialize <i>link</i>. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
