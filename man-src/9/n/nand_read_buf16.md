---
title: "nand_read_buf16(9)"
name: "nand_read_buf16"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_buf16/"
description: "nand_read_buf16 – [DEFAULT] read chip data into buffer"
---

<p>nand_read_buf16 &#8211; [DEFAULT] read chip data into buffer</p>
<h2>Synopsis</h2>
<pre><code>void nand_read_buf16(struct mtd_info *mtd, uint8_t *buf, int len);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>buffer to store date</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to read</dl>
<h2>Description</h2>
<p>Default read function for 16bit buswidth.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
