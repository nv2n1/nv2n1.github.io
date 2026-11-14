---
title: "nand_correct_data(9)"
name: "nand_correct_data"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_correct_data/"
description: "nand_correct_data – [NAND Interface] Detect and correct bit error(s)"
---

<p>nand_correct_data &#8211; [NAND Interface] Detect and correct bit error(s)</p>
<h2>Synopsis</h2>
<pre><code>int nand_correct_data(struct mtd_info *mtd, unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD block structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>raw data read from the chip</dl>
<p> <i>read_ecc</i></p>
<dl>
<dd>ECC from the chip</dl>
<p> <i>calc_ecc</i></p>
<dl>
<dd>the ECC calculated from raw data</dl>
<h2>Description</h2>
<p>Detect and correct a 1 bit error for 256/512 byte block</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
