---
title: "scan_read_oob(9)"
name: "scan_read_oob"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scan_read_oob/"
description: "scan_read_oob – [GENERIC] Scan data+OOB region to buffer"
---

<p>scan_read_oob &#8211; [GENERIC] Scan data+OOB region to buffer</p>
<h2>Synopsis</h2>
<pre><code>int scan_read_oob(struct mtd_info *mtd, uint8_t *buf, loff_t offs, size_t len);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>temporary buffer</dl>
<p> <i>offs</i></p>
<dl>
<dd>offset at which to scan</dl>
<p> <i>len</i></p>
<dl>
<dd>length of data region to read</dl>
<h2>Description</h2>
<p>Scan read data from data+OOB. May traverse multiple pages, interleaving page,OOB,page,OOB,&#8230; in buf. Completes transfer and returns the &#8220;strongest&#8221; ECC condition (error or bitflip). May quit on the first (non-ECC) error.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
