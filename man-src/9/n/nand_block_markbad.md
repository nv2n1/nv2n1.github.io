---
title: "nand_block_markbad(9)"
name: "nand_block_markbad"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_block_markbad/"
description: "nand_block_markbad – [MTD Interface] Mark block at the given offset as bad"
---

<p>nand_block_markbad &#8211; [MTD Interface] Mark block at the given offset as bad</p>
<h2>Synopsis</h2>
<pre><code>int nand_block_markbad(struct mtd_info *mtd, loff_t ofs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset relative to mtd start</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
