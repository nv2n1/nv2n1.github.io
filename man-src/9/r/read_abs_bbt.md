---
title: "read_abs_bbt(9)"
name: "read_abs_bbt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_abs_bbt/"
description: "read_abs_bbt – [GENERIC] Read the bad block table starting at a given page"
---

<p>read_abs_bbt &#8211; [GENERIC] Read the bad block table starting at a given page</p>
<h2>Synopsis</h2>
<pre><code>int read_abs_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, int chip);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>temporary buffer</dl>
<p> <i>td</i></p>
<dl>
<dd>descriptor for the bad block table</dl>
<p> <i>chip</i></p>
<dl>
<dd>read the table for a specific chip, -1 read all chips; applies only if NAND_BBT_PERCHIP option is set</dl>
<h2>Description</h2>
<p>Read the bad block table for all chips starting at a given page. We assume that the bbt bits are in consecutive order.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
