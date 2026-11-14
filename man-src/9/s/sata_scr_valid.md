---
title: "sata_scr_valid(9)"
name: "sata_scr_valid"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_scr_valid/"
description: "sata_scr_valid – test whether SCRs are accessible"
---

<p>sata_scr_valid &#8211; test whether SCRs are accessible</p>
<h2>Synopsis</h2>
<pre><code>int sata_scr_valid(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to test SCR accessibility for</dl>
<h2>Description</h2>
<p>Test whether SCRs are accessible for <i>link</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>1 if SCRs are accessible, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
