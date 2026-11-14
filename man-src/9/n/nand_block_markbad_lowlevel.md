---
title: "nand_block_markbad_lowlevel(9)"
name: "nand_block_markbad_lowlevel"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_block_markbad_lowlevel/"
description: "nand_block_markbad_lowlevel – mark a block bad"
---

<p>nand_block_markbad_lowlevel &#8211; mark a block bad</p>
<h2>Synopsis</h2>
<pre><code>int nand_block_markbad_lowlevel(struct mtd_info *mtd, loff_t ofs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset from device start</dl>
<h2>Description</h2>
<p>This function performs the generic NAND bad block marking steps (i.e., bad block table(s) and/or marker(s)). We only allow the hardware driver to specify how to write bad block markers to OOB (chip-&gt;block_markbad). </p>
<p> We try operations in the following order: (1) erase the affected block, to allow OOB marker to be written cleanly (2) write bad block marker to OOB area of affected block (unless flag NAND_BBT_NO_OOB_BBM is present) (3) update the BBT Note that we retain the first error encountered in (2) or (3), finish the procedures, and dump the error in the end.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
