---
title: "sata_std_hardreset(9)"
name: "sata_std_hardreset"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_std_hardreset/"
description: "sata_std_hardreset – COMRESET w/o waiting or classification"
---

<p>sata_std_hardreset &#8211; COMRESET w/o waiting or classification</p>
<h2>Synopsis</h2>
<pre><code>int sata_std_hardreset(struct ata_link *link, unsigned int *class, unsigned long deadline);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>link to reset</dl>
<p> <i>class</i></p>
<dl>
<dd>resulting class of attached device</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<h2>Description</h2>
<p>Standard SATA COMRESET w/o waiting or classification. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 if link offline, -EAGAIN if link online, -errno on errors.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
