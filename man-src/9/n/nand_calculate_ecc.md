---
title: "nand_calculate_ecc(9)"
name: "nand_calculate_ecc"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_calculate_ecc/"
description: "nand_calculate_ecc – [NAND Interface] Calculate 3-byte ECC for 256/512-byte block"
---

<p>nand_calculate_ecc &#8211; [NAND Interface] Calculate 3-byte ECC for 256/512-byte block</p>
<h2>Synopsis</h2>
<pre><code>int nand_calculate_ecc(struct mtd_info *mtd, const unsigned char *buf, unsigned char *code);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD block structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>input buffer with raw data</dl>
<p> <i>code</i></p>
<dl>
<dd>output buffer with ECC</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
