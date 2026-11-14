---
title: "nand_update_bbt(9)"
name: "nand_update_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_update_bbt/"
description: "nand_update_bbt – update bad block table(s)"
---

<p>nand_update_bbt &#8211; update bad block table(s)</p>
<h2>Synopsis</h2>
<pre><code>int nand_update_bbt(struct mtd_info *mtd, loff_t offs);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>offs</i></p>
<dl>
<dd>the offset of the newly marked block</dl>
<h2>Description</h2>
<p>The function updates the bad block table(s).</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
