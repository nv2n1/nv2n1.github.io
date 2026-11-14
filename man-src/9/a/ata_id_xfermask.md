---
title: "ata_id_xfermask(9)"
name: "ata_id_xfermask"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_id_xfermask/"
description: "ata_id_xfermask – Compute xfermask from the given IDENTIFY data"
---

<p>ata_id_xfermask &#8211; Compute xfermask from the given IDENTIFY data</p>
<h2>Synopsis</h2>
<pre><code>unsigned long ata_id_xfermask(const u16 *id);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>IDENTIFY data to compute xfer mask from</dl>
<h2>Description</h2>
<p>Compute the xfermask for this device. This is not as trivial as it seems if we must consider early devices correctly. </p>
<p> FIXME: pre IDE drive timing (do we care ?). </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Computed xfermask</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
