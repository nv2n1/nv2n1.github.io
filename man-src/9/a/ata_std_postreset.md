---
title: "ata_std_postreset(9)"
name: "ata_std_postreset"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_std_postreset/"
description: "ata_std_postreset – standard postreset callback"
---

<p>ata_std_postreset &#8211; standard postreset callback</p>
<h2>Synopsis</h2>
<pre><code>void ata_std_postreset(struct ata_link *link, unsigned int *classes);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>the target ata_link</dl>
<p> <i>classes</i></p>
<dl>
<dd>classes of attached devices</dl>
<h2>Description</h2>
<p>This function is invoked after a successful reset. Note that the device might have been reset more than once using different reset methods before postreset is invoked. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
