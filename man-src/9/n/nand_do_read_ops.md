---
title: "nand_do_read_ops(9)"
name: "nand_do_read_ops"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_do_read_ops/"
description: "nand_do_read_ops – [INTERN] Read data with ECC"
---

<p>nand_do_read_ops &#8211; [INTERN] Read data with ECC</p>
<h2>Synopsis</h2>
<pre><code>int nand_do_read_ops(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops);</code></pre>
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
<dd>oob ops structure</dl>
<h2>Description</h2>
<p>Internal function. Called with chip held.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
