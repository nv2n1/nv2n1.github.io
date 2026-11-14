---
title: "ata_tf_from_fis(9)"
name: "ata_tf_from_fis"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_tf_from_fis/"
description: "ata_tf_from_fis – Convert SATA FIS to ATA taskfile"
---

<p>ata_tf_from_fis &#8211; Convert SATA FIS to ATA taskfile</p>
<h2>Synopsis</h2>
<pre><code>void ata_tf_from_fis(const u8 *fis, struct ata_taskfile *tf);</code></pre>
<h2>Arguments</h2>
<p><i>fis</i></p>
<dl>
<dd>
<dd>Buffer from which data will be input</dl>
<p> <i>tf</i></p>
<dl>
<dd>Taskfile to output</dl>
<h2>Description</h2>
<p>Converts a serial ATA FIS structure to a standard ATA taskfile. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
