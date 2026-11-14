---
title: "nand_write_byte16(9)"
name: "nand_write_byte16"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_byte16/"
description: "nand_write_byte16 – [DEFAULT] write single byte to a chip with width 16"
---

<p>nand_write_byte16 &#8211; [DEFAULT] write single byte to a chip with width 16</p>
<h2>Synopsis</h2>
<pre><code>void nand_write_byte16(struct mtd_info *mtd, uint8_t byte);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>byte</i></p>
<dl>
<dd>value to write</dl>
<h2>Description</h2>
<p>Default function to write a byte to I/O[7:0] on a 16-bit wide chip.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
