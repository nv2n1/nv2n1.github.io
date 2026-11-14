---
title: "panic_nand_write(9)"
name: "panic_nand_write"
section: "9"
letter: "p"
url: "/docs/linux/man/9-panic_nand_write/"
description: "panic_nand_write – [MTD Interface] NAND write with ECC"
---

<p>panic_nand_write &#8211; [MTD Interface] NAND write with ECC</p>
<h2>Synopsis</h2>
<pre><code>int panic_nand_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const uint8_t *buf);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>to</i></p>
<dl>
<dd>offset to write to</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to write</dl>
<p> <i>retlen</i></p>
<dl>
<dd>pointer to variable to store the number of written bytes</dl>
<p> <i>buf</i></p>
<dl>
<dd>the data to write</dl>
<h2>Description</h2>
<p>NAND write with ECC. Used when performing writes in interrupt context, this may for example be called by mtdoops when writing an oops while in panic.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
