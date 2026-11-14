---
title: "nand_do_read_oob(9)"
name: "nand_do_read_oob"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_do_read_oob/"
description: "nand_do_read_oob – [INTERN] NAND read out-of-band"
---

<p>nand_do_read_oob &#8211; [INTERN] NAND read out-of-band</p>
<h2>Synopsis</h2>
<pre><code>int nand_do_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>from</i></p>
<dl>
<dd>offset to read from</dl>
<p> <i>ops</i></p>
<dl>
<dd>oob operations description structure</dl>
<h2>Description</h2>
<p>NAND read out-of-band data from the spare area.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
