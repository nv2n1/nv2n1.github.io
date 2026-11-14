---
title: "nand_read_page_hwecc_oob_first(9)"
name: "nand_read_page_hwecc_oob_first"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_page_hwecc_oob_first/"
description: "nand_read_page_hwecc_oob_first – [REPLACEABLE] hw ecc, read oob first"
---

<p>nand_read_page_hwecc_oob_first &#8211; [REPLACEABLE] hw ecc, read oob first</p>
<h2>Synopsis</h2>
<pre><code>int nand_read_page_hwecc_oob_first(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page);</code></pre>
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
<p>Hardware ECC for large page chips, require OOB to be read first. For this ECC mode, the write_page method is re-used from ECC_HW. These methods read/write ECC from the OOB area, unlike the ECC_HW_SYNDROME support with multiple ECC steps, follows the &#8220;infix ECC&#8221; scheme and reads/writes ECC from the data area, by overwriting the NAND manufacturer bad block markings.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
