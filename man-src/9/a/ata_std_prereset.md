---
title: "ata_std_prereset(9)"
name: "ata_std_prereset"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_std_prereset/"
description: "ata_std_prereset – prepare for reset"
---

<p>ata_std_prereset &#8211; prepare for reset</p>
<h2>Synopsis</h2>
<pre><code>int ata_std_prereset(struct ata_link *link, unsigned long deadline);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to be reset</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<h2>Description</h2>
<p><i>link</i> is about to be reset. Initialize it. Failure from prereset makes libata abort whole reset sequence and give up that port, so prereset should be best-effort. It does its best to prepare for reset sequence but if things go wrong, it should just whine, not fail. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
