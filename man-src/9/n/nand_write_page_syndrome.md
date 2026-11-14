---
title: "nand_write_page_syndrome(9)"
name: "nand_write_page_syndrome"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_page_syndrome/"
description: "nand_write_page_syndrome – [REPLACEABLE] hardware ECC syndrome based page write"
---

<p>nand_write_page_syndrome &#8211; [REPLACEABLE] hardware ECC syndrome based page write</p>
<h2>Synopsis</h2>
<pre><code>int nand_write_page_syndrome(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page);</code></pre>
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
<h2>Description</h2>
<p>The hw generator calculates the error syndrome automatically. Therefore we need a special oob layout and handling.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
