---
title: "sata_link_resume(9)"
name: "sata_link_resume"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_link_resume/"
description: "sata_link_resume – resume SATA link"
---

<p>sata_link_resume &#8211; resume SATA link</p>
<h2>Synopsis</h2>
<pre><code>int sata_link_resume(struct ata_link *link, const unsigned long *params, unsigned long deadline);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to resume SATA</dl>
<p> <i>params</i></p>
<dl>
<dd>timing parameters { interval, duration, timeout } in msec</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<h2>Description</h2>
<p>Resume SATA phy <i>link</i> and debounce it. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
