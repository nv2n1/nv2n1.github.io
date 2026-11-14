---
title: "ata_force_horkage(9)"
name: "ata_force_horkage"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_force_horkage/"
description: "ata_force_horkage – force horkage according to libata.force"
---

<p>ata_force_horkage &#8211; force horkage according to libata.force</p>
<h2>Synopsis</h2>
<pre><code>void ata_force_horkage(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device of interest</dl>
<h2>Description</h2>
<p>Force horkage according to libata.force and whine about it. For consistency with link selection, device number 15 selects the first device connected to the host link. </p>
<p> LOCKING: EH context.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
