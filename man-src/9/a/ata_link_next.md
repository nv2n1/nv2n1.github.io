---
title: "ata_link_next(9)"
name: "ata_link_next"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_link_next/"
description: "ata_link_next – link iteration helper"
---

<p>ata_link_next &#8211; link iteration helper</p>
<h2>Synopsis</h2>
<pre><code>struct ata_link *ata_link_next(struct ata_link *link, struct ata_port *ap, enum ata_link_iter_mode mode);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>the previous link, NULL to start</dl>
<p> <i>ap</i></p>
<dl>
<dd>ATA port containing links to iterate</dl>
<p> <i>mode</i></p>
<dl>
<dd>iteration mode, one of ATA_LITER_*</dl>
<h2>Description</h2>
<p>LOCKING: Host lock or EH context.</p>
<h2>Return</h2>
<p>Pointer to the next link.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
