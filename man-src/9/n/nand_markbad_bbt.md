---
title: "nand_markbad_bbt(9)"
name: "nand_markbad_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_markbad_bbt/"
description: "nand_markbad_bbt – [NAND Interface] Mark a block bad in the BBT"
---

<p>nand_markbad_bbt &#8211; [NAND Interface] Mark a block bad in the BBT</p>
<h2>Synopsis</h2>
<pre><code>int nand_markbad_bbt(struct mtd_info *mtd, loff_t offs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>offs</i></p>
<dl>
<dd>offset of the bad block</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
