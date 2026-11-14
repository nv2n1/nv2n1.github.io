---
title: "ata_dump_id(9)"
name: "ata_dump_id"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dump_id/"
description: "ata_dump_id – IDENTIFY DEVICE info debugging output"
---

<p>ata_dump_id &#8211; IDENTIFY DEVICE info debugging output</p>
<h2>Synopsis</h2>
<pre><code>void ata_dump_id(const u16 *id);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>IDENTIFY DEVICE page to dump</dl>
<h2>Description</h2>
<p>Dump selected 16-bit words from the given IDENTIFY DEVICE page. </p>
<p> LOCKING: caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
