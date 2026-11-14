---
title: "nand_read(9)"
name: "nand_read"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read/"
description: "nand_read – [MTD Interface] MTD compatibility function for nand_do_read_ecc"
---

<p>nand_read &#8211; [MTD Interface] MTD compatibility function for nand_do_read_ecc</p>
<h2>Synopsis</h2>
<pre><code>int nand_read(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, uint8_t *buf);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>from</i></p>
<dl>
<dd>offset to read from</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to read</dl>
<p> <i>retlen</i></p>
<dl>
<dd>pointer to variable to store the number of read bytes</dl>
<p> <i>buf</i></p>
<dl>
<dd>the databuffer to put data</dl>
<h2>Description</h2>
<p>Get hold of the chip and call nand_do_read.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
