---
title: "nand_isbad_bbt(9)"
name: "nand_isbad_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_isbad_bbt/"
description: "nand_isbad_bbt – [NAND Interface] Check if a block is bad"
---

<p>nand_isbad_bbt &#8211; [NAND Interface] Check if a block is bad</p>
<h2>Synopsis</h2>
<pre><code>int nand_isbad_bbt(struct mtd_info *mtd, loff_t offs, int allowbbt);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>offs</i></p>
<dl>
<dd>offset in the device</dl>
<p> <i>allowbbt</i></p>
<dl>
<dd>allow access to bad block table region</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
