---
title: "nand_read_subpage(9)"
name: "nand_read_subpage"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_subpage/"
description: "nand_read_subpage – [REPLACEABLE] ECC based sub-page read function"
---

<p>nand_read_subpage &#8211; [REPLACEABLE] ECC based sub-page read function</p>
<h2>Synopsis</h2>
<pre><code>int nand_read_subpage(struct mtd_info *mtd, struct nand_chip *chip, uint32_t data_offs, uint32_t readlen, uint8_t *bufpoi, int page);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>mtd info structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>nand chip info structure</dl>
<p> <i>data_offs</i></p>
<dl>
<dd>offset of requested data within the page</dl>
<p> <i>readlen</i></p>
<dl>
<dd>data length</dl>
<p> <i>bufpoi</i></p>
<dl>
<dd>buffer to store read data</dl>
<p> <i>page</i></p>
<dl>
<dd>page number to read</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
