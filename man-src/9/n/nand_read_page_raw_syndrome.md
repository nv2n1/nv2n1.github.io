---
title: "nand_read_page_raw_syndrome(9)"
name: "nand_read_page_raw_syndrome"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_page_raw_syndrome/"
description: "nand_read_page_raw_syndrome – [INTERN] read raw page data without ecc"
---

<p>nand_read_page_raw_syndrome &#8211; [INTERN] read raw page data without ecc</p>
<h2>Synopsis</h2>
<pre><code>int nand_read_page_raw_syndrome(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page);</code></pre>
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
<dd>buffer to store read data</dl>
<p> <i>oob_required</i></p>
<dl>
<dd>caller requires OOB data read to chip-&gt;oob_poi</dl>
<p> <i>page</i></p>
<dl>
<dd>page number to read</dl>
<h2>Description</h2>
<p>We need a special oob layout and handling even when OOB isn&#8217;t used.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
