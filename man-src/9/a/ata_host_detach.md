---
title: "ata_host_detach(9)"
name: "ata_host_detach"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_detach/"
description: "ata_host_detach – Detach all ports of an ATA host"
---

<p>ata_host_detach &#8211; Detach all ports of an ATA host</p>
<h2>Synopsis</h2>
<pre><code>void ata_host_detach(struct ata_host *host);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>Host to detach</dl>
<h2>Description</h2>
<p>Detach all ports of <i>host</i>. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
