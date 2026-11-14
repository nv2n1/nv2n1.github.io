---
title: "ata_gen_ata_sense(9)"
name: "ata_gen_ata_sense"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_gen_ata_sense/"
description: "ata_gen_ata_sense – generate a SCSI fixed sense block"
---

<p>ata_gen_ata_sense &#8211; generate a SCSI fixed sense block</p>
<h2>Synopsis</h2>
<pre><code>void ata_gen_ata_sense(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>Command that we are erroring out</dl>
<h2>Description</h2>
<p>Generate sense block for a failed ATA command <i>qc</i>. Descriptor format is used to accommodate LBA48 block address. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
