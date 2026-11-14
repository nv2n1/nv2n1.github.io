---
title: "nand_write_page_hwecc(9)"
name: "nand_write_page_hwecc"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_page_hwecc/"
description: "nand_write_page_hwecc – [REPLACEABLE] hardware ECC based page write function"
---

<p>nand_write_page_hwecc &#8211; [REPLACEABLE] hardware ECC based page write function</p>
<h2>Synopsis</h2>
<pre><code>int nand_write_page_hwecc(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>mtd info structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>nand chip info structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>data buffer</dl>
<p> <i>oob_required</i></p>
<dl>
<dd>must write chip-&gt;oob_poi to OOB</dl>
<p> <i>page</i></p>
<dl>
<dd>page number to write</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
