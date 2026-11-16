---
title: "read_bbt(9)"
name: "read_bbt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_bbt/"
description: "read_bbt – [GENERIC] Read the bad block table starting from page"
---

<p>read_bbt &#8211; [GENERIC] Read the bad block table starting from page</p>
<h2>Synopsis</h2>
<pre><code>int read_bbt(struct mtd_info *mtd, uint8_t *buf, int page, int num, struct nand_bbt_descr *td, int offs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
</dd><dd>MTD device structure</dd></dl>
<p> <i>buf</i></p>
<dl>
<dd>temporary buffer</dd></dl>
<p> <i>page</i></p>
<dl>
<dd>the starting page</dd></dl>
<p> <i>num</i></p>
<dl>
<dd>the number of bbt descriptors to read</dd></dl>
<p> <i>td</i></p>
<dl>
<dd>the bbt describtion table</dd></dl>
<p> <i>offs</i></p>
<dl>
<dd>block number offset in the table</dd></dl>
<h2>Description</h2>
<p>Read the bad block table starting from page.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
