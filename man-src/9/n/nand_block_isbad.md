---
title: "nand_block_isbad(9)"
name: "nand_block_isbad"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_block_isbad/"
description: "nand_block_isbad – [MTD Interface] Check if block at offset is bad"
---

<p>nand_block_isbad &#8211; [MTD Interface] Check if block at offset is bad</p>
<h2>Synopsis</h2>
<pre><code>int nand_block_isbad(struct mtd_info *mtd, loff_t offs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>offs</i></p>
<dl>
<dd>offset relative to mtd start</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
