---
title: "nand_write_oob_std(9)"
name: "nand_write_oob_std"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_write_oob_std/"
description: "nand_write_oob_std – [REPLACEABLE] the most common OOB data write function"
---

<p>nand_write_oob_std &#8211; [REPLACEABLE] the most common OOB data write function</p>
<h2>Synopsis</h2>
<pre><code>int nand_write_oob_std(struct mtd_info *mtd, struct nand_chip *chip, int page);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>mtd info structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>nand chip info structure</dl>
<p> <i>page</i></p>
<dl>
<dd>page number to write</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
