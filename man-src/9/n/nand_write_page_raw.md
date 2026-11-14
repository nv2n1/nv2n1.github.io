---
title: "nand_write_page_raw(9)"
name: "nand_write_page_raw"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_page_raw/"
description: "nand_write_page_raw – [INTERN] raw page write function"
---

<p>nand_write_page_raw &#8211; [INTERN] raw page write function</p>
<h2>Synopsis</h2>
<pre><code>int nand_write_page_raw(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page);</code></pre>
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
<p>Not for syndrome calculating ECC controllers, which use a special oob layout.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
