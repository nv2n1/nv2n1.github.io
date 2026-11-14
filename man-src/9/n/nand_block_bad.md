---
title: "nand_block_bad(9)"
name: "nand_block_bad"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_block_bad/"
description: "nand_block_bad – [DEFAULT] Read bad block marker from the chip"
---

<p>nand_block_bad &#8211; [DEFAULT] Read bad block marker from the chip</p>
<h2>Synopsis</h2>
<pre><code>int nand_block_bad(struct mtd_info *mtd, loff_t ofs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset from device start</dl>
<h2>Description</h2>
<p>Check, if the block is bad.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
