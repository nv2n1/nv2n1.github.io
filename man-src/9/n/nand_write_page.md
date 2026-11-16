---
title: "nand_write_page(9)"
name: "nand_write_page"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_page/"
description: "nand_write_page – [REPLACEABLE] write one page"
---

<p>nand_write_page &#8211; [REPLACEABLE] write one page</p>
<h2>Synopsis</h2>
<pre><code>int nand_write_page(struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, int data_len, const uint8_t *buf, int oob_required, int page, int cached, int raw);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
</dd><dd>MTD device structure</dd></dl>
<p> <i>chip</i></p>
<dl>
<dd>NAND chip descriptor</dd></dl>
<p> <i>offset</i></p>
<dl>
<dd>address offset within the page</dd></dl>
<p> <i>data_len</i></p>
<dl>
<dd>length of actual data to be written</dd></dl>
<p> <i>buf</i></p>
<dl>
<dd>the data to write</dd></dl>
<p> <i>oob_required</i></p>
<dl>
<dd>must write chip-&gt;oob_poi to OOB</dd></dl>
<p> <i>page</i></p>
<dl>
<dd>page number to write</dd></dl>
<p> <i>cached</i></p>
<dl>
<dd>cached programming</dd></dl>
<p> <i>raw</i></p>
<dl>
<dd>use _raw version of write_page</dd></dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
