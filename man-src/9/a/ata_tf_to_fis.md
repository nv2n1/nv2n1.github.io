---
title: "ata_tf_to_fis(9)"
name: "ata_tf_to_fis"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_tf_to_fis/"
description: "ata_tf_to_fis – Convert ATA taskfile to SATA FIS structure"
---

<p>ata_tf_to_fis &#8211; Convert ATA taskfile to SATA FIS structure</p>
<h2>Synopsis</h2>
<pre><code>void ata_tf_to_fis(const struct ata_taskfile *tf, u8 pmp, int is_cmd, u8 *fis);</code></pre>
<h2>Arguments</h2>
<p><i>tf</i></p>
<dl>
<dd>
<dd>Taskfile to convert</dl>
<p> <i>pmp</i></p>
<dl>
<dd>Port multiplier port</dl>
<p> <i>is_cmd</i></p>
<dl>
<dd>This FIS is for command</dl>
<p> <i>fis</i></p>
<dl>
<dd>Buffer into which data will output</dl>
<h2>Description</h2>
<p>Converts a standard ATA taskfile to a Serial ATA FIS structure (Register &#8211; Host to Device). </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
