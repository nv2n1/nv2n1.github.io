---
title: "write_bbt(9)"
name: "write_bbt"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_bbt/"
description: "write_bbt – [GENERIC] (Re)write the bad block table"
---

<p>write_bbt &#8211; [GENERIC] (Re)write the bad block table</p>
<h2>Synopsis</h2>
<pre><code>int write_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md, int chipsel);</code></pre>
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
<p> <i>chipsel</i></p>
<dl>
<dd>selector for a specific chip, -1 for all</dl>
<h2>Description</h2>
<p>(Re)write the bad block table.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
