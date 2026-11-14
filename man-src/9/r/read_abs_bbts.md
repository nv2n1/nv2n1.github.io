---
title: "read_abs_bbts(9)"
name: "read_abs_bbts"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_abs_bbts/"
description: "read_abs_bbts – [GENERIC] Read the bad block table(s) for all chips starting at a given page"
---

<p>read_abs_bbts &#8211; [GENERIC] Read the bad block table(s) for all chips starting at a given page</p>
<h2>Synopsis</h2>
<pre><code>void read_abs_bbts(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md);</code></pre>
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
<p> <i>md</i></p>
<dl>
<dd>descriptor for the bad block table mirror</dl>
<h2>Description</h2>
<p>Read the bad block table(s) for all chips starting at a given page. We assume that the bbt bits are in consecutive order.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
