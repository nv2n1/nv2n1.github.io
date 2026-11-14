---
title: "piix_pata_prereset(9)"
name: "piix_pata_prereset"
section: "9"
letter: "p"
url: "/docs/linux/man/9-piix_pata_prereset/"
description: "piix_pata_prereset – prereset for PATA host controller"
---

<p>piix_pata_prereset &#8211; prereset for PATA host controller</p>
<h2>Synopsis</h2>
<pre><code>int piix_pata_prereset(struct ata_link *link, unsigned long deadline);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Target link</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<h2>Description</h2>
<p>LOCKING: None (inherited from caller).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
