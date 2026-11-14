---
title: "nand_erase_nand(9)"
name: "nand_erase_nand"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_erase_nand/"
description: "nand_erase_nand – [INTERN] erase block(s)"
---

<p>nand_erase_nand &#8211; [INTERN] erase block(s)</p>
<h2>Synopsis</h2>
<pre><code>int nand_erase_nand(struct mtd_info *mtd, struct erase_info *instr, int allowbbt);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>instr</i></p>
<dl>
<dd>erase instruction</dl>
<p> <i>allowbbt</i></p>
<dl>
<dd>allow erasing the bbt area</dl>
<h2>Description</h2>
<p>Erase one ore more blocks.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
