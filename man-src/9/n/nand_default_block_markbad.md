---
title: "nand_default_block_markbad(9)"
name: "nand_default_block_markbad"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_default_block_markbad/"
description: "nand_default_block_markbad – [DEFAULT] mark a block bad via bad block marker"
---

<p>nand_default_block_markbad &#8211; [DEFAULT] mark a block bad via bad block marker</p>
<h2>Synopsis</h2>
<pre><code>int nand_default_block_markbad(struct mtd_info *mtd, loff_t ofs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset from device start</dl>
<h2>Description</h2>
<p>This is the default implementation, which can be overridden by a hardware specific driver. It provides the details for writing a bad block marker to a block.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
