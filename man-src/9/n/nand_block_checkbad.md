---
title: "nand_block_checkbad(9)"
name: "nand_block_checkbad"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_block_checkbad/"
description: "nand_block_checkbad – [GENERIC] Check if a block is marked bad"
---

<p>nand_block_checkbad &#8211; [GENERIC] Check if a block is marked bad</p>
<h2>Synopsis</h2>
<pre><code>int nand_block_checkbad(struct mtd_info *mtd, loff_t ofs, int allowbbt);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset from device start</dl>
<p> <i>allowbbt</i></p>
<dl>
<dd>1, if its allowed to access the bbt area</dl>
<h2>Description</h2>
<p>Check, if the block is bad. Either by reading the bad block table or calling of the scan function.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
