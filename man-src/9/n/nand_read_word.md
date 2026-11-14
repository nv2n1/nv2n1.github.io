---
title: "nand_read_word(9)"
name: "nand_read_word"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_word/"
description: "nand_read_word – [DEFAULT] read one word from the chip"
---

<p>nand_read_word &#8211; [DEFAULT] read one word from the chip</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 nand_read_word(struct mtd_info&nbsp;<wbr>*&nbsp;<wbr></code><i>mtd</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>Default read function for 16bit buswidth without endianness conversion.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
