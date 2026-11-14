---
title: "nand_read_oob_syndrome(9)"
name: "nand_read_oob_syndrome"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_read_oob_syndrome/"
description: "nand_read_oob_syndrome – [REPLACEABLE] OOB data read function for HW ECC with syndromes"
---

<p>nand_read_oob_syndrome &#8211; [REPLACEABLE] OOB data read function for HW ECC with syndromes</p>
<h2>Synopsis</h2>
<pre><code>int nand_read_oob_syndrome(struct mtd_info *mtd, struct nand_chip *chip, int page);</code></pre>
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
<dd>page number to read</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
